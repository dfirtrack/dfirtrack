from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from dfirtrack_artifacts.models import Artifact, Artifactstatus
from dfirtrack_main.models import Analysisstatus, System, Systemstatus, Task, Taskstatus, Taskpriority
from dfirtrack_main.logger.default_logger import debug_logger


class AboutView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = 'dfirtrack_main/about.html'

    def get(self, request, *args, **kwargs):
        debug_logger(str(request.user), ' ABOUT_ENTERED')
        return render(request, self.template_name)

class FaqView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = 'dfirtrack_main/faq.html'

    def get(self, request, *args, **kwargs):
        debug_logger(str(request.user), ' FAQ_ENTERED')
        return render(request, self.template_name)

class StatusView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = 'dfirtrack_main/status.html'

    def get_context_data(self, *args, **kwargs):

        context = super(StatusView, self).get_context_data(*args, **kwargs)

        # get numbers
        context['artifacts_number'] = Artifact.objects.all().count()
        context['systems_number'] = System.objects.all().count()
        context['tasks_number'] = Task.objects.all().count()

        # get objects
        context['analysisstatus_all'] = Analysisstatus.objects.all().order_by('analysisstatus_id')
        context['artifactstatus_all'] = Artifactstatus.objects.all().order_by('artifactstatus_name')
        context['systemstatus_all'] = Systemstatus.objects.all().order_by('systemstatus_id')
        context['taskstatus_all'] = Taskstatus.objects.all().order_by('taskstatus_id')
        context['taskpriority_all'] = Taskpriority.objects.all().order_by('taskpriority_id')

        # TODO: request missing
        # call logger
        #debug_logger(str(request.user), ' STATUS_ENTERED')

        # return context dictionary
        return context
