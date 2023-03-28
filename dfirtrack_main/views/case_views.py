from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from dfirtrack.settings import INSTALLED_APPS as installed_apps
from dfirtrack_artifacts.models import Artifact
from dfirtrack_config.models import MainConfigModel
from dfirtrack_main.forms import CaseForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case, Casepriority, Casestatus


def query_case(casestatus_list):
    """query cases with a list of specific casestatus"""

    # create empty case queryset
    cases_merged = Case.objects.none()

    # iterate over casestatus objects
    for casestatus in casestatus_list:
        # get cases with specific casestatus
        cases = Case.objects.filter(casestatus=casestatus)

        # add cases from above query to merge queryset
        cases_merged = cases | cases_merged

    # sort cases by id
    cases_sorted = cases_merged.order_by('case_id')

    # return sorted cases with specific casestatus
    return cases_sorted


class CaseList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Case
    template_name = 'dfirtrack_main/case/case_list.html'
    context_object_name = 'case_list'

    def get_queryset(self):
        # call logger
        debug_logger(str(self.request.user), ' CASE_LIST_ENTERED')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')

        """ get all cases with casestatus to be considered open """

        # get 'open' casestatus from config
        casestatus_open = main_config_model.casestatus_open.all()
        # guery cases according to subset of casestatus open
        cases = query_case(casestatus_open)

        # return cases according to query
        return cases


class CaseClosed(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Case
    template_name = 'dfirtrack_main/case/case_closed.html'
    context_object_name = 'case_list'

    def get_queryset(self):
        # call logger
        debug_logger(str(self.request.user), ' CASE_CLOSED_ENTERED')
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')

        """ get all cases with casestatus to be considered closed """

        # get all casestatus from database
        casestatus_all = Casestatus.objects.all()
        # get 'open' casestatus from config
        casestatus_open = main_config_model.casestatus_open.all()
        # get diff between all casestatus and open casestatus
        casestatus_closed = casestatus_all.difference(casestatus_open)

        # guery cases according to subset of casestatus closed
        cases = query_case(casestatus_closed)
        # return cases according to query
        return cases


class CaseAll(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Case
    template_name = 'dfirtrack_main/case/case_all.html'
    context_object_name = 'case_list'

    def get_queryset(self):
        # call logger
        debug_logger(str(self.request.user), ' CASE_ALL_ENTERED')
        return Case.objects.order_by('case_id')


class CaseDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Case
    template_name = 'dfirtrack_main/case/case_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        case = self.object

        # set dfirtrack_artifacts for template
        if 'dfirtrack_artifacts' in installed_apps:
            context['dfirtrack_artifacts'] = True
        else:
            context['dfirtrack_artifacts'] = False

        # call logger
        case.logger(str(self.request.user), " CASE_DETAIL_ENTERED")
        return context


def set_case_times(case):
    """set case times according to config"""

    # get config
    main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')

    # get relevant casestatus out of config
    casestatus_start = main_config_model.casestatus_start.all()
    casestatus_end = main_config_model.casestatus_end.all()

    # set start time if new casestatus of system is in casestatus_start of main config (and has not been set before)
    if case.casestatus in casestatus_start and case.case_start_time == None:
        case.case_start_time = timezone.now()

    # set end time if new casestatus of system is in casestatus_end of main config (and has not been set before)
    if case.casestatus in casestatus_end and case.case_end_time == None:
        case.case_end_time = timezone.now()
        # also set start time if it has not already been done
        if case.case_start_time == None:
            case.case_start_time = timezone.now()

    return case


class CaseCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Case
    form_class = CaseForm
    template_name = 'dfirtrack_main/case/case_generic_form.html'

    def get(self, request, *args, **kwargs):
        # get id of first status objects sorted by name
        casepriority = Casepriority.objects.order_by('casepriority_name')[
            0
        ].casepriority_id
        casestatus = Casestatus.objects.order_by('casestatus_name')[0].casestatus_id

        form = self.form_class(
            initial={
                'casepriority': casepriority,
                'casestatus': casestatus,
            }
        )
        debug_logger(str(request.user), " CASE_ADD_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Add',
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.case_created_by_user_id = request.user
            case.case_modified_by_user_id = request.user
            # set case times according to config
            case = set_case_times(case)
            case.save()
            form.save_m2m()
            case.logger(str(request.user), " CASE_ADD_EXECUTED")
            messages.success(request, 'Case added')
            return redirect(reverse('case_detail', args=(case.case_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Add',
                },
            )


class CaseUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Case
    form_class = CaseForm
    template_name = 'dfirtrack_main/case/case_generic_form.html'

    def get(self, request, *args, **kwargs):
        case = self.get_object()
        form = self.form_class(instance=case)
        case.logger(str(request.user), " CASE_EDIT_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Edit',
            },
        )

    def post(self, request, *args, **kwargs):
        case = self.get_object()
        form = self.form_class(request.POST, instance=case)
        if form.is_valid():
            case = form.save(commit=False)
            case.case_modified_by_user_id = request.user
            # set case times according to config
            case = set_case_times(case)
            case.save()
            form.save_m2m()
            case.logger(str(request.user), " CASE_EDIT_EXECUTED")
            messages.success(request, 'Case edited')
            return redirect(reverse('case_detail', args=(case.case_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Edit',
                },
            )


class CaseSetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Case

    def get(self, request, *args, **kwargs):
        case = self.get_object()
        case.case_assigned_to_user_id = request.user
        case.save()
        case.logger(str(request.user), " CASE_SET_USER_EXECUTED")
        messages.success(request, 'Case assigned to you')

        # redirect
        return redirect(reverse('case_detail', args=(case.case_id,)))


class CaseUnsetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Case

    def get(self, request, *args, **kwargs):
        case = self.get_object()
        case.case_assigned_to_user_id = None
        case.save()
        case.logger(str(request.user), " CASE_UNSET_USER_EXECUTED")
        messages.warning(request, 'User assignment for case deleted')

        # redirect
        return redirect(reverse('case_detail', args=(case.case_id,)))
