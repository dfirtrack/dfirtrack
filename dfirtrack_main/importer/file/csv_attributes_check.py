from django.contrib import messages
from dfirtrack_main.logger.default_logger import warning_logger
from dfirtrack_main.models import Ip
import ipaddress


def check_and_create_ip(ip_ip, row_counter, request=None):

    # value is an IP
    try:

        # check ip column for IP(s)
        ipaddress.ip_address(ip_ip)

        # create ip
        ip, created = Ip.objects.get_or_create(ip_ip=ip_ip)
        # IP was created
        if created:
            # call logger
            ip.logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_IP_CREATED")

        # return to 'add_many2many_attributes'
        return ip

    # value is not an IP
    except ValueError:

        # if function was called from 'system_instant' and 'system_upload'
        if request:
            # call message
            messages.warning(request, "Value for ip address in row " + str(row_counter) + " was not a valid IP address.")

        # call logger
        warning_logger(str(request.user), " SYSTEM_IMPORTER_FILE_CSV_IP_COLUMN " + "row_" + str(row_counter) + ":invalid_ip")

        # return to 'add_many2many_attributes'
        return None
