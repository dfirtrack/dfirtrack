from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from dfirtrack_artifacts.forms import ArtifactForm
from dfirtrack_artifacts.models import Artifact
from dfirtrack_main.logger.default_logger import debug_logger

class ArtifactListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_list.html'
    context_object_name = 'artifact_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), ' ARTIFACT_LIST_ENTERED')
        return Artifact.objects.order_by('artifact_id')

class ArtifactDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        systemtype = self.object
        systemtype.logger(str(self.request.user), " ARTIFACT_DETAIL_ENTERED")
        return context

class ArtifactCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_add.html'
    form_class = ArtifactForm

    def get(self, request, *args, **kwargs):
        if 'system' in request.GET:
            system = request.GET['system']
            form = self.form_class(
                initial={'system': system,}
            )
        else:
            form = self.form_class()
        debug_logger(str(request.user), ' ARTIFACT_ADD_ENTERED')
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artifact_created_by_user_id = self.request.user
        self.object.artifact_modified_by_user_id = self.request.user
        self.object.save()
        self.object.logger(str(self.request.user), ' ARTIFACT_ADD_EXECUTED')
        messages.success(self.request, 'Artifact added')

        # check for existing hashes
        self.object.check_existing_hashes(self.request)

        return super().form_valid(form) 

    def form_invalid(self, form):
        messages.error(self.request, 'Artifact could not be added')
        return super().form_invalid(form)

class ArtifactUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_edit.html'
    form_class = ArtifactForm

    def get(self, request, *args, **kwargs):
        artifact = self.get_object()
        form = self.form_class(instance = artifact)
        artifact.logger(str(request.user), ' ARTIFACT_EDIT_ENTERED')
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artifact_modified_by_user_id = self.request.user
        self.object.save()
        self.object.logger(str(self.request.user), ' ARTIFACT_EDIT_EXECUTED')
        messages.success(self.request, 'Artifact edited')

        # check for existing hashes
        self.object.check_existing_hashes(self.request)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Artifact could not be edited')
        return super().form_invalid(form)
