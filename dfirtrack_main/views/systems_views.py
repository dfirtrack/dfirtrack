from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import SystemForm
from dfirtrack_main.logger.default_logger import debug_logger, warning_logger
from dfirtrack_main.models import Ip, System
from dfirtrack.settings import INSTALLED_APPS as installed_apps
import ipaddress

class Systems(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/systems_list.html'
    def get_queryset(self):
        # call logger
        debug_logger(str(self.request.user), " SYSTEM_ENTERED")
        return System.objects.order_by('system_name')

    # check for dfirtrack_api
    def get_context_data(self, **kwargs):
        # returns context dictionary
        context = super(Systems, self).get_context_data()
        print("context type: " + str(type(context)))
        print("context: " + str(context))
        # check settings for dfirtrack_api in installed_apps
        if 'dfirtrack_api' in installed_apps:
            # add key value pair for 'dfirtrack_api' to dictionary
            context['dfirtrack_api'] = True
        else:
            # add key value pair for 'dfirtrack_api' to dictionary
            context['dfirtrack_api'] = False
        # return dictionary with additional key value pair for 'dfirtrack_api'
        return context

class SystemsDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/systems_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        system = self.object
        # call logger
        system.logger(str(self.request.user), " SYSTEMDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def systems_add(request):
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.system_created_by_user_id = request.user
            system.system_modified_by_user_id = request.user
            system.system_modify_time = timezone.now()
            system.save()
            form.save_m2m()

            # get user string
            request_user = str(request.user)
            # extract lines from ip list
            lines = request.POST.get('iplist').splitlines()
            # call function to save ips
            ips_save(request, system, lines)

            # call logger
            system.logger(str(request.user), ' SYSTEM_ADD_EXECUTED')
            messages.success(request, 'System added')
            return redirect('/systems/' + str(system.system_id))
    else:
        # show empty form with default values for convenience and speed reasons
        form = SystemForm(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })
        # call logger
        debug_logger(str(request.user), " SYSTEM_ADD_ENTERED")
    return render(request, 'dfirtrack_main/system/systems_add.html', {'form': form})

@login_required(login_url="/login")
def systems_edit(request, pk):
    system = get_object_or_404(System, pk=pk)
    if request.method == 'POST':
        form = SystemForm(request.POST, instance=system)
        if form.is_valid():
            system = form.save(commit=False)
            system.system_modified_by_user_id = request.user
            system.system_modify_time = timezone.now()
            system.save()
            form.save_m2m()

            system.ip.clear()
            # get user string
            request_user = str(request.user)
            # extract lines from ip list
            lines = request.POST.get('iplist').splitlines()
            # call function to save ips
            ips_save(request, system, lines)

            # call logger
            system.logger(str(request.user), ' SYSTEM_EDIT_EXECUTED')
            messages.success(request, 'System edited')
            return redirect('/systems/' + str(system.system_id))
    else:
        system = System.objects.get(system_id = pk)

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
        form = SystemForm(
            instance=system,
            initial={
                'iplist': ipstring,
            },
        )
        # call logger
        system.logger(str(request.user), " SYSTEM_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/system/systems_edit.html', {'form': form})

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
