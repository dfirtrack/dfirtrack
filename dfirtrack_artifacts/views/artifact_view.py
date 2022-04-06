from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse, resolve
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView

from dfirtrack_artifacts.forms import ArtifactForm
from dfirtrack_artifacts.models import Artifact, Artifactpriority, Artifactstatus
from dfirtrack_config.models import MainConfigModel, UserConfigModel
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.filter_forms import GeneralFilterForm


class ArtifactListView(LoginRequiredMixin, FormView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_list.html'
    context_object_name = 'artifact_list'
    form_class = GeneralFilterForm
    filter_view = 'artifact_list'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user,
            filter_view=self.filter_view
        )

        # filter: pre-select form according to previous filter selection
        context['form'] = self.form_class(instance=user_config)

        # get current artifact view
        current_url = resolve(self.request.path_info).url_name
        if current_url == 'artifacts_artifact_list':
            # call logger
            debug_logger(str(self.request.user), ' ARTIFACT_OPEN_ENTERED')
            context['artifact_site'] = 'open'
        elif current_url == 'artifacts_artifact_closed':
            # call logger
            debug_logger(str(self.request.user), ' ARTIFACT_CLOSED_ENTERED')
            context['artifact_site'] = 'closed'
        else:
            # call logger
            debug_logger(str(self.request.user), ' ARTIFACT_ALL_ENTERED')
            context['artifact_site'] = 'all'
        return context
    
    def post(self, request, *args, **kwargs):
        """save form data to config and call view again"""
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.user,
            filter_view=self.filter_view
        )

        form = self.form_class(request.POST, instance=user_config)

        if form.is_valid():
            user_config = form.save(commit=False)
            user_config.save()
            form.save_m2m()

        # call view again
        return redirect(reverse('artifact_list'))

class ArtifactDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        systemtype = self.object
        systemtype.logger(str(self.request.user), ' ARTIFACT_DETAIL_ENTERED')
        return context


class ArtifactCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_generic_form.html'
    form_class = ArtifactForm

    def get(self, request, *args, **kwargs):

        # get id of first status objects sorted by name
        artifactpriority = Artifactpriority.objects.order_by('artifactpriority_name')[
            0
        ].artifactpriority_id
        artifactstatus = Artifactstatus.objects.order_by('artifactstatus_name')[
            0
        ].artifactstatus_id

        if 'system' in request.GET:
            system = request.GET['system']
            form = self.form_class(
                initial={
                    'system': system,
                    'artifactpriority': artifactpriority,
                    'artifactstatus': artifactstatus,
                }
            )
        else:
            form = self.form_class(
                initial={
                    'artifactpriority': artifactpriority,
                    'artifactstatus': artifactstatus,
                }
            )
        debug_logger(str(request.user), ' ARTIFACT_ADD_ENTERED')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Add',
            },
        )

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


class ArtifactUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Artifact
    template_name = 'dfirtrack_artifacts/artifact/artifact_generic_form.html'
    form_class = ArtifactForm

    def get(self, request, *args, **kwargs):
        artifact = self.get_object()
        form = self.form_class(instance=artifact)
        artifact.logger(str(request.user), ' ARTIFACT_EDIT_ENTERED')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Edit',
            },
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artifact_modified_by_user_id = self.request.user
        self.object.save()
        self.object.logger(str(self.request.user), ' ARTIFACT_EDIT_EXECUTED')
        messages.success(self.request, 'Artifact edited')

        # check for existing hashes
        self.object.check_existing_hashes(self.request)

        return super().form_valid(form)


class ArtifactSetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Artifact

    def get(self, request, *args, **kwargs):
        artifact = self.get_object()
        artifact.artifact_assigned_to_user_id = request.user
        artifact.save()
        artifact.logger(str(request.user), " ARTIFACT_SET_USER_EXECUTED")
        messages.success(request, 'Artifact assigned to you')

        # redirect
        return redirect(
            reverse('artifacts_artifact_detail', args=(artifact.artifact_id,))
        )


class ArtifactUnsetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Artifact

    def get(self, request, *args, **kwargs):
        artifact = self.get_object()
        artifact.artifact_assigned_to_user_id = None
        artifact.save()
        artifact.logger(str(request.user), " ARTIFACT_UNSET_USER_EXECUTED")
        messages.warning(request, 'User assignment for artifact deleted')

        # redirect
        return redirect(
            reverse('artifacts_artifact_detail', args=(artifact.artifact_id,))
        )

@login_required(login_url="/login")
def clear_artifact_list_filter(request):
    """clear system list filter"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user,
        filter_view='artifact_list'
    )

    # clear values
    user_config.filter_list_case = None
    user_config.filter_list_assigned_to_user_id = None
    user_config.filter_list_tag.clear()

    # save config
    user_config.save()

    return redirect(reverse('artifacts_artifact_list'))