from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from dfirtrack_artifacts.models import Artifact
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case, System, Task


class AssignmentView(LoginRequiredMixin, TemplateView):
    """assignment view to show current assignment"""

    login_url = '/login'
    template_name = 'dfirtrack_config/assignment/assignment.html'

    def get_context_data(self, *args, **kwargs):

        user = self.request.user

        # get context
        context = super().get_context_data(*args, **kwargs)

        # get artifacts
        context['artifact'] = Artifact.objects.filter(artifact_assigned_to_user_id=user)
        # get cases
        context['case'] = Case.objects.filter(case_assigned_to_user_id=user)
        # get systems
        context['system'] = System.objects.filter(system_assigned_to_user_id=user)
        # get tasks
        context['task'] = Task.objects.filter(task_assigned_to_user_id=user)

        # call logger
        debug_logger(str(self.request.user), ' ASSIGNMENT_ENTERED')

        # return context dictionary
        return context
