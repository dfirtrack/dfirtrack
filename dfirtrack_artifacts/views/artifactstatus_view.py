from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from dfirtrack_artifacts import models as artifacts_models
from dfirtrack_artifacts import forms

class ArtifactstatusListView(ListView):
    model = artifacts_models.Artifactstatus


class ArtifactstatusCreateView(CreateView):
    model = artifacts_models.Artifactstatus
    form_class = forms.ArtifactstatusForm

class ArtifactstatusDetailView(DetailView):
    model = artifacts_models.Artifactstatus

class ArtifactstatusUpdateView(UpdateView):
    model = artifacts_models.Artifactstatus
    form_class = forms.ArtifactstatusForm