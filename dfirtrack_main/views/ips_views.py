from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import IpForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Ip

class Ips(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Ip
    template_name = 'dfirtrack_main/ip/ips_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " IP_ENTERED")
        return Ip.objects.order_by('ip_ip')

class IpsDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Ip
    template_name = 'dfirtrack_main/ip/ips_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ip = self.object
        ip.logger(str(self.request.user), " IPDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def ips_add(request):
    if request.method == 'POST':
        form = IpForm(request.POST)
        if form.is_valid():
            ip = form.save(commit=False)
            ip.save()
            ip.logger(str(request.user), " IP_ADD_EXECUTED")
            messages.success(request, 'IP address added')
            return redirect('/ips')
    else:
        form = IpForm()
        debug_logger(str(request.user), " IP_ADD_ENTERED")
    return render(request, 'dfirtrack_main/ip/ips_add.html', {'form': form})

@login_required(login_url="/login")
def ips_add_popup(request):
    if request.method == 'POST':
        form = IpForm(request.POST)
        if form.is_valid():
            ip = form.save(commit=False)
            ip.save()
            ip.logger(str(request.user), " IP_ADD_POPUP_EXECUTED")
            messages.success(request, 'IP address added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = IpForm()
        debug_logger(str(request.user), " IP_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/ip/ips_add_popup.html', {'form': form})

@login_required(login_url="/login")
def ips_edit(request, pk):
    ip = get_object_or_404(Ip, pk=pk)
    if request.method == 'POST':
        form = IpForm(request.POST, instance=ip)
        if form.is_valid():
            ip = form.save(commit=False)
            ip.save()
            ip.logger(str(request.user), " IP_EDIT_EXECUTED")
            messages.success(request, 'IP address edited')
            return redirect('/ips')
    else:
        form = IpForm(instance=ip)
        ip.logger(str(request.user), " IP_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/ip/ips_edit.html', {'form': form})
