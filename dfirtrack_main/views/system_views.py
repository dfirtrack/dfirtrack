from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from dfirtrack.config import SYSTEM_NAME_EDITABLE as system_name_editable
from dfirtrack_main.forms import SystemForm, SystemNameForm
from dfirtrack_main.logger.default_logger import debug_logger, warning_logger
from dfirtrack_main.models import Ip, System
from dfirtrack.settings import INSTALLED_APPS as installed_apps
import ipaddress

class SystemList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/systems_list.html'
    context_object_name = 'system_list'

    def get_queryset(self):
        # call logger
        debug_logger(str(self.request.user), " SYSTEM_LIST_ENTERED")
        return System.objects.order_by('system_name')

    # check for dfirtrack_api
    def get_context_data(self, **kwargs):
        # returns context dictionary
        context = super(SystemList, self).get_context_data()
        # check settings for dfirtrack_api in installed_apps
        if 'dfirtrack_api' in installed_apps:
            # add key value pair for 'dfirtrack_api' to dictionary
            context['dfirtrack_api'] = True
        else:
            # add key value pair for 'dfirtrack_api' to dictionary
            context['dfirtrack_api'] = False
        # return dictionary with additional key value pair for 'dfirtrack_api'
        return context

class SystemDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/systems_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        system = self.object
        # call logger
        system.logger(str(self.request.user), " SYSTEM_DETAIL_ENTERED")
        return context

class SystemCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = System
    form_class = SystemNameForm
    template_name = 'dfirtrack_main/system/systems_add.html'

    def get(self, request, *args, **kwargs):
        # show empty form with default values for convenience and speed reasons
        form = self.form_class(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })
        # call logger
        debug_logger(str(request.user), " SYSTEM_ADD_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.system_created_by_user_id = request.user
            system.system_modified_by_user_id = request.user
            system.system_modify_time = timezone.now()
            system.save()
            form.save_m2m()

            # extract lines from ip list
            lines = request.POST.get('iplist').splitlines()
            # call function to save ips
            ips_save(request, system, lines)

            # call logger
            system.logger(str(request.user), ' SYSTEM_ADD_EXECUTED')
            messages.success(request, 'System added')
            return redirect('/systems/' + str(system.system_id))
        else:
            return render(request, self.template_name, {'form': form})

class SystemUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/systems_edit.html'

    # choose form class depending on variable
    if system_name_editable is False:
        form_class = SystemForm
    elif system_name_editable is True:
        form_class = SystemNameForm

    def get(self, request, *args, **kwargs):
        system = self.get_object()

        """ get all existing ip addresses """

        # get objects
        ips = system.ip.all()
        # count objects
        iplen = len(ips)
        # set counter
        i = 0
        # set default string if there is no object at all
        ipstring = ''
        for ip in ips:
            # add ip to string
            ipstring = ipstring + str(ip.ip_ip)
            # increment counter
            i += 1
            # add newline but not for last occurence
            if i < iplen:
                ipstring = ipstring + '\n'

        # show form for system with all ip addresses
        form = self.form_class(
            instance=system,
            initial={
                'iplist': ipstring,
            },
        )
        # call logger
        system.logger(str(request.user), " SYSTEM_EDIT_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        system = self.get_object()
        form = self.form_class(request.POST, instance=system)
        if form.is_valid():
            system = form.save(commit=False)
            system.system_modified_by_user_id = request.user
            system.system_modify_time = timezone.now()
            system.save()
            form.save_m2m()

            # remove all ips to avoid double assignment of beforehand assigned ips
            system.ip.clear()
            # extract lines from ip list
            lines = request.POST.get('iplist').splitlines()
            # call function to save ips
            ips_save(request, system, lines)

            # call logger
            system.logger(str(request.user), ' SYSTEM_EDIT_EXECUTED')
            messages.success(request, 'System edited')
            return redirect('/systems/' + str(system.system_id))
        else:
            return render(request, self.template_name, {'form': form})

def ips_save(request, system, lines):
    # iterate over lines
    for line in lines:
        # skip empty lines
        if line == '':
            # call logger
            warning_logger(str(request.user), ' SYSTEM_ADD_IP_EMPTY_LINE')
            messages.error(request, 'Empty line instead of IP was provided')
            continue
        # check line for ip
        try:
            ipaddress.ip_address(line)
        except ValueError:
            # call logger
            warning_logger(str(request.user), ' SYSTEM_ADD_IP_NO_IP')
            messages.error(request, 'Provided string was no IP')
            continue

        # create ip
        ip, created = Ip.objects.get_or_create(ip_ip=line)
        # call logger
        if created == True:
            ip.logger(str(request.user), ' SYSTEM_ADD_IP_CREATED')
            messages.success(request, 'IP created')
        else:
            messages.warning(request, 'IP already exists in database')

        # save ip for system
        system.ip.add(ip)
