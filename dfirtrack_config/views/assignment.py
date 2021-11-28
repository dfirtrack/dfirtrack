from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from dfirtrack_artifacts.models import Artifact
from dfirtrack_config.filter_forms import AssignmentFilterForm
from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case, System, Tag, Task


class AssignmentView(LoginRequiredMixin, FormView):
    """assignment view to show current assignment"""

    login_url = '/login'
    template_name = 'dfirtrack_config/assignment/assignment.html'
    form_class = AssignmentFilterForm

    def get_context_data(self, *args, **kwargs):
        """actually shows the view"""

        """prologue"""

        # get context
        context = super().get_context_data(*args, **kwargs)

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user
        )

        """form preparation"""

        # initialize filter flag (needed for messages)
        filter_flag = False

        # even if the persistence option has been deselected, the initial values must correspond to the current filtering until the view is reloaded or left

        # create dict to initialize form values set by filtering in previous view call
        form_initial = {}

        # check box if persistence option was provided
        if user_config.filter_assignment_view_keep:
            # set initial value for form
            form_initial['filter_assignment_view_keep'] = True
        else:
            form_initial['filter_assignment_view_keep'] = False

        # get case from config and add to initial form value
        if user_config.filter_assignment_view_case:
            # get id
            case_id = user_config.filter_assignment_view_case.case_id
            # set initial value for form
            form_initial['case'] = case_id
            # set filter flag
            filter_flag = True

        # get tag from config and add to initial form value
        if user_config.filter_assignment_view_tag:
            # get id
            tag_id = user_config.filter_assignment_view_tag.tag_id
            # set initial value for form
            form_initial['tag'] = tag_id
            # set filter flag
            filter_flag = True

        # get user from config and add to initial form value
        if user_config.filter_assignment_view_user:
            # get id
            user_id = user_config.filter_assignment_view_user.id
            # set initial value for form
            form_initial['user'] = user_id

        # pre-select form according to previous filter selection
        context['form'] = self.form_class(initial=form_initial)

        """filter"""

        # get queryset with all entities
        artifact_queryset = Artifact.objects.all()
        case_queryset = Case.objects.all()
        system_queryset = System.objects.all()
        task_queryset = Task.objects.all()

        # filter queryset to case
        if user_config.filter_assignment_view_case:
            artifact_queryset = artifact_queryset.filter(
                case=user_config.filter_assignment_view_case
            )
            case_queryset = case_queryset.filter(
                case_id=user_config.filter_assignment_view_case.case_id
            )
            system_queryset = system_queryset.filter(
                case=user_config.filter_assignment_view_case
            )
            task_queryset = task_queryset.filter(
                case=user_config.filter_assignment_view_case
            )

        # filter queryset to tag
        if user_config.filter_assignment_view_tag:
            artifact_queryset = artifact_queryset.filter(
                tag=user_config.filter_assignment_view_tag
            )
            case_queryset = case_queryset.filter(
                tag=user_config.filter_assignment_view_tag
            )
            system_queryset = system_queryset.filter(
                tag=user_config.filter_assignment_view_tag
            )
            task_queryset = task_queryset.filter(
                tag=user_config.filter_assignment_view_tag
            )

        # filter queryset to user
        if user_config.filter_assignment_view_user:
            artifact_queryset = artifact_queryset.filter(
                artifact_assigned_to_user_id=user_config.filter_assignment_view_user
            )
            case_queryset = case_queryset.filter(
                case_assigned_to_user_id=user_config.filter_assignment_view_user
            )
            system_queryset = system_queryset.filter(
                system_assigned_to_user_id=user_config.filter_assignment_view_user
            )
            task_queryset = task_queryset.filter(
                task_assigned_to_user_id=user_config.filter_assignment_view_user
            )
            # add username to context used for template
            context[
                'assignment_user'
            ] = user_config.filter_assignment_view_user.username
        # show unassigned entities otherwise
        else:
            artifact_queryset = artifact_queryset.filter(
                artifact_assigned_to_user_id=None
            )
            case_queryset = case_queryset.filter(case_assigned_to_user_id=None)
            system_queryset = system_queryset.filter(system_assigned_to_user_id=None)
            task_queryset = task_queryset.filter(task_assigned_to_user_id=None)
            # add username to context used for template
            context['assignment_user'] = None

        # add querysets to context
        context['artifact'] = artifact_queryset
        context['case'] = case_queryset
        context['system'] = system_queryset
        context['task'] = task_queryset

        """filter cleaning"""

        # clean filtering after providing filter results if persistence option was not selected
        if not user_config.filter_assignment_view_keep:
            # unset filter case
            user_config.filter_assignment_view_case = None
            # unset filter tag
            user_config.filter_assignment_view_tag = None
            # unset filter user
            user_config.filter_assignment_view_user = None
            # save config
            user_config.save()

        """visibility"""

        if user_config.filter_assignment_view_show_artifact:
            context['show_artifact'] = True
        if user_config.filter_assignment_view_show_case:
            context['show_case'] = True
        if user_config.filter_assignment_view_show_note:
            context['show_note'] = True
        if user_config.filter_assignment_view_show_reportitem:
            context['show_reportitem'] = True
        if user_config.filter_assignment_view_show_system:
            context['show_system'] = True
        if user_config.filter_assignment_view_show_tag:
            context['show_tag'] = True
        if user_config.filter_assignment_view_show_task:
            context['show_task'] = True

        """epilogue"""

        # call logger
        debug_logger(str(self.request.user), ' ASSIGNMENT_ENTERED')

        # info message that filter is active (not for user filtering)
        if filter_flag:
            messages.info(
                self.request, 'Filter is active. Entities might be incomplete.'
            )

        # return context dictionary
        return context

    def form_valid(self, form):
        """save form data to config and call view again"""

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user
        )

        # save filter choices from form in 'assignment_view' to database and call 'assignment_view' again with the new filter options

        # get case from form and save to config
        if form.data['case']:
            assignment_view_case = Case.objects.get(case_id=form.data['case'])
            user_config.filter_assignment_view_case = assignment_view_case
        else:
            user_config.filter_assignment_view_case = None

        # get tag from form and save to config
        if form.data['tag']:
            assignment_view_tag = Tag.objects.get(tag_id=form.data['tag'])
            user_config.filter_assignment_view_tag = assignment_view_tag
        else:
            user_config.filter_assignment_view_tag = None

        # get user from form and save to config
        if form.data['user']:
            assignment_view_user = User.objects.get(id=form.data['user'])
            user_config.filter_assignment_view_user = assignment_view_user
        else:
            user_config.filter_assignment_view_user = None

        # avoid MultiValueDictKeyError by providing default False if checkbox was empty
        if form.data.get('filter_assignment_view_keep', False):
            user_config.filter_assignment_view_keep = True
        else:
            user_config.filter_assignment_view_keep = False

        # save config
        user_config.save()

        # call view again
        return redirect(reverse('assignment'))


@login_required(login_url="/login")
def clear_assignment_view_filter(request):
    """clear assignment view filter"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # clear values
    user_config.filter_assignment_view_case = None
    user_config.filter_assignment_view_tag = None
    user_config.filter_assignment_view_user = None

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_artifact(request):
    """toggle visibility"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # toggle value
    if user_config.filter_assignment_view_show_artifact:
        user_config.filter_assignment_view_show_artifact = False
    else:
        user_config.filter_assignment_view_show_artifact = True

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_case(request):
    """toggle visibility"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # toggle value
    if user_config.filter_assignment_view_show_case:
        user_config.filter_assignment_view_show_case = False
    else:
        user_config.filter_assignment_view_show_case = True

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_note(request):
    """toggle visibility"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # toggle value
    if user_config.filter_assignment_view_show_note:
        user_config.filter_assignment_view_show_note = False
    else:
        user_config.filter_assignment_view_show_note = True

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_reportitem(request):
    """toggle visibility"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # toggle value
    if user_config.filter_assignment_view_show_reportitem:
        user_config.filter_assignment_view_show_reportitem = False
    else:
        user_config.filter_assignment_view_show_reportitem = True

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_system(request):
    """toggle visibility"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # toggle value
    if user_config.filter_assignment_view_show_system:
        user_config.filter_assignment_view_show_system = False
    else:
        user_config.filter_assignment_view_show_system = True

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_tag(request):
    """toggle visibility"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # toggle value
    if user_config.filter_assignment_view_show_tag:
        user_config.filter_assignment_view_show_tag = False
    else:
        user_config.filter_assignment_view_show_tag = True

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_task(request):
    """toggle visibility"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # toggle value
    if user_config.filter_assignment_view_show_task:
        user_config.filter_assignment_view_show_task = False
    else:
        user_config.filter_assignment_view_show_task = True

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))
