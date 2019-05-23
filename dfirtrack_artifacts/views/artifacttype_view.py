from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from dfirtrack_artifacts import models as artifacts_models
#TODO: Forms mus be created
#from dfirtrack_artifacts.forms import ArtifacttypeForm

class ArtifacttypeListView(ListView):
    model = artifacts_models.Artifacttype


class ArtifacttypeCreateView(CreateView):
    model = artifacts_models.Artifacttype
    form_class = ArtifacttypeForm

class ArtifacttypeDetailView(DetailView):
    model = artifacts_models.Artifacttype


class ArtifacttypeUpdateView(UpdateView):
    model = artifacts_models.Artifacttype
    form_class = ArtifacttypeFormP