from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from dfirtrack_artifacts import models as artifacts_models

class ArtifactstatusListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = artifacts_models.Artifactstatus
    template_name = 'dfirtrack_artifacts/artifactstatus/artifactstatus_list.html'
    context_object_name = 'artifactstatus_list'

class ArtifactstatusDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = artifacts_models.Artifactstatus
    template_name = 'dfirtrack_artifacts/artifactstatus/artifactstatus_detail.html'
