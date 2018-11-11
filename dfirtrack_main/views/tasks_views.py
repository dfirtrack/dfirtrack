from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import TaskForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Task, Taskstatus

class Tasks(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Task
    template_name = 'dfirtrack_main/task/tasks_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " TASK_ENTERED")
        return Task.objects.order_by('taskstatus')

class TasksDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Task
    template_name = 'dfirtrack_main/task/tasks_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.object
        task.logger(str(self.request.user), " TASKDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def tasks_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_created_by_user_id = request.user
            task.task_modified_by_user_id = request.user
            task.save()
            form.save_m2m()
            task.logger(str(request.user), " TASK_ADD_EXECUTED")
            messages.success(request, 'Task added')
        if 'system' in request.GET:
            system = request.GET['system']
            return redirect('/systems/' + str(system))
        else:
            return redirect('/tasks/' + str(task.task_id))
    else:
        if request.method == 'GET' and 'system' in request.GET:
            system = request.GET['system']
            form = TaskForm(initial={
                'system': system,
                'taskpriority': 2,
                'taskstatus': 1,
                'task_scheduled_time': timezone.now(),
                'task_due_time': timezone.now(),
            })
        else:
            form = TaskForm(initial={
                'taskpriority': 2,
                'taskstatus': 1,
                'task_scheduled_time': timezone.now(),
                'task_due_time': timezone.now(),
            })
        debug_logger(str(request.user), " TASK_ADD_ENTERED")
    return render(request, 'dfirtrack_main/task/tasks_add.html', {'form': form})

@login_required(login_url="/login")
def tasks_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_modified_by_user_id = request.user
            task.save()
            form.save_m2m()
            task.logger(str(request.user), " TASK_EDIT_EXECUTED")
            messages.success(request, 'Task edited')
            return redirect('/tasks/' + str(task.task_id))
    else:
        form = TaskForm(instance=task)
        task.logger(str(request.user), " TASK_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/task/tasks_edit.html', {'form': form})

@login_required(login_url="/login")
def tasks_start(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.task_started_time = timezone.now()
    task.taskstatus = Taskstatus.objects.get(taskstatus_name="Working")
    task.save()
    task.logger(str(request.user), " TASK_START_EXECUTED")
    messages.success(request, 'Task started')
    if 'system' in request.GET:
        system = request.GET['system']
        return redirect('/systems/' + str(system))
    else:
        return redirect('/tasks/' + str(task.task_id))

@login_required(login_url="/login")
def tasks_finish(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.task_finished_time = timezone.now()
    task.taskstatus = Taskstatus.objects.get(taskstatus_name="Done")
    task.save()
    task.logger(str(request.user), " TASK_FINISH_EXECUTED")
    messages.success(request, 'Task finished')
    if 'system' in request.GET:
        system = request.GET['system']
        return redirect('/systems/' + str(system))
    else:
        return redirect('/tasks/' + str(task.task_id))

@login_required(login_url="/login")
def tasks_renew(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.task_started_time = None
    task.task_finished_time = None
    task.taskstatus = Taskstatus.objects.get(taskstatus_name="Pending")
    task.task_assigned_to_user_id = None
    task.save()
    task.logger(str(request.user), " TASK_RENEW_EXECUTED")
    messages.warning(request, 'Task renewed')
    if 'system' in request.GET:
        system = request.GET['system']
        return redirect('/systems/' + str(system))
    else:
        return redirect('/tasks/' + str(task.task_id))

@login_required(login_url="/login")
def tasks_user(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.task_assigned_to_user_id = request.user
    task.save()
    task.logger(str(request.user), " TASK_USER_EXECUTED")
    messages.success(request, 'Task assigned to you')
    if 'system' in request.GET:
        system = request.GET['system']
        return redirect('/systems/' + str(system))
    else:
        return redirect('/tasks/' + str(task.task_id))
