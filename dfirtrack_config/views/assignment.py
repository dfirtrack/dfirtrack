from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.filter_forms import GeneralFilterForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case, Note, Reportitem, System, Tag, Task


class AssignmentView(LoginRequiredMixin, FormView):
    """assignment view to show current assignment"""

    login_url = '/login'
    template_name = 'dfirtrack_config/assignment/assignment.html'
    form_class = GeneralFilterForm
    filter_view = 'assignment'

    def get_context_data(self, *args, **kwargs):
        """actually shows the view"""

        """prologue"""

        # get context
        context = super().get_context_data(*args, **kwargs)

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user,
            filter_view=self.filter_view
        )

        """form preparation"""

        # filter: pre-select form according to previous filter selection
        context['form'] = self.form_class(instance=user_config)

        filter_kwargs = dict()

        # get case from config and add to initial form value
        if user_config.filter_list_case:
            # queryset kwargs
            filter_kwargs['case'] = user_config.filter_list_case

        # get tag from config and add to initial form value
        if user_config.filter_list_tag.count() > 0:
            # queryset kwargs
            filter_kwargs['tag__in'] = user_config.filter_list_tag.all()

        """
        filter
        even if system filtering takes place in
        'dfirtrack_main.views.json_provider_views.get_systems_json'
        it is currently required for the template 'assignment.html'
        """

        # get queryset with all entities
        case = filter_kwargs.pop('case', None)
        if case:
            case_queryset = Case.objects.all().filter(**filter_kwargs).filter(case_id=case.case_id)
            filter_kwargs['case'] = case
        else:
            case_queryset = Case.objects.all().filter(**filter_kwargs)
        note_queryset = Note.objects.all().filter(**filter_kwargs)
        reportitem_queryset = Reportitem.objects.all().filter(**filter_kwargs)
        system_queryset = System.objects.all().filter(**filter_kwargs)
        task_queryset = Task.objects.all().filter(**filter_kwargs)
        tags = filter_kwargs.pop('tag__in', Tag.objects.all())
        tag_queryset = Tag.objects.all().filter(**filter_kwargs).filter(tag_id__in=tags)

        # filter queryset to user
        if user_config.filter_list_assigned_to_user_id:
            case_queryset = case_queryset.filter(
                case_assigned_to_user_id=user_config.filter_list_assigned_to_user_id
            )
            note_queryset = note_queryset.filter(
                note_assigned_to_user_id=user_config.filter_list_assigned_to_user_id
            )
            reportitem_queryset = reportitem_queryset.filter(
                reportitem_assigned_to_user_id=user_config.filter_list_assigned_to_user_id
            )
            system_queryset = system_queryset.filter(
                system_assigned_to_user_id=user_config.filter_list_assigned_to_user_id
            )
            tag_queryset = tag_queryset.filter(
                tag_assigned_to_user_id=user_config.filter_list_assigned_to_user_id
            )
            task_queryset = task_queryset.filter(
                task_assigned_to_user_id=user_config.filter_list_assigned_to_user_id
            )
            # add username to context used for template
            context[
                'assignment_user'
            ] = user_config.filter_list_assigned_to_user_id
        # show unassigned entities otherwise
        else:
            case_queryset = case_queryset.filter(case_assigned_to_user_id=None)
            note_queryset = note_queryset.filter(note_assigned_to_user_id=None)
            reportitem_queryset = reportitem_queryset.filter(
                reportitem_assigned_to_user_id=None
            )
            system_queryset = system_queryset.filter(system_assigned_to_user_id=None)
            tag_queryset = tag_queryset.filter(tag_assigned_to_user_id=None)
            task_queryset = task_queryset.filter(task_assigned_to_user_id=None)
            # add username to context used for template
            context['assignment_user'] = None

        # add querysets to context
        context['case'] = case_queryset
        context['note'] = note_queryset
        context['reportitem'] = reportitem_queryset
        context['system'] = system_queryset
        context['tag'] = tag_queryset
        context['task'] = task_queryset

        """visibility"""

        if user_config.filter_view_show:
            context.update(user_config.filter_view_show)
        else:
            user_config.filter_view_show = {
                'show_artifact': True,
                'show_case': True,
                'show_note': True,
                'show_reportitem': True,
                'show_system': True,
                'show_tag': True,
                'show_task': True,
            }
            user_config.save()

        """epilogue"""

        # call logger
        debug_logger(str(self.request.user), ' ASSIGNMENT_ENTERED')

        # info message that filter is active (not for user filtering)
        if user_config.is_filter_active():
            messages.info(
                self.request, 'Filter is active. Entities might be incomplete.'
            )

        # return context dictionary
        return context

    def post(self, request, *args, **kwargs):
        """save form data to config and call view again"""
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user,
            filter_view=self.filter_view
        )

        form = self.form_class(request.POST, instance=user_config)

        if form.is_valid():
            user_config = form.save(commit=False)
            user_config.save()
            form.save_m2m()

        # call view again
        return redirect(reverse('assignment'))

def toggle_user_config(user, key):
    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=user,
            filter_view='assignment'
        )
    
    # toggle user config key
    user_config.toggle_user_config(key)

@login_required(login_url="/login")
def clear_assignment_view_filter(request):
    """clear assignment view filter"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user,
        filter_view='assignment'
    )

    # clear values
    user_config.filter_list_case = None
    user_config.filter_list_tag.clear()
    user_config.filter_list_assigned_to_user_id = None

    # save config
    user_config.save()

    # return to assignment view
    return redirect(reverse('assignment'))


@login_required(login_url="/login")
def toggle_assignment_view_artifact(request):
    """toggle visibility"""

    # toggle value
    toggle_user_config(request.user, 'show_artifact')

    # return to assignment view
    return redirect(reverse('assignment') + '#artifact')


@login_required(login_url="/login")
def toggle_assignment_view_case(request):
    """toggle visibility"""

    # toggle value
    toggle_user_config(request.user, 'show_case')

    # return to assignment view
    return redirect(reverse('assignment') + '#case')


@login_required(login_url="/login")
def toggle_assignment_view_note(request):
    """toggle visibility"""

    # toggle value
    toggle_user_config(request.user, 'show_note')

    # return to assignment view
    return redirect(reverse('assignment') + '#note')


@login_required(login_url="/login")
def toggle_assignment_view_reportitem(request):
    """toggle visibility"""

    # toggle value
    toggle_user_config(request.user, 'show_reportitem')

    # return to assignment view
    return redirect(reverse('assignment') + '#reportitem')


@login_required(login_url="/login")
def toggle_assignment_view_system(request):
    """toggle visibility"""

    # toggle value
    toggle_user_config(request.user, 'show_system')

    # return to assignment view
    return redirect(reverse('assignment') + '#system')


@login_required(login_url="/login")
def toggle_assignment_view_tag(request):
    """toggle visibility"""

    # toggle value
    toggle_user_config(request.user, 'show_tag')

    # return to assignment view
    return redirect(reverse('assignment') + '#tag')


@login_required(login_url="/login")
def toggle_assignment_view_task(request):
    """toggle visibility"""

    # toggle value
    toggle_user_config(request.user, 'show_task')

    # return to assignment view
    return redirect(reverse('assignment') + '#task')
