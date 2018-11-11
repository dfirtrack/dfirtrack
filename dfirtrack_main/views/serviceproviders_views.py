from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import ServiceproviderForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Serviceprovider

class Serviceproviders(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Serviceprovider
    template_name = 'dfirtrack_main/serviceprovider/serviceproviders_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " SERVICEPROVIDER_ENTERED")
        return Serviceprovider.objects.order_by('serviceprovider_name')

class ServiceprovidersDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Serviceprovider
    template_name = 'dfirtrack_main/serviceprovider/serviceproviders_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        serviceprovider = self.object
        serviceprovider.logger(str(self.request.user), " SERVICEPROVIDERDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def serviceproviders_add(request):
    if request.method == 'POST':
        form = ServiceproviderForm(request.POST)
        if form.is_valid():
            serviceprovider = form.save(commit=False)
            serviceprovider.save()
            serviceprovider.logger(str(request.user), " SERVICEPROVIDER_ADD_EXECUTED")
            messages.success(request, 'Serviceprovider added')
            return redirect('/serviceproviders')
    else:
        form = ServiceproviderForm()
        debug_logger(str(request.user), " SERVICEPROVIDER_ADD_ENTERED")
    return render(request, 'dfirtrack_main/serviceprovider/serviceproviders_add.html', {'form': form})

@login_required(login_url="/login")
def serviceproviders_add_popup(request):
    if request.method == 'POST':
        form = ServiceproviderForm(request.POST)
        if form.is_valid():
            serviceprovider = form.save(commit=False)
            serviceprovider.save()
            serviceprovider.logger(str(request.user), " SERVICEPROVIDER_ADD_POPUP_EXECUTED")
            messages.success(request, 'Serviceprovider added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = ServiceproviderForm()
        debug_logger(str(request.user), " SERVICEPROVIDER_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/serviceprovider/serviceproviders_add_popup.html', {'form': form})

@login_required(login_url="/login")
def serviceproviders_edit(request, pk):
    serviceprovider = get_object_or_404(Serviceprovider, pk=pk)
    if request.method == 'POST':
        form = ServiceproviderForm(request.POST, instance=serviceprovider)
        if form.is_valid():
            serviceprovider = form.save(commit=False)
            serviceprovider.save()
            serviceprovider.logger(str(request.user), " SERVICEPROVIDER_EDIT_EXECUTED")
            messages.success(request, 'Serviceprovider edited')
            return redirect('/serviceproviders')
    else:
        form = ServiceproviderForm(instance=serviceprovider)
        serviceprovider.logger(str(request.user), " SERVICEPROVIDER_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/serviceprovider/serviceproviders_edit.html', {'form': form})
