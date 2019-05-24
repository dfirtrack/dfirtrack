from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from dfirtrack_artifacts import models as artifacts_models
from dfirtrack_main import models as main_models
from dfirtrack_artifacts import forms

class ArtifactListView(ListView):
    model = artifacts_models.Artifact

class ArtifactCreateView(CreateView):
    model = artifacts_models.Artifact
    form_class = forms.ArtifactForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Connect current django user to the request
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form) 

class ArtifactDetailView(DetailView):
    model = artifacts_models.Artifact

class ArtifactUpdateView(UpdateView):
    model = artifacts_models.Artifact
    form_class = forms.ArtifactForm