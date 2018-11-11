from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import TaskpriorityForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Taskpriority

class Taskprioritys(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Taskpriority
    template_name = 'dfirtrack_main/taskpriority/taskprioritys_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " TASKPRIORITY_ENTERED")
        return Taskpriority.objects.order_by('taskpriority_name')

class TaskprioritysDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Taskpriority
    template_name = 'dfirtrack_main/taskpriority/taskprioritys_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        taskpriority = self.object
        taskpriority.logger(str(self.request.user), " TASKPRIORITYDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def taskprioritys_add(request):
    if request.method == 'POST':
        form = TaskpriorityForm(request.POST)
        if form.is_valid():
            taskpriority = form.save(commit=False)
            taskpriority.save()
            taskpriority.logger(str(request.user), " TASKPRIORITY_ADD_EXECUTED")
            messages.success(request, 'Taskpriority added')
            return redirect('/taskprioritys')
    else:
        form = TaskpriorityForm()
        debug_logger(str(request.user), " TASKPRIORITY_ADD_ENTERED")
    return render(request, 'dfirtrack_main/taskpriority/taskprioritys_add.html', {'form': form})

@login_required(login_url="/login")
def taskprioritys_edit(request, pk):
    taskpriority = get_object_or_404(Taskpriority, pk=pk)
    if request.method == 'POST':
        form = TaskpriorityForm(request.POST, instance=taskpriority)
        if form.is_valid():
            taskpriority = form.save(commit=False)
            taskpriority.save()
            taskpriority.logger(str(request.user), " TASKPRIORITY_EDIT_EXECUTED")
            messages.success(request, 'Taskpriority edited')
            return redirect('/taskprioritys')
    else:
        form = TaskpriorityForm(instance=taskpriority)
        taskpriority.logger(str(request.user), " TASKPRIORITY_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/taskpriority/taskprioritys_edit.html', {'form': form})
