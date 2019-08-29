from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from dfirtrack_artifacts import models as artifacts_models
from dfirtrack_main import models as main_models
from dfirtrack_artifacts import forms

class ArtifactListView(LoginRequiredMixin, ListView):
    model = artifacts_models.Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_list.html'
    context_object_name = 'artifact_list'

class ArtifactCreateView(LoginRequiredMixin, CreateView):
    model = artifacts_models.Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_add.html'
    form_class = forms.ArtifactForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artifact_created_by_user_id = self.request.user
        self.object.artifact_modified_by_user_id = self.request.user
        self.object.save()
        self.object.logger(str(self.request.user), "ARTIFACT_ADD_EXECUTED")
        messages.success(self.request, 'Artifact added')
        return super().form_valid(form) 

    def form_invalid(self, form):
        self.object.created_by = self.request.user
        messages.error(self.request, 'Artifact could not be added')
        return super().form_invalid(form)


class ArtifactDetailView(LoginRequiredMixin, DetailView):
    model = artifacts_models.Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_detail.html'

class ArtifactUpdateView(LoginRequiredMixin, UpdateView):
    model = artifacts_models.Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_edit.html'
    form_class = forms.ArtifactForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artifact_modified_by_user_id = self.request.user
        self.object.save()
        self.object.logger(str(self.request.user), "ARTIFACT_EDIT_EXECUTED")
        messages.success(self.request, 'Artifact edited')
        return super().form_valid(form)
