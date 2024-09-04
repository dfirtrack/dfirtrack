import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import FormView
from djangoql.queryset import apply_search
from djangoql.schema import DjangoQLSchema
from djangoql.serializers import DjangoQLSchemaSerializer

from dfirtrack_artifacts.models import Artifact
from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.filter_forms import GeneralFilterForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case, Note, Reportitem, System, Tag, Task


class AssignmentQLSchema(DjangoQLSchema):
    include = (User,)

    # fields for autocomplete suggestions
    suggest_options = {
        User: ['username'],
    }

    # return fields for foreign objects
    def get_fields(self, model):
        return ['id', 'username']


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
            user_config_username=self.request.user, filter_view=self.filter_view
        )

        """form preparation"""

        # filter: pre-select form according to previous filter selection
        context['form'] = self.form_class(instance=user_config)

        filter_kwargs = dict()

        introspections = DjangoQLSchemaSerializer().serialize(
            AssignmentQLSchema(User.objects.model)
        )

        context['introspections'] = json.dumps(introspections)

        """
        filter
        even if system filtering takes place in
        'dfirtrack_main.views.json_provider_views.get_systems_json'
        it is currently required for the template 'assignment.html'
        """

        # filter user
        user_queryset = User.objects.all()
        if user_config.filter_query != "":
            user_queryset = apply_search(
                User.objects.all(), user_config.filter_query, schema=AssignmentQLSchema
            )

            # get queryset with all entities
            case_queryset = Case.objects.filter(
                case_assigned_to_user_id__in=user_queryset
            )
            note_queryset = Note.objects.filter(
                note_assigned_to_user_id__in=user_queryset
            )
            reportitem_queryset = Reportitem.objects.filter(
                reportitem_assigned_to_user_id__in=user_queryset
            )
            task_queryset = Task.objects.filter(
                task_assigned_to_user_id__in=user_queryset
            )
            tag_queryset = Tag.objects.filter(tag_assigned_to_user_id__in=user_queryset)

            artifact_count = Artifact.objects.filter(
                artifact_assigned_to_user_id__in=user_queryset
            ).count()
            system_count = System.objects.filter(
                system_assigned_to_user_id__in=user_queryset
            ).count()
        else:
            # get queryset with all entities
            case_queryset = Case.objects.exclude(
                case_assigned_to_user_id__in=user_queryset
            )
            note_queryset = Note.objects.exclude(
                note_assigned_to_user_id__in=user_queryset
            )
            reportitem_queryset = Reportitem.objects.exclude(
                reportitem_assigned_to_user_id__in=user_queryset
            )
            task_queryset = Task.objects.exclude(
                task_assigned_to_user_id__in=user_queryset
            )
            tag_queryset = Tag.objects.exclude(
                tag_assigned_to_user_id__in=user_queryset
            )

            artifact_count = Artifact.objects.exclude(
                artifact_assigned_to_user_id__in=user_queryset
            ).count()
            system_count = System.objects.exclude(
                system_assigned_to_user_id__in=user_queryset
            ).count()

        if user_config.filter_query != "":
            context['assignment_user'] = user_queryset

        # add querysets to context
        context['case'] = case_queryset
        context['note'] = note_queryset
        context['reportitem'] = reportitem_queryset
        context['tag'] = tag_queryset
        context['task'] = task_queryset

        context['system_number'] = system_count
        context['artifact_number'] = artifact_count

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
            user_config_username=request.user, filter_view=self.filter_view
        )

        form = self.form_class(request.POST, instance=user_config)

        if form.is_valid():
            user_config = form.save(commit=False)
            user_config.save()
            form.save_m2m()

            # call view again
            return redirect(reverse('assignment'))
        else:
            return render(request, self.template_name, {'form': form})


def toggle_user_config(user, key):
    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=user, filter_view='assignment'
    )

    # toggle user config key
    user_config.toggle_user_config(key)


@login_required(login_url="/login")
def clear_assignment_view_filter(request):
    """clear assignment view filter"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user, filter_view='assignment'
    )

    # clear values
    user_config.filter_query = ""

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
