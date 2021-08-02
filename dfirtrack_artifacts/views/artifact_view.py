from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from dfirtrack_artifacts.forms import ArtifactForm
from dfirtrack_artifacts.models import Artifact, Artifactpriority, Artifactstatus
from dfirtrack_config.models import MainConfigModel
from dfirtrack_main.logger.default_logger import debug_logger


def query_artifact(artifactstatus_list):
    """query artifacts with a list of specific artifactstatus"""

    # create empty artifact queryset
    artifacts_merged = Artifact.objects.none()

    # iterate over artifactstatus objects
    for artifactstatus in artifactstatus_list:

        # get artifacts with specific artifactstatus
        artifacts = Artifact.objects.filter(artifactstatus=artifactstatus)

        # add artifacts from above query to merge queryset
        artifacts_merged = artifacts | artifacts_merged

    # sort artifacts by id
    artifacts_sorted = artifacts_merged.order_by("artifact_id")

    # return sorted artifacts with specific artifactstatus
    return artifacts_sorted


class ArtifactListView(LoginRequiredMixin, ListView):
    login_url = "/login"
    model = Artifact
    template_name = "dfirtrack_artifacts/artifact/artifact_list.html"
    context_object_name = "artifact_list"

    def get_queryset(self):

        # call logger
        debug_logger(str(self.request.user), " ARTIFACT_LIST_ENTERED")
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name="MainConfig")

        """ get all artifacts with artifactstatus to be considered open """

        # get 'open' artifactstatus from config
        artifactstatus_open = main_config_model.artifactstatus_open.all()
        # guery artifacts according to subset of artifactstatus open
        artifacts = query_artifact(artifactstatus_open)

        # return artifacts according to query
        return artifacts


class ArtifactClosedView(LoginRequiredMixin, ListView):
    login_url = "/login"
    model = Artifact
    template_name = "dfirtrack_artifacts/artifact/artifact_closed.html"
    context_object_name = "artifact_list"

    def get_queryset(self):

        # call logger
        debug_logger(str(self.request.user), " ARTIFACT_CLOSED_ENTERED")
        # get config
        main_config_model = MainConfigModel.objects.get(main_config_name="MainConfig")

        """ get all artifacts with artifactstatus to be considered closed """

        # get all artifactstatus from database
        artifactstatus_all = Artifactstatus.objects.all()
        # get 'open' artifactstatus from config
        artifactstatus_open = main_config_model.artifactstatus_open.all()
        # get diff between all artifactstatus and open artifactstatus
        artifactstatus_closed = artifactstatus_all.difference(artifactstatus_open)

        # guery artifacts according to subset of artifactstatus closed
        artifacts = query_artifact(artifactstatus_closed)
        # return artifacts according to query
        return artifacts


class ArtifactAllView(LoginRequiredMixin, ListView):
    login_url = "/login"
    model = Artifact
    template_name = "dfirtrack_artifacts/artifact/artifact_all.html"
    context_object_name = "artifact_list"

    def get_queryset(self):
        # call logger
        debug_logger(str(self.request.user), " ARTIFACT_ALL_ENTERED")
        return Artifact.objects.order_by("artifact_id")


class ArtifactDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login"
    model = Artifact
    template_name = "dfirtrack_artifacts/artifact/artifact_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        systemtype = self.object
        systemtype.logger(str(self.request.user), " ARTIFACT_DETAIL_ENTERED")
        return context


class ArtifactCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login"
    model = Artifact
    template_name = "dfirtrack_artifacts/artifact/artifact_generic_form.html"
    form_class = ArtifactForm

    def get(self, request, *args, **kwargs):

        # get id of first status objects sorted by name
        artifactpriority = Artifactpriority.objects.order_by("artifactpriority_name")[
            0
        ].artifactpriority_id
        artifactstatus = Artifactstatus.objects.order_by("artifactstatus_name")[
            0
        ].artifactstatus_id

        if "system" in request.GET:
            system = request.GET["system"]
            form = self.form_class(
                initial={
                    "system": system,
                    "artifactpriority": artifactpriority,
                    "artifactstatus": artifactstatus,
                }
            )
        else:
            form = self.form_class(
                initial={
                    "artifactpriority": artifactpriority,
                    "artifactstatus": artifactstatus,
                }
            )
        debug_logger(str(request.user), " ARTIFACT_ADD_ENTERED")
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Add",
            },
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artifact_created_by_user_id = self.request.user
        self.object.artifact_modified_by_user_id = self.request.user
        self.object.save()
        self.object.logger(str(self.request.user), " ARTIFACT_ADD_EXECUTED")
        messages.success(self.request, "Artifact added")

        # check for existing hashes
        self.object.check_existing_hashes(self.request)

        return super().form_valid(form)


class ArtifactUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login"
    model = Artifact
    template_name = "dfirtrack_artifacts/artifact/artifact_generic_form.html"
    form_class = ArtifactForm

    def get(self, request, *args, **kwargs):
        artifact = self.get_object()
        form = self.form_class(instance=artifact)
        artifact.logger(str(request.user), " ARTIFACT_EDIT_ENTERED")
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Edit",
            },
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artifact_modified_by_user_id = self.request.user
        self.object.save()
        self.object.logger(str(self.request.user), " ARTIFACT_EDIT_EXECUTED")
        messages.success(self.request, "Artifact edited")

        # check for existing hashes
        self.object.check_existing_hashes(self.request)

        return super().form_valid(form)
