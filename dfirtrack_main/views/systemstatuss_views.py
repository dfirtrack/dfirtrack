from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import SystemstatusForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Systemstatus

class Systemstatuss(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Systemstatus
    template_name = 'dfirtrack_main/systemstatus/systemstatuss_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " SYSTEMSTATUS_ENTERED")
        return Systemstatus.objects.order_by('systemstatus_name')

class SystemstatussDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Systemstatus
    template_name = 'dfirtrack_main/systemstatus/systemstatuss_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        systemstatus = self.object
        systemstatus.logger(str(self.request.user), " SYSTEMSTATUSDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def systemstatuss_add(request):
    if request.method == 'POST':
        form = SystemstatusForm(request.POST)
        if form.is_valid():
            systemstatus = form.save(commit=False)
            systemstatus.save()
            systemstatus.logger(str(request.user), " SYSTEMSTATUS_ADD_EXECUTED")
            messages.success(request, 'Systemstatus added')
            return redirect('/systemstatuss')
    else:
        form = SystemstatusForm()
        debug_logger(str(request.user), " SYSTEMSTATUS_ADD_ENTERED")
    return render(request, 'dfirtrack_main/systemstatus/systemstatuss_add.html', {'form': form})

@login_required(login_url="/login")
def systemstatuss_add_popup(request):
    if request.method == 'POST':
        form = SystemstatusForm(request.POST)
        if form.is_valid():
            systemstatus = form.save(commit=False)
            systemstatus.save()
            systemstatus.logger(str(request.user), " SYSTEMSTATUS_ADD_POPUP_EXECUTED")
            messages.success(request, 'Systemstatus added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = SystemstatusForm()
        debug_logger(str(request.user), " SYSTEMSTATUS_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/systemstatus/systemstatuss_add_popup.html', {'form': form})

@login_required(login_url="/login")
def systemstatuss_edit(request, pk):
    systemstatus = get_object_or_404(Systemstatus, pk=pk)
    if request.method == 'POST':
        form = SystemstatusForm(request.POST, instance=systemstatus)
        if form.is_valid():
            systemstatus = form.save(commit=False)
            systemstatus.save()
            systemstatus.logger(str(request.user), " SYSTEMSTATUS_EDIT_EXECUTED")
            messages.success(request, 'Systemstatus edited')
            return redirect('/systemstatuss')
    else:
        form = SystemstatusForm(instance=systemstatus)
        systemstatus.logger(str(request.user), " SYSTEMSTATUS_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/systemstatus/systemstatuss_edit.html', {'form': form})
