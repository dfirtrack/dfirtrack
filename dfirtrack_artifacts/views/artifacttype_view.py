from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from dfirtrack_artifacts import models as artifacts_models
from dfirtrack_artifacts import forms

class ArtifacttypeListView(ListView):
    model = artifacts_models.Artifacttype
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_list.html'

class ArtifacttypeCreateView(CreateView):
    model = artifacts_models.Artifacttype
    form_class = forms.ArtifacttypeForm
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_add.html'

class ArtifacttypeDetailView(DetailView):
    model = artifacts_models.Artifacttype
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_detail.html'

class ArtifacttypeUpdateView(UpdateView):
    model = artifacts_models.Artifacttype
    form_class = forms.ArtifacttypeForm
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_edit.html'