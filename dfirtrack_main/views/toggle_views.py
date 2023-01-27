from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import System


def toggle_user_config(user, key):
    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=user, filter_view='system_detail'
    )

    # toggle user config key
    user_config.toggle_user_config(key)


class ToggleSystemDetailArtifact(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_artifact')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#artifact'
        )


class ToggleSystemDetailArtifactClosed(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_artifact_closed')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#artifact'
        )


class ToggleSystemDetailTask(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_task')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(reverse('system_detail', args=(system.system_id,)) + '#task')


class ToggleSystemDetailTaskClosed(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_task_closed')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(reverse('system_detail', args=(system.system_id,)) + '#task')


class ToggleSystemDetailTechnicalInformation(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_technical_information')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,))
            + '#technical_information'
        )


class ToggleSystemDetailTimeline(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_timeline')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#timeline'
        )


class ToggleSystemDetailVirtualizationInformation(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_virtualization_information')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,))
            + '#virtualization_information'
        )


class ToggleSystemDetailCompanyInformation(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_company_information')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#company_information'
        )


class ToggleSystemDetailSystemuser(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_systemuser')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#systemuser'
        )


class ToggleSystemDetailAnalystmemo(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_analystmemo')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#analystmemo'
        )


class ToggleSystemDetailReportitem(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # toggle config
        toggle_user_config(request.user, 'show_reportitem')

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#reportitem'
        )
