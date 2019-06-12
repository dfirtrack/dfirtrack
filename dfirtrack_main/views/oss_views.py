from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import OsForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Os

class OsList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Os
    template_name = 'dfirtrack_main/os/oss_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " OS_ENTERED")
        return Os.objects.order_by('os_name')

class OsDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Os
    template_name = 'dfirtrack_main/os/oss_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        os = self.object
        os.logger(str(self.request.user), " OSDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def oss_add(request):
    if request.method == 'POST':
        form = OsForm(request.POST)
        if form.is_valid():
            os = form.save(commit=False)
            os.save()
            os.logger(str(request.user), " OS_ADD_EXECUTED")
            messages.success(request, 'OS added')
            return redirect('/oss')
    else:
        form = OsForm()
        debug_logger(str(request.user), " OS_ADD_ENTERED")
    return render(request, 'dfirtrack_main/os/oss_add.html', {'form': form})

@login_required(login_url="/login")
def oss_add_popup(request):
    if request.method == 'POST':
        form = OsForm(request.POST)
        if form.is_valid():
            os = form.save(commit=False)
            os.save()
            os.logger(str(request.user), " OS_ADD_POPUP_EXECUTED")
            messages.success(request, 'OS added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = OsForm()
        debug_logger(str(request.user), " OS_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/os/oss_add_popup.html', {'form': form})

@login_required(login_url="/login")
def oss_edit(request, pk):
    os = get_object_or_404(Os, pk=pk)
    if request.method == 'POST':
        form = OsForm(request.POST, instance=os)
        if form.is_valid():
            os = form.save(commit=False)
            os.save()
            os.logger(str(request.user), " OS_EDIT_EXECUTED")
            messages.success(request, 'OS edited')
            return redirect('/oss')
    else:
        form = OsForm(instance=os)
        os.logger(str(request.user), " OS_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/os/oss_edit.html', {'form': form})
