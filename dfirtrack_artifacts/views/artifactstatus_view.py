from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from dfirtrack_artifacts import models as artifacts_models
from dfirtrack_artifacts import forms

class ArtifactstatusListView(LoginRequiredMixin, ListView):
    model = artifacts_models.Artifactstatus
    template_name = 'dfirtrack_artifacts/artifactstatus/artifactstatus_list.html'


class ArtifactstatusCreateView(LoginRequiredMixin, CreateView):
    model = artifacts_models.Artifactstatus
    form_class = forms.ArtifactstatusForm
    template_name = 'dfirtrack_artifacts/artifactstatus/artifactstatus_add.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Connect current django user to the request
        self.object.created_by = self.request.user
        self.object.save()
        messages.success(self.request, 'Artifactstatus added')
        return super().form_valid(form) 

class ArtifactstatusDetailView(LoginRequiredMixin, DetailView):
    model = artifacts_models.Artifactstatus
    template_name = 'dfirtrack_artifacts/artifactstatus/artifactstatus_detail.html'

class ArtifactstatusUpdateView(LoginRequiredMixin, UpdateView):
    model = artifacts_models.Artifactstatus
    form_class = forms.ArtifactstatusForm
    template_name = 'dfirtrack_artifacts/artifactstatus/artifactstatus_edit.html'