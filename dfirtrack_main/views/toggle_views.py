from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import System


class ToggleSystemDetailArtifact(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_artifact = (
            not user_config.filter_system_detail_show_artifact
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_artifact_closed = (
            not user_config.filter_system_detail_show_artifact_closed
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_task = (
            not user_config.filter_system_detail_show_task
        )

        # save config
        user_config.save()

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(reverse('system_detail', args=(system.system_id,)) + '#task')


class ToggleSystemDetailTaskClosed(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_task_closed = (
            not user_config.filter_system_detail_show_task_closed
        )

        # save config
        user_config.save()

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(reverse('system_detail', args=(system.system_id,)) + '#task')


class ToggleSystemDetailTechnicalInformation(LoginRequiredMixin, DetailView):
    """toggle visibility"""

    login_url = '/login'
    model = System

    def get(self, request, *args, **kwargs):

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_technical_information = (
            not user_config.filter_system_detail_show_technical_information
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_timeline = (
            not user_config.filter_system_detail_show_timeline
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_virtualization_information = (
            not user_config.filter_system_detail_show_virtualization_information
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_company_information = (
            not user_config.filter_system_detail_show_company_information
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_systemuser = (
            not user_config.filter_system_detail_show_systemuser
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_analystmemo = (
            not user_config.filter_system_detail_show_analystmemo
        )

        # save config
        user_config.save()

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

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user
        )

        # toggle value
        user_config.filter_system_detail_show_reportitem = (
            not user_config.filter_system_detail_show_reportitem
        )

        # save config
        user_config.save()

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(
            reverse('system_detail', args=(system.system_id,)) + '#reportitem'
        )
