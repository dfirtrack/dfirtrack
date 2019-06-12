from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import DnsnameForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Dnsname

class DnsnameList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Dnsname
    template_name = 'dfirtrack_main/dnsname/dnsnames_list.html'
    context_object_name = 'dnsname_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " DNSNAME_ENTERED")
        return Dnsname.objects.order_by('dnsname_name')

class DnsnameDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Dnsname
    template_name = 'dfirtrack_main/dnsname/dnsnames_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dnsname = self.object
        dnsname.logger(str(self.request.user), " DNSNAMEDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def dnsnames_add(request):
    if request.method == 'POST':
        form = DnsnameForm(request.POST)
        if form.is_valid():
            dnsname = form.save(commit=False)
            dnsname.save()
            dnsname.logger(str(request.user), " DNSNAME_ADD_EXECUTED")
            messages.success(request, 'DNS name added')
            return redirect('/dnsnames')
    else:
        form = DnsnameForm()
        debug_logger(str(request.user), " DNSNAME_ADD_ENTERED")
    return render(request, 'dfirtrack_main/dnsname/dnsnames_add.html', {'form': form})

@login_required(login_url="/login")
def dnsnames_add_popup(request):
    if request.method == 'POST':
        form = DnsnameForm(request.POST)
        if form.is_valid():
            dnsname = form.save(commit=False)
            dnsname.save()
            dnsname.logger(str(request.user), " DNSNAME_ADD_POPUP_EXECUTED")
            messages.success(request, 'DNS name added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = DnsnameForm()
        debug_logger(str(request.user), " DNSNAME_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/dnsname/dnsnames_add_popup.html', {'form': form})

@login_required(login_url="/login")
def dnsnames_edit(request, pk):
    dnsname = get_object_or_404(Dnsname, pk=pk)
    if request.method == 'POST':
        form = DnsnameForm(request.POST, instance=dnsname)
        if form.is_valid():
            dnsname = form.save(commit=False)
            dnsname.save()
            dnsname.logger(str(request.user), " DNSNAME_EDIT_EXECUTED")
            messages.success(request, 'DNS name edited')
            return redirect('/dnsnames')
    else:
        form = DnsnameForm(instance=dnsname)
        dnsname.logger(str(request.user), " DNSNAME_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/dnsname/dnsnames_edit.html', {'form': form})
