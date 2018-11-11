from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import TaskstatusForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Taskstatus

class Taskstatuss(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Taskstatus
    template_name = 'dfirtrack_main/taskstatus/taskstatuss_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " TASKSTATUS_ENTERED")
        return Taskstatus.objects.order_by('taskstatus_name')

class TaskstatussDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Taskstatus
    template_name = 'dfirtrack_main/taskstatus/taskstatuss_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        taskstatus = self.object
        taskstatus.logger(str(self.request.user), " TASKSTATUSDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def taskstatuss_add(request):
    if request.method == 'POST':
        form = TaskstatusForm(request.POST)
        if form.is_valid():
            taskstatus = form.save(commit=False)
            taskstatus.save()
            taskstatus.logger(str(request.user), " TASKSTATUS_ADD_EXECUTED")
            messages.success(request, 'Taskstatus added')
            return redirect('/taskstatuss')
    else:
        form = TaskstatusForm()
        debug_logger(str(request.user), " TASKSTATUS_ADD_ENTERED")
    return render(request, 'dfirtrack_main/taskstatus/taskstatuss_add.html', {'form': form})

@login_required(login_url="/login")
def taskstatuss_edit(request, pk):
    taskstatus = get_object_or_404(Taskstatus, pk=pk)
    if request.method == 'POST':
        form = TaskstatusForm(request.POST, instance=taskstatus)
        if form.is_valid():
            taskstatus = form.save(commit=False)
            taskstatus.save()
            taskstatus.logger(str(request.user), " TASKSTATUS_EDIT_EXECUTED")
            messages.success(request, 'Taskstatus edited')
            return redirect('/taskstatuss')
    else:
        form = TaskstatusForm(instance=taskstatus)
        taskstatus.logger(str(request.user), " TASKSTATUS_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/taskstatus/taskstatuss_edit.html', {'form': form})
