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
        if user_config.filter_system_detail_show_artifact:
            user_config.filter_system_detail_show_artifact = False
        else:
            user_config.filter_system_detail_show_artifact = True

        # save config
        user_config.save()

        # get system for return redirect
        system = self.get_object()

        # redirect
        return redirect(reverse('system_detail', args=(system.system_id,)))
