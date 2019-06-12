from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import DomainForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Domain

class DomainList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Domain
    template_name = 'dfirtrack_main/domain/domains_list.html'
    context_object_name = 'domain_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " DOMAIN_ENTERED")
        return Domain.objects.order_by('domain_name')

class DomainDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Domain
    template_name = 'dfirtrack_main/domain/domains_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        domain = self.object
        domain.logger(str(self.request.user), " DOMAINDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def domains_add(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain = form.save(commit=False)
            domain.save()
            domain.logger(str(request.user), " DOMAIN_ADD_EXECUTED")
            messages.success(request, 'Domain added')
            return redirect('/domains')
    else:
        form = DomainForm()
        debug_logger(str(request.user), " DOMAIN_ADD_ENTERED")
    return render(request, 'dfirtrack_main/domain/domains_add.html', {'form': form})

@login_required(login_url="/login")
def domains_add_popup(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            domain = form.save(commit=False)
            domain.save()
            domain.logger(str(request.user), " DOMAIN_ADD_POPUP_EXECUTED")
            messages.success(request, 'Domain added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = DomainForm()
        debug_logger(str(request.user), " DOMAIN_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/domain/domains_add_popup.html', {'form': form})

@login_required(login_url="/login")
def domains_edit(request, pk):
    domain = get_object_or_404(Domain, pk=pk)
    if request.method == 'POST':
        form = DomainForm(request.POST, instance=domain)
        if form.is_valid():
            domain = form.save(commit=False)
            domain.save()
            domain.logger(str(request.user), " DOMAIN_EDIT_EXECUTED")
            messages.success(request, 'Domain edited')
            return redirect('/domains')
    else:
        form = DomainForm(instance=domain)
        domain.logger(str(request.user), " DOMAIN_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/domain/domains_edit.html', {'form': form})
