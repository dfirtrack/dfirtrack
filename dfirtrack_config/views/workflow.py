from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from dfirtrack_config.forms import (
    WorkflowDefaultArtifactAttributesFormSet,
    WorkflowDefaultTasknameAttributesFormSet,
    WorkflowForm,
)
from dfirtrack_config.models import (
    Workflow,
    WorkflowDefaultArtifactAttributes,
    WorkflowDefaultTasknameAttributes,
)
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import System


class WorkflowList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Workflow
    template_name = 'dfirtrack_config/workflow/workflows.html'
    context_object_name = 'workflow_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " WORKFLOW_LIST_ENTERED")
        return Workflow.objects.order_by('workflow_name')


class WorkflowDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Workflow
    template_name = 'dfirtrack_config/workflow/workflow_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workflow = self.object

        # get workflow artifacttype names mapping to include default_names
        context['artifacttypes'] = WorkflowDefaultArtifactAttributes.objects.filter(
            workflow=workflow
        )
        context['tasknames'] = WorkflowDefaultTasknameAttributes.objects.filter(
            workflow=workflow
        )

        workflow.logger(str(self.request.user), " WORKFLOW_DETAIL_ENTERED")
        return context


class WorkflowCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Workflow
    form_class = WorkflowForm
    template_name = 'dfirtrack_config/workflow/workflow_generic_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        # create custom WorkflowDefaultArtifactAttributesFormSet to add multiple artifacttypes to workflow
        artifacttypes_formset = WorkflowDefaultArtifactAttributesFormSet(
            queryset=WorkflowDefaultArtifactAttributes.objects.none(), prefix='artifact'
        )

        tasknames_formset = WorkflowDefaultTasknameAttributesFormSet(
            queryset=WorkflowDefaultTasknameAttributes.objects.none(),
            prefix='taskname',
        )

        debug_logger(str(request.user), " WORKFLOW_ADD_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Add',
                'artifacttypes_formset': artifacttypes_formset,
                'tasknames_formset': tasknames_formset,
            },
        )

    def post(self, request, *args, **kwargs):
        # parse forms
        form = self.form_class(request.POST)
        artifacttypes_formset = WorkflowDefaultArtifactAttributesFormSet(
            request.POST, prefix='artifact'
        )
        tasknames_formset = WorkflowDefaultTasknameAttributesFormSet(
            request.POST, prefix='taskname'
        )

        if (
            not tasknames_formset.has_changed()
            and not artifacttypes_formset.has_changed()
        ):
            form.errors['General'] = (
                ': You need to configure a taskname or artifacttype.'
            )

        # check default form and custom artifacttypes_formset
        if (
            form.is_valid()
            and artifacttypes_formset.is_valid()
            and tasknames_formset.is_valid()
        ):
            workflow = form.save(commit=False)
            workflow.workflow_created_by_user_id = request.user
            workflow.workflow_modified_by_user_id = request.user
            workflow.save()
            form.save_m2m()

            # create WorkflowDefaultArtifactAttributes mapping for every sub-form
            for artifacttypes_form in artifacttypes_formset:
                if artifacttypes_form.is_valid() and artifacttypes_form.has_changed():
                    workflow_artifacttype = artifacttypes_form.save(commit=False)
                    workflow_artifacttype.workflow = workflow
                    workflow_artifacttype.save()

            # create WorkflowDefaultTasknameAttributes for every sub-form
            for tasknames_form in tasknames_formset:
                if tasknames_form.is_valid() and tasknames_form.has_changed():
                    workflow_taskname = tasknames_form.save(commit=False)
                    workflow_taskname.workflow = workflow
                    workflow_taskname.save()

            workflow.logger(str(request.user), " WORKFLOW_ADD_EXECUTED")
            messages.success(request, 'Workflow added')
            return redirect(reverse('workflow_detail', args=(workflow.workflow_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Add',
                    'artifacttypes_formset': artifacttypes_formset,
                    'tasknames_formset': tasknames_formset,
                },
            )


class WorkflowUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Workflow
    form_class = WorkflowForm
    template_name = 'dfirtrack_config/workflow/workflow_generic_form.html'

    def get(self, request, *args, **kwargs):
        workflow = self.get_object()
        form = self.form_class(instance=workflow)

        artifacttypes_formset = WorkflowDefaultArtifactAttributesFormSet(
            queryset=WorkflowDefaultArtifactAttributes.objects.filter(
                workflow=workflow
            ),
            prefix='artifact',
        )
        tasknames_formset = WorkflowDefaultTasknameAttributesFormSet(
            queryset=WorkflowDefaultTasknameAttributes.objects.filter(
                workflow=workflow
            ),
            prefix='taskname',
        )

        workflow.logger(str(request.user), " TAG_EDIT_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Edit',
                'artifacttypes_formset': artifacttypes_formset,
                'tasknames_formset': tasknames_formset,
            },
        )

    def post(self, request, *args, **kwargs):
        workflow = self.get_object()

        # parse forms
        form = self.form_class(request.POST, instance=workflow)
        # filter artifacttypes based on workflow
        artifacttypes_formset = WorkflowDefaultArtifactAttributesFormSet(
            request.POST, prefix='artifact'
        )
        tasknames_formset = WorkflowDefaultTasknameAttributesFormSet(
            request.POST, prefix='taskname'
        )

        # check default form and custom artifacttypes_formset
        if (
            form.is_valid()
            and artifacttypes_formset.is_valid()
            and tasknames_formset.is_valid()
        ):
            workflow = form.save(commit=False)
            workflow.workflow_modified_by_user_id = request.user
            workflow.save()
            form.save_m2m()

            # create WorkflowDefaultArtifactname mapping for every sub-form
            for artifacttypes_form in artifacttypes_formset:
                if artifacttypes_form.is_valid() and artifacttypes_form.has_changed():
                    workflow_artifacttype = artifacttypes_form.save(commit=False)
                    workflow_artifacttype.workflow = workflow
                    workflow_artifacttype.save()

            # create WorkflowDefaultTasknameAttributes for every sub-form
            for tasknames_form in tasknames_formset:
                if tasknames_form.is_valid() and tasknames_form.has_changed():
                    workflow_taskname = tasknames_form.save(commit=False)
                    workflow_taskname.workflow = workflow
                    workflow_taskname.save()

            workflow.logger(str(request.user), " WORKFLOW_EDIT_EXECUTED")
            messages.success(request, 'Workflow edited')
            return redirect(reverse('workflow_detail', args=(workflow.workflow_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Edit',
                    'artifacttypes_formset': artifacttypes_formset,
                    'tasknames_formset': tasknames_formset,
                },
            )


class WorkflowDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Workflow
    template_name = 'dfirtrack_config/workflow/workflow_delete.html'

    def get(self, request, *args, **kwargs):
        workflow = self.get_object()
        workflow.logger(str(request.user), " WORKFLOW_DELETE_ENTERED")
        return render(request, self.template_name, {'workflow': workflow})

    def post(self, request, *args, **kwargs):
        workflow = self.get_object()
        workflow.logger(str(request.user), " WORKFLOW_DELETE_EXECUTED")
        workflow.delete()
        messages.success(request, 'Workflow deleted')
        return redirect(reverse('workflow_list'))


@login_required(login_url='/login')
def apply_workflows(request, system_id=None):
    try:
        # get system by id
        system = System.objects.get(pk=system_id)
    except System.DoesNotExist:
        # faulty system id
        messages.error(request, 'System does not exist')
        return redirect(reverse('system_list'))
    # parse wokflow list (multiple workflows possible)
    workflows = request.POST.getlist("workflow")
    error_code = Workflow.apply(workflows, system, request.user)
    if error_code:
        messages.error(request, 'Could not apply workflow')
        return redirect(reverse('workflow_list'))
    messages.success(request, 'Workflow applied')
    return redirect(reverse('system_detail', args=(system.system_id,)))
