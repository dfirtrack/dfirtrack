import ipaddress

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView

from dfirtrack.settings import INSTALLED_APPS as installed_apps
from dfirtrack_artifacts.models import Artifact, Artifactstatus
from dfirtrack_config.models import MainConfigModel, UserConfigModel, Workflow
from dfirtrack_main.filter_forms import SystemFilterForm
from dfirtrack_main.forms import SystemForm, SystemNameForm
from dfirtrack_main.logger.default_logger import debug_logger, warning_logger
from dfirtrack_main.models import Analysisstatus, Case, Ip, System, Systemstatus, Tag, Task, Taskstatus


def query_artifact(artifactstatus_list, system):
    """query artifacts with a list of specific artifactstatus"""

    # create empty artifact queryset
    artifacts_merged = Artifact.objects.none()

    # iterate over artifactstatus objects
    for artifactstatus in artifactstatus_list:

        # get artifacts with specific artifactstatus
        artifacts = Artifact.objects.filter(
            artifactstatus=artifactstatus,
            system=system,
        )

        # add artifacts from above query to merge queryset
        artifacts_merged = artifacts | artifacts_merged

    # sort artifacts by id
    artifacts_sorted = artifacts_merged.order_by('artifact_id')

    # return sorted artifacts with specific artifactstatus
    return artifacts_sorted


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
    form_class = SystemFilterForm
    template_name = 'dfirtrack_main/system/system_list.html'

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
        for a better understanding of filter related condition flow, every important comment starts with 'filter: '
        """

        # initialize filter flag (needed for messages)
        filter_flag = False

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user
        )

        # filter: even if the persistence option has been deselected, the initial values must correspond to the current filtering until the view is reloaded or left

        # create dict to initialize form values set by filtering in previous view call
        form_initial = {}

        # check box if persistence option was provided
        if user_config.filter_system_list_keep:
            # set initial value for form
            form_initial['filter_system_list_keep'] = True
        else:
            form_initial['filter_system_list_keep'] = False

        # get case from config
        if user_config.filter_system_list_case:
            # get id
            case_id = user_config.filter_system_list_case.case_id
            # set initial value for form
            form_initial['case'] = case_id
            # set filter flag
            filter_flag = True

        # get tag from config
        if user_config.filter_system_list_tag:
            # get id
            tag_id = user_config.filter_system_list_tag.tag_id
            # set initial value for form
            form_initial['tag'] = tag_id
            # set filter flag
            filter_flag = True

        # filter: pre-select form according to previous filter selection
        context['form'] = self.form_class(initial=form_initial)

        # call logger
        debug_logger(str(self.request.user), " SYSTEM_LIST_ENTERED")

        # info message that filter is active
        if filter_flag:
            messages.info(
                self.request, 'Filter is active. Systems might be incomplete.'
            )

        # return dictionary with additional values for template
        return context

    def form_valid(self, form):
        """save form data to config and call view again"""

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user
        )

        # filter: save filter choices from form in 'system_list' to database and call 'system_list' again with the new filter options

        # get case from form and save to config
        if form.data['case']:
            system_list_case = Case.objects.get(case_id=form.data['case'])
            user_config.filter_system_list_case = system_list_case
        else:
            user_config.filter_system_list_case = None

        # get tag from form and save to config
        if form.data['tag']:
            system_list_tag = Tag.objects.get(tag_id=form.data['tag'])
            user_config.filter_system_list_tag = system_list_tag
        else:
            user_config.filter_system_list_tag = None

        # avoid MultiValueDictKeyError by providing default False if checkbox was empty
        if form.data.get('filter_system_list_keep', False):
            user_config.filter_system_list_keep = True
        else:
            user_config.filter_system_list_keep = False

        # save config
        user_config.save()

        # call view again
        return redirect(reverse('system_list'))


class SystemDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = System
    template_name = 'dfirtrack_main/system/system_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        system = self.object

        '''artifacts'''

        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')

        # get all artifactstatus from database
        artifactstatus_all = Artifactstatus.objects.all()

        # get all artifacts of system for number
        context['artifacts_all'] = Artifact.objects.filter(system=system)

        # get 'open' artifactstatus from config
        artifactstatus_open = main_config_model.artifactstatus_open.all()
        # query artifacts according to subset of artifactstatus open
        context['artifacts_open'] = query_artifact(artifactstatus_open,system=system)

        # get diff between all artifactstatus and open artifactstatu
        artifactstatus_closed = artifactstatus_all.difference(artifactstatus_open)
        # query artifacts according to subset of artifactstatus closed
        context['artifacts_closed'] = query_artifact(artifactstatus_closed,system=system)

        '''tasks'''

        # get all tasks of system for number
        context['tasks_all'] = Task.objects.filter(system=system)

        # get open taskstatus
        taskstatus_open = Taskstatus.objects.filter(taskstatus_name__in=['00_blocked', '10_pending', '20_working'])
        # query tasks according to subset of taskstatus open
        context['tasks_open'] = query_task(taskstatus_open,system=system)

        # get open taskstatus
        taskstatus_closed = Taskstatus.objects.filter(taskstatus_name__in=['30_done', '40_skipped'])
        # query tasks according to subset of taskstatus closed
        context['tasks_closed'] = query_task(taskstatus_closed,system=system)

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
            user_config_username=self.request.user
        )

        # get visibility values from config and add to context
        context['show_artifact'] = user_config.filter_system_detail_show_artifact
        context['show_artifact_closed'] = user_config.filter_system_detail_show_artifact_closed
        context['show_task'] = user_config.filter_system_detail_show_task
        context['show_task_closed'] = user_config.filter_system_detail_show_task_closed
        context['show_technical_information'] = user_config.filter_system_detail_show_technical_information
        context['show_timeline'] = user_config.filter_system_detail_show_timeline
        context['show_virtualization_information'] = user_config.filter_system_detail_show_virtualization_information
        context['show_company_information'] = user_config.filter_system_detail_show_company_information
        context['show_systemuser'] = user_config.filter_system_detail_show_systemuser
        context['show_analystmemo'] = user_config.filter_system_detail_show_analystmemo
        context['show_reportitem'] = user_config.filter_system_detail_show_reportitem

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
    try:
        system_name_editable = MainConfigModel.objects.get(
            main_config_name='MainConfig'
        ).system_name_editable
    except:  # coverage: ignore branch
        system_name_editable = False

    # choose form class depending on variable
    if system_name_editable is False:
        form_class = SystemForm
    elif system_name_editable is True:
        form_class = SystemNameForm
    else:
        # enforce default value False
        form_class = SystemForm

    def get(self, request, *args, **kwargs):
        system = self.get_object()

        # get config model (without try statement 'manage.py migrate' fails (but not in tests))
        try:
            system_name_editable = MainConfigModel.objects.get(
                main_config_name='MainConfig'
            ).system_name_editable
        except:  # coverage: ignore branch
            system_name_editable = False

        # set system_name_editable for template
        if system_name_editable is False:
            system_name_edit = False
        elif system_name_editable is True:
            system_name_edit = True

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
                'system_name_edit': system_name_edit,
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
        user_config_username=request.user
    )

    # clear values
    user_config.filter_system_list_case = None
    user_config.filter_system_list_tag = None

    # save config
    user_config.save()

    return redirect(reverse('system_list'))


@login_required(login_url="/login")
def get_systems_json(request):
    """function to create system query used by datatable JSON"""

    # get referer
    try:
        referer = request.headers['Referer']
    # if '/system/json/' was called directly for some reason
    except KeyError:
        # call 'system_list' properly to refresh this call
        return redirect(reverse('system_list'))

    # get parameters from GET request and parse them accordingly
    get_params = request.GET
    order_column_number = get_params['order[0][column]']
    order_column_name = get_params['columns[' + order_column_number + '][data]']
    order_dir = '' if (get_params['order[0][dir]'] == 'asc') else '-'
    search_value = get_params['search[value]']
    # check that string contains only alphanumerical chars or spaces (or '_','-',':')
    if not all(
        (x.isalnum() or x.isspace() or x == '_' or x == '-' or x == ':')
        for x in search_value
    ):
        search_value = ''

    """get filter values from config"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # system list

    # case filter
    if user_config.filter_system_list_case:
        # get filter values from config
        system_list_case = Case.objects.get(
            case_id=user_config.filter_system_list_case.case_id
        )
    else:
        system_list_case = None

    # tag filter
    if user_config.filter_system_list_tag:
        # get filter values from config
        system_list_tag = Tag.objects.get(
            tag_id=user_config.filter_system_list_tag.tag_id
        )
    else:
        system_list_tag = None

    # assignment view

    # case filter
    if user_config.filter_assignment_view_case:
        # get filter values from config
        assignment_view_case = Case.objects.get(
            case_id=user_config.filter_assignment_view_case.case_id
        )
    else:
        assignment_view_case = None

    # tag filter
    if user_config.filter_assignment_view_tag:
        # get filter values from config
        assignment_view_tag = Tag.objects.get(
            tag_id=user_config.filter_assignment_view_tag.tag_id
        )
    else:
        assignment_view_tag = None

    # user filter
    if user_config.filter_assignment_view_user:
        # get filter values from config
        assignment_view_user = user_config.filter_assignment_view_user
    else:
        assignment_view_user = None

    """ no search value in datatable search field """

    # if no search value is given, get all objects and order them according to user setting
    # if the table is not generated on the general system overview page, only show the systems with the relevant id
    if search_value == '':

        # start with full query
        system_values = System.objects.all().order_by(order_dir + order_column_name)

        # system list
        if '/system/' in referer:
            # filter: filtering for case and tag is only applied to 'system_list'
            if system_list_case:
                system_values = system_values.filter(case=system_list_case)
            if system_list_tag:
                system_values = system_values.filter(tag=system_list_tag)
        # analysisstatus detail
        elif '/analysisstatus/' in referer:
            analysisstatus_id = referer.split("/")[-2]
            system_values = system_values.filter(
                analysisstatus__analysisstatus_id=analysisstatus_id
            ).order_by(order_dir + order_column_name)
        # systemstatus detail
        elif '/systemstatus/' in referer:
            systemstatus_id = referer.split("/")[-2]
            system_values = system_values.filter(
                systemstatus__systemstatus_id=systemstatus_id
            ).order_by(order_dir + order_column_name)
        # case detail
        elif '/case/' in referer:
            case_id = referer.split("/")[-2]
            system_values = system_values.filter(case__case_id=case_id).order_by(
                order_dir + order_column_name
            )
        # tag detail
        elif '/tag/' in referer:
            tag_id = referer.split("/")[-2]
            system_values = system_values.filter(tag__tag_id=tag_id).order_by(
                order_dir + order_column_name
            )
        # assignment view
        elif '/assignment/' in referer:
            if assignment_view_case:
                system_values = system_values.filter(case=assignment_view_case)
            if assignment_view_tag:
                system_values = system_values.filter(tag=assignment_view_tag)
            if assignment_view_user:
                system_values = system_values.filter(
                    system_assigned_to_user_id=assignment_view_user
                )
            else:
                system_values = system_values.filter(system_assigned_to_user_id=None)
        # catch-all rule to prevent empty 'system_values' if the datatable is included in other views in the future
        else:
            system_values = system_values

    # """ search value in datatable search field """

    # if search value is given, go through all cloumn-raw-data and search for it
    else:

        # start with empty query
        system_values = System.objects.none()

        # to keep the search dynamic and not hardcode the fields, we go through all columns as they are found in the request here
        for entry in get_params:
            # this matches on these lines: ''' columns[0][data]': ['system_id/system_name/...'] '''
            if '][data]' in entry:
                tmp_column_name = get_params[entry]
                # we start with an empty queryset and add all systems that have a match in one of their relevant fields
                try:
                    # filter_kwargs is necessary for dynamic filter design
                    filter_kwargs = {tmp_column_name + '__icontains': search_value}
                    # analysisstatus detail
                    if '/analysisstatus/' in referer:
                        analysisstatus_id = referer.split("/")[-2]
                        filter_kwargs[
                            "analysisstatus__analysisstatus_id"
                        ] = analysisstatus_id
                    # systemstatus detail
                    elif '/systemstatus/' in referer:
                        systemstatus_id = referer.split("/")[-2]
                        filter_kwargs["systemstatus__systemstatus_id"] = systemstatus_id
                    # case detail
                    elif '/case/' in referer:
                        case_id = referer.split("/")[-2]
                        filter_kwargs["case__case_id"] = case_id
                    # tag detail
                    elif '/tag/' in referer:
                        tag_id = referer.split("/")[-2]
                        filter_kwargs["tag__tag_id"] = tag_id
                    # apply search filter
                    system_values = system_values | System.objects.filter(
                        **filter_kwargs
                    )
                # for foreign keys, an exception is thrown, need to modify filter_kwargs accordingly
                except FieldError:
                    filter_kwargs = {
                        tmp_column_name
                        + '__'
                        + tmp_column_name
                        + '_name'
                        + '__icontains': search_value
                    }
                    # analysisstatus detail
                    if '/analysisstatus/' in referer:
                        analysisstatus_id = referer.split("/")[-2]
                        filter_kwargs[
                            "analysisstatus__analysisstatus_id"
                        ] = analysisstatus_id
                    # systemstatus detail
                    elif '/systemstatus/' in referer:
                        systemstatus_id = referer.split("/")[-2]
                        filter_kwargs["systemstatus__systemstatus_id"] = systemstatus_id
                    # case detail
                    elif '/case/' in referer:
                        case_id = referer.split("/")[-2]
                        filter_kwargs["case__case_id"] = case_id
                    # tag detail
                    elif '/tag/' in referer:
                        tag_id = referer.split("/")[-2]
                        filter_kwargs["tag__tag_id"] = tag_id
                    # apply search filter
                    system_values = system_values | System.objects.filter(
                        **filter_kwargs
                    )

        # system list
        if '/system/' in referer:
            # filter: filtering for case and tag is only applied to 'system_list'
            if system_list_case:
                system_values = system_values.filter(case=system_list_case)
            if system_list_tag:
                system_values = system_values.filter(tag=system_list_tag)
        # assignment view
        elif '/assignment/' in referer:
            if assignment_view_case:
                system_values = system_values.filter(case=assignment_view_case)
            if assignment_view_tag:
                system_values = system_values.filter(tag=assignment_view_tag)
            if assignment_view_user:
                system_values = system_values.filter(
                    system_assigned_to_user_id=assignment_view_user
                )
            else:
                system_values = system_values.filter(system_assigned_to_user_id=None)

        # make the resulting queryset unique and sort it according to user settings
        system_values = system_values.distinct().order_by(order_dir + order_column_name)

    # starting point for records in table
    start = int(get_params['start'])
    # how many records are to be shown? if all records are to be shown, length is set to -1
    length = (
        int(get_params['length'])
        if int(get_params['length']) != -1
        else len(system_values)
    )

    # if there is a search value check that the search value really occurs in one of the visible fields in the table (it is possible that the value only occurs e.g. only in the milliseconds of the data field)
    if search_value != '':
        for i in system_values:
            # extract values from system object
            system_id = i.system_id
            system_name = i.system_name
            systemstatus = i.systemstatus
            analysisstatus = i.analysisstatus
            system_create_time = i.system_create_time.strftime("%Y-%m-%d %H:%M")
            system_modify_time = i.system_modify_time.strftime("%Y-%m-%d %H:%M")

            search_relevant_strings = [
                str(system_id),
                str(system_name),
                str(systemstatus),
                str(analysisstatus),
                str(system_create_time),
                str(system_modify_time),
            ]
            really_contains_search_string = False
            # go through visible fields and check if search string is contained
            for field in search_relevant_strings:
                if search_value in field:
                    really_contains_search_string = True
            # if the searched string was not found, exclude system from queryset
            if not really_contains_search_string:
                system_values = system_values.exclude(system_id=system_id)

    # all matching systems
    system_count = len(system_values)
    # construct the final list with systems that are presented to user
    visible_system_list = []
    for i in system_values[start : (start + length)]:
        # construct the data to be presented in the system table, important: if you add something here, make sure you also add it above in the cleaned_system_values generation to stay consistent
        visible_system_list.append(
            {
                "system_id": i.system_id,
                "system_name": "<a href='"
                + i.get_absolute_url()
                + "' type='button' class='btn btn-primary btn-sm copy-true'><img src='"
                + static("dfirtrack_main/icons/monitor-light.svg")
                + "' class='icon right-distance copy-false' alt='icon'>"
                + i.system_name
                + "</a>",
                "systemstatus": render_to_string(
                    'dfirtrack_main/includes/button_systemstatus.html',
                    {'systemstatus': i.systemstatus},
                ),
                "analysisstatus": "<span data-toggle='tooltip' data-placement='auto' title='"
                + str(i.analysisstatus.analysisstatus_note or "")
                + "'><a href='"
                + i.analysisstatus.get_absolute_url()
                + "'>"
                + str(i.analysisstatus)
                + "</a></span>"
                if i.analysisstatus is not None
                else "---",
                "system_create_time": i.system_create_time.strftime("%Y-%m-%d %H:%M"),
                "system_modify_time": i.system_modify_time.strftime("%Y-%m-%d %H:%M"),
            }
        )

    # prepare dictionary with relevant data to convert to json
    json_dict = {}
    json_dict['draw'] = int(get_params['draw'])
    json_dict['recordsTotal'] = len(System.objects.all())
    json_dict['recordsFiltered'] = system_count
    json_dict['data'] = visible_system_list

    # filter: clean filtering after providing filter results if persistence option was not selected
    if not user_config.filter_system_list_keep:
        # unset filter case
        user_config.filter_system_list_case = None
        # unset filter tag
        user_config.filter_system_list_tag = None
        # save config
        user_config.save()

    # convert dict with data to jsonresponse
    response = JsonResponse(json_dict, safe=False)

    return response


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
