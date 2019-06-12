from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import TasknameForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Taskname

class TasknameList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Taskname
    template_name = 'dfirtrack_main/taskname/tasknames_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " TASKNAME_ENTERED")
        return Taskname.objects.order_by('taskname_name')

class TasknameDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Taskname
    template_name = 'dfirtrack_main/taskname/tasknames_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        taskname = self.object
        taskname.logger(str(self.request.user), " TASKNAMEDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def tasknames_add(request):
    if request.method == 'POST':
        form = TasknameForm(request.POST)
        if form.is_valid():
            taskname = form.save(commit=False)
            taskname.save()
            taskname.logger(str(request.user), " TASKNAME_ADD_EXECUTED")
            messages.success(request, 'Taskname added')
            return redirect('/tasknames')
    else:
        form = TasknameForm()
        debug_logger(str(request.user), " TASKNAME_ADD_ENTERED")
    return render(request, 'dfirtrack_main/taskname/tasknames_add.html', {'form': form})

@login_required(login_url="/login")
def tasknames_edit(request, pk):
    taskname = get_object_or_404(Taskname, pk=pk)
    if request.method == 'POST':
        form = TasknameForm(request.POST, instance=taskname)
        if form.is_valid():
            taskname = form.save(commit=False)
            taskname.save()
            taskname.logger(str(request.user), " TASKNAME_EDIT_EXECUTED")
            messages.success(request, 'Taskname edited')
            return redirect('/tasknames')
    else:
        form = TasknameForm(instance=taskname)
        taskname.logger(str(request.user), " TASKNAME_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/taskname/tasknames_edit.html', {'form': form})
