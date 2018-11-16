from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.shortcuts import redirect
from django_q.tasks import async_task
from dfirtrack.config import MARKDOWN_PATH
from dfirtrack_main.exporter.markdown import clean_directory, config_check, write_report
from dfirtrack_main.logger.default_logger import debug_logger, info_logger
from dfirtrack_main.models import System
from time import strftime
import yaml


def write_report_systemsorted(system, request_user):
    """ function that prepares return values and pathes """

    """
    the return values (prefix 'r') are used for the `mkdocs.yml` file
    they build the key-value-pair for every system
    """

    # return system_id for mkdocs.yml
    rid = str(system.system_id)

    # return fqdn for mkdocs.yml
    if system.system_dnssuffix != None:
        rfqdn = system.system_name + "." + system.system_dnssuffix
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

    # finish path for markdown file
    path = MARKDOWN_PATH + "/docs/systems/" + path + ".md"

    # open file for system
    report = open(path, "w")
    django_report = File(report)

    # write systemreport
    write_report.write_report(django_report, system)

    # close and save file
    django_report.closed
    report.close()

    # call logger
    info_logger(request_user, " SYSTEM_MARKDOWN_CREATED system_id:" + str(system.system_id) + "|system_name:" + str(system.system_name))

    # return strings for mkdocs.yml (only used in systemsorted_async)
    return(rid, rfqdn, rpath)


@login_required(login_url="/login")
def systemsorted(request):
    """ exports markdown report for all systems (helper function to call the real function) """

    request_user = str(request.user)

    # call logger
    debug_logger(request_user, " SYSTEM_MARKDOWN_ALL_SYSTEMS_BEGIN")

    # check for existing variable MARKDOWN_PATH
    config_check(request)

    # call async function
    async_task(
        "dfirtrack_main.exporter.markdown.systemsorted.systemsorted_async",
        request_user,
    )

    return redirect('/systems')


def systemsorted_async(request_user):
    """ exports markdown report for all systems """

    # call directory cleaning function
    clean_directory.clean_directory(request_user)

    # get all systems
    systems = System.objects.all().order_by('system_name')

    # create empty list and dict (needed for mkdocs.yml)
    systemlist = []
    systemdict = {}

    # iterate over systems
    for system in systems:

        # call writing function (and get return values)
        rid, rfqdn, rpath = write_report_systemsorted(system, request_user)

        """ build a dict that is used for the system section in mkdocs.yml """

        # build string as key for systemdict (needed for mkdocs.yml)
        index = rfqdn + " (" + rid + ")"
        # add value to key in 1-value dict (needed for mkdocs.yml)
        systemdict[index] = rpath
        # add dict to list (needed for mkdocs.yml)
        systemlist.append(systemdict)
        # set dict to empty dict (needed for mkdocs.yml)
        systemdict = {}

    # get path for mkdocs.yml
    mkdconfpath = MARKDOWN_PATH + "/mkdocs.yml"

    # open mkdocs.yml for reading
    mkdconffile = open(mkdconfpath, "r")

    # read YAML to dict
    mkdconfdict = yaml.load(mkdconffile)

    # close mkdocs.yml
    mkdconffile.close()

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
        except:
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

    mkdconffile.close()

    # call logger
    debug_logger(request_user, " SYSTEM_MARKDOWN_ALL_SYSTEMS_END")
