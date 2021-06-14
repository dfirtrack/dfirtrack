from django.core.files import File
from django_q.tasks import async_task
from dfirtrack_config.models import MainConfigModel, SystemExporterMarkdownConfigModel
from dfirtrack_main.exporter.markdown.messages import end_message, start_message
from dfirtrack_main.exporter.markdown import clean_directory, read_or_create_mkdocs_yml, write_report
from dfirtrack_main.logger.default_logger import debug_logger, info_logger
from dfirtrack_main.models import System
from time import strftime
import yaml


def write_report_systemsorted(system, username):
    """ function that prepares return values and pathes """

    """
    the return values (prefix 'r') are used for the `mkdocs.yml` file
    they build the key-value-pair for every system
    """

    # return system_id for mkdocs.yml
    rid = str(system.system_id)

    # return fqdn for mkdocs.yml
    if system.dnsname != None:
        rfqdn = system.system_name + "." + system.dnsname.dnsname_name
    else:
        rfqdn = system.system_name

    """
    build the path for every file
    it is distinguished between the short version for the `mkdocs.yml` file ('value' of key-value-pair)
    and the long version that is used to write to the file system
    """

    # build path
    path = system.system_name

    # check for domain and add to path
    if system.domain != None:
        path = path + "_" + system.domain.domain_name

    # check for system_install_time and add to path
    if system.system_install_time != None:
        install_time = system.system_install_time.strftime('%Y%m%d_%H%M%S')
        path = path + "_" + install_time

    # return shortened path for mkdocs.yml ('value')
    rpath = "systems/" + path + ".md"

    # get config model
    model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')

    # finish path for markdown file
    path = model.markdown_path + "/docs/systems/" + path + ".md"

    # open file for system
    report = open(path, "w")
    django_report = File(report)

    # write systemreport
    write_report.write_report(django_report, system)

    # close and save file
    django_report.closed
    report.close()

    # call logger
    info_logger(username, " SYSTEM_MARKDOWN_CREATED system_id:" + str(system.system_id) + "|system_name:" + str(system.system_name))

    # return strings for mkdocs.yml (only used in systemsorted_async)
    return(rid, rfqdn, rpath)

def systemsorted(request=None):
    """ exports markdown report for all systems (helper function to call the real function) """

    # get username
    if request:
        # get username from request object
        username = str(request.user)
    else:
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name = 'MainConfig')
        # get username from config
        username = main_config_model.cron_username

    # call logger
    debug_logger(username, " SYSTEM_EXPORTER_MARKDOWN_SYSTEMSORTED_START")

    # show immediate message for user (but only if no errors have occured before)
    if request:
        start_message(request, 'system')

    # call async function
    if request:
        async_task(
            "dfirtrack_main.exporter.markdown.systemsorted.systemsorted_async",
            username,
            request.user,
        )
    else:
        async_task(
            "dfirtrack_main.exporter.markdown.systemsorted.systemsorted_async",
            username,
        )

    return

def systemsorted_async(username, request_user=None):
    """ exports markdown report for all systems """

    # call directory cleaning function
    clean_directory.clean_directory(username)

    # get all systems
    systems = System.objects.all().order_by('system_name')

    # create empty list and dict (needed for mkdocs.yml)
    systemlist = []
    systemdict = {}

    # iterate over systems
    for system in systems:

        # skip system depending on export variable
        if system.system_export_markdown == False:
            continue

        # call writing function (and get return values)
        rid, rfqdn, rpath = write_report_systemsorted(system, username)

        """ build a dict that is used for the system section in mkdocs.yml """

        # build string as key for systemdict (needed for mkdocs.yml)
        index = rfqdn + " (" + rid + ")"
        # add value to key in 1-value dict (needed for mkdocs.yml)
        systemdict[index] = rpath
        # add dict to list (needed for mkdocs.yml)
        systemlist.append(systemdict)
        # set dict to empty dict (needed for mkdocs.yml)
        systemdict = {}

    # get config model
    model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')

    # get path for mkdocs.yml
    mkdconfpath = model.markdown_path + "/mkdocs.yml"

    # read content (dictionary) of mkdocs.yml if existent, else create dummy content
    mkdconfdict = read_or_create_mkdocs_yml.read_or_create_mkdocs_yml(username, mkdconfpath)

    # get pages list
    mkdconflist = mkdconfdict['pages']

    # set counter
    i = 0
    j = 0

    # iterate over 'pages' list
    for item in mkdconflist:

        # find subsection 'Systems' in list
        try:
            dummy = item['Systems']
            # set index
            j = i
        except:     # coverage: ignore branch
            # do nothing
            pass

        # autoincrement counter for next loop
        i += 1

    # set at dict 'Systems' in list mkdconflist at index j (replace section 'Systems')
    mkdconflist[j]['Systems'] = systemlist

    # set pages with old entries and new 'Systems' section
    mkdconfdict['pages'] = mkdconflist

    # open mkdocs.yml for writing (new file)
    mkdconffile = open(mkdconfpath, "w")
    yaml.dump(mkdconfdict, mkdconffile)

    # close file
    mkdconffile.close()

    # finish message
    if request_user:
        end_message(request_user, 'system')

    # call logger
    debug_logger(username, " SYSTEM_EXPORTER_MARKDOWN_SYSTEMSORTED_END")
