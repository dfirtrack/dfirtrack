import ipaddress

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView

from dfirtrack.settings import INSTALLED_APPS as installed_apps
from dfirtrack_artifacts.models import Artifact
from dfirtrack_config.models import MainConfigModel, UserConfigModel, Workflow
from dfirtrack_main.filter_forms import GeneralFilterForm
from dfirtrack_main.forms import SystemForm, SystemNameForm
from dfirtrack_main.logger.default_logger import debug_logger, warning_logger
from dfirtrack_main.models import (
    Analysisstatus,
    Ip,
    System,
    Systemstatus,
    Task,
    Taskstatus,
)


def query_task(taskstatus_list, system):
    """query tasks with a list of specific taskstatus"""

    # create empty task queryset
    tasks_merged = Task.objects.none()

    # iterate over taskstatus objects
    for taskstatus in taskstatus_list:
        # get tasks with specific taskstatus
        tasks = Task.objects.filter(
            taskstatus=taskstatus,
            system=system,
        )

        # add tasks from above query to merge queryset
        tasks_merged = tasks | tasks_merged

    # sort tasks by id
    tasks_sorted = tasks_merged.order_by('task_id')

    # return sorted tasks with specific taskstatus
    return tasks_sorted


class SystemList(LoginRequiredMixin, FormView):
    login_url = '/login'
    form_class = GeneralFilterForm
    template_name = 'dfirtrack_main/system/system_list.html'
    filter_view = 'system_list'

    def get_context_data(self, **kwargs):
        """enrich context data"""

        # get context
        context = super().get_context_data()

        """ dfirtrack api settings """

        # set dfirtrack_api for template
        if 'dfirtrack_api' in installed_apps:
            context['dfirtrack_api'] = True
        else:
            context['dfirtrack_api'] = False

        """
        filter: provide initial form values according to config
        """

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user, filter_view=self.filter_view
        )

        # filter: pre-select form according to previous filter selection
        context['form'] = self.form_class(instance=user_config)

        # call logger
        debug_logger(str(self.request.user), " SYSTEM_LIST_ENTERED")

        # info message that filter is active
        if user_config.is_filter_active():
            messages.info(
                self.request, 'Filter is active. Systems might be incomplete.'
            )

        # return dictionary with additional values for template
        return context

    def post(self, request, *args, **kwargs):
        """save form data to config and call view again"""
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user, filter_view=self.filter_view
        )

        form = self.form_class(request.POST, instance=user_config)

        if form.is_valid():
            user_config = form.save(commit=False)
            user_config.save()
            form.save_m2m()

        # call view again
        return redirect(reverse('system_list'))


class SystemDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/system_detail.html'
    filter_view = 'system_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        system = self.object

        '''artifacts'''

        # get all artifacts of system for number
        context['artifacts_number'] = Artifact.objects.filter(system=system).count()

        '''tasks'''

        # get all tasks of system for number
        context['tasks_all'] = Task.objects.filter(system=system)

        # get open taskstatus
        taskstatus_open = Taskstatus.objects.filter(
            taskstatus_name__in=['00_blocked', '10_pending', '20_working']
        )
        # query tasks according to subset of taskstatus open
        context['tasks_open'] = query_task(taskstatus_open, system=system)

        # get open taskstatus
        taskstatus_closed = Taskstatus.objects.filter(
            taskstatus_name__in=['30_done', '40_skipped']
        )
        # query tasks according to subset of taskstatus closed
        context['tasks_closed'] = query_task(taskstatus_closed, system=system)

        '''api'''

        # set dfirtrack_api for template
        if 'dfirtrack_api' in installed_apps:
            context['dfirtrack_api'] = True
        else:
            context['dfirtrack_api'] = False

        '''workflows'''

        # get all workflows
        context['workflows'] = Workflow.objects.all()

        '''visibility'''

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user, filter_view=self.filter_view
        )

        # get visibility values from config and add to context
        if user_config.filter_view_show:
            context.update(user_config.filter_view_show)
        else:
            user_config.filter_view_show = {
                'show_artifact': True,
                'show_artifact_closed': False,
                'show_task': True,
                'show_task_closed': False,
                'show_technical_information': False,
                'show_timeline': False,
                'show_virtualization_information': False,
                'show_company_information': False,
                'show_systemuser': False,
                'show_analystmemo': False,
                'show_reportitem': False,
            }
            user_config.save()

        # call logger
        system.logger(str(self.request.user), " SYSTEM_DETAIL_ENTERED")
        return context


class SystemCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = System
    form_class = SystemNameForm
    template_name = 'dfirtrack_main/system/system_add.html'

    def get(self, request, *args, **kwargs):
        # get id of first status objects sorted by name
        systemstatus = Systemstatus.objects.order_by('systemstatus_name')[
            0
        ].systemstatus_id
        analysisstatus = Analysisstatus.objects.order_by('analysisstatus_name')[
            0
        ].analysisstatus_id

        # get all workflows
        workflows = Workflow.objects.all()

        # show empty form with default values for convenience and speed reasons
        form = self.form_class(
            initial={
                'systemstatus': systemstatus,
                'analysisstatus': analysisstatus,
            }
        )
        # call logger
        debug_logger(str(request.user), " SYSTEM_ADD_ENTERED")
        return render(
            request, self.template_name, {'form': form, 'workflows': workflows}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.system_created_by_user_id = request.user
            system.system_modified_by_user_id = request.user
            system.save()
            form.save_m2m()

            # extract lines from ip list
            lines = request.POST.get('iplist').splitlines()
            # call function to save ips
            ips_save(request, system, lines)

            # workflow handling
            if 'workflow' in request.POST:
                error_code = Workflow.apply(
                    request.POST.getlist("workflow"), system, request.user
                )
                if error_code:
                    messages.warning(request, 'Could not apply workflow')
                else:
                    messages.success(request, 'Workflow applied')

            # call logger
            system.logger(str(request.user), ' SYSTEM_ADD_EXECUTED')
            messages.success(request, 'System added')
            return redirect(reverse('system_detail', args=(system.system_id,)))
        else:
            return render(request, self.template_name, {'form': form})


class SystemUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/system_edit.html'

    # get config model (without try statement 'manage.py migrate' fails (but not in tests))
    def __init__(self, *args, **kwargs) -> None:
        try:
            system_name_editable = MainConfigModel.objects.get(
                main_config_name='MainConfig'
            ).system_name_editable
        except:  # coverage: ignore branch
            system_name_editable = False

        # choose form class depending on variable
        self.form_class = SystemForm
        if system_name_editable is True:
            self.form_class = SystemNameForm
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        system = self.get_object()

        # get config model (without try statement 'manage.py migrate' fails (but not in tests))
        try:
            system_name_editable = MainConfigModel.objects.get(
                main_config_name='MainConfig'
            ).system_name_editable
        except:  # coverage: ignore branch
            system_name_editable = False

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
            # add newline but not for last occurrence
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
        return render(
            request,
            self.template_name,
            {
                'form': form,
                # boolean variable is used in template
                'system_name_edit': system_name_editable,
                # return system object in context for use in template
                'system': system,
            },
        )

    def post(self, request, *args, **kwargs):
        system = self.get_object()
        form = self.form_class(request.POST, instance=system)
        if form.is_valid():
            system = form.save(commit=False)
            system.system_modified_by_user_id = request.user
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
            return redirect(reverse('system_detail', args=(system.system_id,)))
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


@login_required(login_url="/login")
def clear_system_list_filter(request):
    """clear system list filter"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user, filter_view='system_list'
    )

    # clear values
    user_config.filter_list_case = None
    user_config.filter_list_assigned_to_user_id = None
    user_config.filter_list_tag.clear()

    # save config
    user_config.save()

    return redirect(reverse('system_list'))


class SystemSetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):
        system = self.get_object()
        system.system_assigned_to_user_id = request.user
        system.save()
        system.logger(str(request.user), " SYSTEM_SET_USER_EXECUTED")
        messages.success(request, 'System assigned to you')

        # redirect
        return redirect(reverse('system_detail', args=(system.system_id,)))


class SystemUnsetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):
        system = self.get_object()
        system.system_assigned_to_user_id = None
        system.save()
        system.logger(str(request.user), " SYSTEM_UNSET_USER_EXECUTED")
        messages.warning(request, 'User assignment for system deleted')

        # redirect
        return redirect(reverse('system_detail', args=(system.system_id,)))
