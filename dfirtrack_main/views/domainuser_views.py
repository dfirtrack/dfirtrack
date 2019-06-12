from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import DomainuserForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Domainuser

class DomainuserList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Domainuser
    template_name = 'dfirtrack_main/domainuser/domainusers_list.html'
    context_object_name = 'domainuser_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " DOMAINUSER_ENTERED")
        return Domainuser.objects.order_by('domainuser_name')

class DomainuserDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Domainuser
    template_name = 'dfirtrack_main/domainuser/domainusers_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        domainuser = self.object
        domainuser.logger(str(self.request.user), " DOMAINUSERDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def domainusers_add(request):
    if request.method == 'POST':
        form = DomainuserForm(request.POST)
        if form.is_valid():
            domainuser = form.save(commit=False)
            domainuser.save()
            form.save_m2m()
            domainuser.logger(str(request.user), " DOMAINUSER_ADD_EXECUTED")
            messages.success(request, 'Domainuser added')
            return redirect('/domainusers')
    else:
        form = DomainuserForm()
        debug_logger(str(request.user), " DOMAINUSER_ADD_ENTERED")
    return render(request, 'dfirtrack_main/domainuser/domainusers_add.html', {'form': form})

@login_required(login_url="/login")
def domainusers_edit(request, pk):
    domainuser = get_object_or_404(Domainuser, pk=pk)
    if request.method == 'POST':
        form = DomainuserForm(request.POST, instance=domainuser)
        if form.is_valid():
            domainuser = form.save(commit=False)
            domainuser.save()
            form.save_m2m()
            domainuser.logger(str(request.user), " DOMAINUSER_EDIT_EXECUTED")
            messages.success(request, 'Domainuser edited')
            return redirect('/domainusers')
    else:
        form = DomainuserForm(instance=domainuser)
        domainuser.logger(str(request.user), " DOMAINUSER_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/domainuser/domainusers_edit.html', {'form': form})
