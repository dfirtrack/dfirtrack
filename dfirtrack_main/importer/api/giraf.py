import dateutil.parser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from dfirtrack.config import GIRAF_PASS, GIRAF_URL, GIRAF_USER
from dfirtrack_main.logger.default_logger import debug_logger, error_logger
from dfirtrack_main.models import Domain, Entry, Ip, Os, Osarch, Osimportname, System, Systemstatus, Systemuser
import json
import requests
import urllib

@login_required(login_url="/login")
def systems(request):

    # get user string
    request_user = str(request.user)

    # call logger
    debug_logger(request_user, " API_GIRAF_SYSTEMS_BEGIN")

    # check connection
    try:
        urllib.request.urlopen(GIRAF_URL, timeout=2)
    except:
        # call logger
        error_logger(request_user, " API_GIRAF_SYSTEMS_URL_NOT_AVAILABLE")
        messages.error(request, "GIRAF API URL not available.")
        # call logger (for consistency purposes to show end of api call)
        debug_logger(request_user, " API_GIRAF_SYSTEMS_END")
        return redirect('/systems')

    # get JSON from GIRAF API (returns <class 'requests.models.Response'>)
    system_json = requests.get(GIRAF_URL + '/api/systems/systems/', auth=(GIRAF_USER,GIRAF_PASS))

    # load JSON to list (returns list if authenticated, returns dict else)
    system_list = system_json.json()

    # check for list type (in case of auth error it returns dict)
    if type(system_list) != list:
        """ stop api call because of missing list """
        # call logger
        error_logger(request_user, " API_GIRAF_POSSIBLE_AUTH_ERROR")
        messages.error(request, "GIRAF API possible authentication error.")
        # call logger (for consistency purposes to show end of api call)
        debug_logger(request_user, " API_GIRAF_SYSTEMS_END")
        return redirect('/systems')

    # iterate over systems
    for system_dict in system_list:

        # get hostname and uuid
        try:
            hostname = system_dict['hostname']
        except:
            # leave this loop if there is something wrong with the data
            error_logger(request_user, " API_GIRAF_WRONG_DATA")
            continue

        # get uuid
        uuid = system_dict['uuid']

        # get list of ips
        ip_list = system_dict['ip_address']

        # get list of systemusers
        systemuser_list = system_dict['systemuser']

        # get domain
        domain = system_dict['domain']
        domain, created = Domain.objects.get_or_create(domain_name=domain)

        if created == True:
            # call logger
            domain.logger(request_user, " API_GIRAF_SYSTEMS_DOMAIN_CREATED")

        # get Os
        osimportname = str(system_dict['os']) + " " + str(system_dict['release']) + " " + str(system_dict['version'])
        osimportname, created = Osimportname.objects.get_or_create(
            osimportname_name = osimportname,
            osimportname_importer = 'GIRAF',
            defaults = {'os': Os.objects.get(os_name='tbd')},   # set 'tbd' if no mapping exists, real os will be updated after next api call after mapping
        )

        # get architecture
        osarch = system_dict['machine_type']
        osarch, created = Osarch.objects.get_or_create(osarch_name=osarch)

        if created == True:
            # call logger
            osarch.logger(request_user, " API_GIRAF_SYSTEMS_OSARCH_CREATED")

        # get installation date
        install_date = system_dict['install_date']
        if install_date is not None:
            install_date = dateutil.parser.parse(install_date)

        # get boot time
        last_booted_at = system_dict['last_booted_at']
        if last_booted_at is not None:
            last_booted_at = dateutil.parser.parse(last_booted_at)

        # check for uuid
        system = System.objects.filter(system_uuid=uuid)    
        if not system:      # uuid:no

            # check for hostname
            system = System.objects.filter(system_name=hostname)
            if not system:          # hostname:no

                system = System()   # create new system object
                system.system_name = hostname
                system.systemstatus = Systemstatus.objects.get(systemstatus_name='Unknown')
                system.system_created_by_user_id = request.user
                system.system_modified_by_user_id = request.user
                system.system_modify_time = timezone.now()
                system.save()       # hostname:yes

            #system = System.objects.filter(system_name=hostname, domain.domain_name=domain)
            #if not system:      # if system with this hostname and domain doesn't exit
            #    pass
            #else:
            #    system = System.objects.filter(system_name=hostname, domain.domain_name=domain, system_install_time=FOO)

            system = System.objects.get(system_name=hostname)   # Get system for the case uuid:no hostname:yes
            system.system_uuid = uuid   # uuid:yes
    
            # iterate over ips
            for ip_dict in ip_list:
                ip = ip_dict['ip_address']
                # get or create ip object
                ip, created = Ip.objects.get_or_create(ip_ip=ip)

                if created == True:
                    ip.logger(request_user, " API_GIRAF_SYSTEMS_IP_CREATED")

                # check whether ip already exists for this system otherwise add fk-relationship
                if system.ip.filter(ip_ip=ip.ip_ip).exists() is False:
                    system.ip.add(ip)

            # iterate over systemusers
            for systemuser_dict in systemuser_list:
                systemuser_name = systemuser_dict['username']
                systemuser_lastlogon_time = systemuser_dict['last_logon']
                if systemuser_lastlogon_time is not None:
                    systemuser_lastlogon_time = dateutil.parser.parse(systemuser_lastlogon_time)
                # get or create systemuser object (check isn't required because system is already bind by this)
                systemuser, created = Systemuser.objects.get_or_create(systemuser_name=systemuser_name, system=system)
                # update logon time (not suitable for searching above)
                systemuser.systemuser_lastlogon_time = systemuser_lastlogon_time
                systemuser.save()

                if created == True:
                    systemuser.logger(request_user, " API_GIRAF_SYSTEMS_SYSTEMUSER_CREATED")

            system.domain = domain
            system.os = osimportname.os     # set OS to existing mapping or 'tbd'
            system.osarch = osarch
            system.system_install_time = install_date
            system.system_lastbooted_time = last_booted_at

            # set auto values
            system.system_api_time = timezone.now()

            # save object
            system.save()

            # call logger
            system.logger(request_user, ' API_GIRAF_SYSTEMS_EXECUTED')

        else:           # uuid:yes
    
            system = System.objects.get(system_uuid=uuid)
    
            # iterate over ips
            for ip_dict in ip_list:
                ip = ip_dict['ip_address']
                # get or create ip object
                ip, created = Ip.objects.get_or_create(ip_ip=ip)

                if created == True:
                    ip.logger(request_user, " API_GIRAF_SYSTEMS_IP_CREATED")

                # check whether ip already exists for this system otherwise add fk-relationship
                if system.ip.filter(ip_ip=ip.ip_ip).exists() is False:
                    system.ip.add(ip)

            # iterate over systemusers
            for systemuser_dict in systemuser_list:
                systemuser_name = systemuser_dict['username']
                systemuser_lastlogon_time = systemuser_dict['last_logon']
                if systemuser_lastlogon_time is not None:
                    systemuser_lastlogon_time = dateutil.parser.parse(systemuser_lastlogon_time)
                # get or create systemuser object (check isn't required because system is already bind by this)
                systemuser, created = Systemuser.objects.get_or_create(systemuser_name=systemuser_name, system=system)
                # update logon time (not suitable for searching above)
                systemuser.systemuser_lastlogon_time = systemuser_lastlogon_time
                systemuser.save()

                if created == True:
                    # call logger
                    systemuser.logger(request_user, " API_GIRAF_SYSTEMS_SYSTEMUSER_CREATED")

            system.domain = domain
            system.os = osimportname.os     # set OS to existing mapping or 'tbd'
            system.osarch = osarch
            system.system_install_time = install_date
            system.system_lastbooted_time = last_booted_at

            # set auto values
            system.system_api_time = timezone.now()
            # save object
            system.save()

            # call logger
            system.logger(request_user, ' API_GIRAF_SYSTEMS_EXECUTED')

    # call logger
    debug_logger(request_user, " API_GIRAF_SYSTEMS_END")

    return redirect('/systems')

@login_required(login_url="/login")
def entrys(request):

    # get user string
    request_user = str(request.user)

    # get redirector from GET request
    redirector = request.GET['redirector']

    # call logger
    debug_logger(request_user, " API_GIRAF_ENTRIES_BEGIN")

    # check connection
    try:
        urllib.request.urlopen(GIRAF_URL, timeout=2)
    except:
        # call logger
        error_logger(request_user, " API_GIRAF_ENTRIES_URL_NOT_AVAILABLE")
        messages.error(request, "GIRAF API URL not available.")
        # call logger (for consistency purposes to show end of api call)
        debug_logger(request_user, " API_GIRAF_SYSTEMS_END")
        return redirect('/' + redirector)

    # get JSON from GIRAF API (returns <class 'requests.models.Response'>)
    entry_json = requests.get(GIRAF_URL + '/api/systems/timelines/', auth=(GIRAF_USER,GIRAF_PASS))

    # load JSON to list (returns list if authenticated, returns dict else)
    entry_list = entry_json.json()

    # check for list type (in case of auth error it returns dict)
    if type(entry_list) != list:
        """ stop api call because of missing list """
        # call logger
        error_logger(request_user, " API_GIRAF_POSSIBLE_AUTH_ERROR")
        messages.error(request, "GIRAF API possible authentication error.")
        # call logger (for consistency purposes to show end of api call)
        debug_logger(request_user, " API_GIRAF_ENTRIES_END")
        # redirect depending on redirector from GET request
        return redirect('/' + redirector)

    # iterate over entries
    for entry_dict in entry_list:

        # get entry time
        entry_time = entry_dict['entry_date']
        if entry_time is not None:
            entry_time = dateutil.parser.parse(entry_time )

        # get system
        entry_system_dict = entry_dict['system']
        system_uuid = entry_system_dict['uuid']
        try:
            system = System.objects.get(system_uuid=system_uuid)
        except:
            # call logger
            error_logger(request_user, " API_GIRAF_ENTRIES_UNKNOWN_SYSTEM " + "system_uuid:" + system_uuid)
            messages.error(request, "GIRAF API unknown system UUID: " + system_uuid)
            # leave this loop because system for this entry does not exist yet
            continue

        # get entry sha1
        entry_sha1 = entry_dict['hash_sha1']

        # get entry content
        entry_content = entry_dict['json_content']
        # load JSON to dict
        entry_content = json.loads(entry_content)

        # extract entry content from dict
        entry_date = entry_content['date']
        entry_utc = entry_content['utc']
        entry_system = entry_content['system']
        entry_type = entry_content['type']
        entry_content = entry_content['content']

        # get entry if it already exists
        entry = Entry.objects.filter(system=system, entry_sha1=entry_sha1)

        # only create object if it does not exist yet
        if not entry:

            # create new entry object
            entry = Entry()

            # enter extracted values
            entry.entry_time = entry_time
            entry.system = system
            entry.entry_sha1 = entry_sha1
            entry.entry_date = entry_date
            entry.entry_utc = entry_utc
            entry.entry_system = entry_system
            entry.entry_type = entry_type
            entry.entry_content = entry_content

            # set auto values
            entry.entry_create_time = timezone.now()
            entry.entry_modify_time = timezone.now()
            entry.entry_api_time = timezone.now()
            entry.entry_created_by_user_id = request.user
            entry.entry_modified_by_user_id = request.user

            # save object
            entry.save()

            # call logger
            entry.logger(request_user, ' API_GIRAF_ENTRIES_EXECUTED')

    # call logger
    debug_logger(request_user, " API_GIRAF_ENTRIES_END")

    # redirect depending on redirector from GET request
    return redirect('/' + redirector)
