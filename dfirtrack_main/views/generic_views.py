from datetime import datetime, timedelta, time
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

        # prepare dates
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        yesterday = today - timedelta(1)
        two_days_ago = today - timedelta(2)
        three_days_ago = today - timedelta(3)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        yesterday_start = datetime.combine(yesterday, time())
        two_days_ago_start = datetime.combine(two_days_ago, time())
        three_days_ago_start = datetime.combine(three_days_ago, time())

        # get numbers
        context['artifacts_number'] = Artifact.objects.all().count()
        context['systems_number'] = System.objects.all().count()
        context['tasks_number'] = Task.objects.all().count()

        # get numbers according to date
        context['artifacts_today_number'] = Artifact.objects.filter(artifact_create_time__lt=today_end, artifact_create_time__gte=today_start).count()
        context['artifacts_yesterday_number'] = Artifact.objects.filter(artifact_create_time__lt=today_start, artifact_create_time__gte=yesterday_start).count()
        context['artifacts_two_days_ago_number'] = Artifact.objects.filter(artifact_create_time__lt=yesterday_start, artifact_create_time__gte=two_days_ago_start).count()
        context['artifacts_three_days_ago_number'] = Artifact.objects.filter(artifact_create_time__lt=two_days_ago_start, artifact_create_time__gte=three_days_ago_start).count()
        context['systems_today_number'] = System.objects.filter(system_create_time__lt=today_end, system_create_time__gte=today_start).count()
        context['systems_yesterday_number'] = System.objects.filter(system_create_time__lt=today_start, system_create_time__gte=yesterday_start).count()
        context['systems_two_days_ago_number'] = System.objects.filter(system_create_time__lt=yesterday_start, system_create_time__gte=two_days_ago_start).count()
        context['systems_three_days_ago_number'] = System.objects.filter(system_create_time__lt=two_days_ago_start, system_create_time__gte=three_days_ago_start).count()
        context['tasks_today_number'] = Task.objects.filter(task_create_time__lt=today_end, task_create_time__gte=today_start).count()
        context['tasks_yesterday_number'] = Task.objects.filter(task_create_time__lt=today_start, task_create_time__gte=yesterday_start).count()
        context['tasks_two_days_ago_number'] = Task.objects.filter(task_create_time__lt=yesterday_start, task_create_time__gte=two_days_ago_start).count()
        context['tasks_three_days_ago_number'] = Task.objects.filter(task_create_time__lt=two_days_ago_start, task_create_time__gte=three_days_ago_start).count()

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
