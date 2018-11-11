from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import AnalysisstatusForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Analysisstatus

class Analysisstatuss(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Analysisstatus
    template_name = 'dfirtrack_main/analysisstatus/analysisstatuss_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " ANALYSISSTATUS_ENTERED")
        return Analysisstatus.objects.order_by('analysisstatus_name')

class AnalysisstatussDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Analysisstatus
    template_name = 'dfirtrack_main/analysisstatus/analysisstatuss_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        analysisstatus = self.object
        analysisstatus.logger(str(self.request.user), " ANALYSISSTATUSDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def analysisstatuss_add(request):
    if request.method == 'POST':
        form = AnalysisstatusForm(request.POST)
        if form.is_valid():
            analysisstatus = form.save(commit=False)
            analysisstatus.save()
            analysisstatus.logger(str(request.user), " ANALYSISSTATUSDETAIL_ADD_EXECUTED")
            messages.success(request, 'Analysisstatus added')
            return redirect('/analysisstatuss')
    else:
        form = AnalysisstatusForm()
        debug_logger(str(request.user), " ANALYSISSTATUS_ADD_ENTERED")
    return render(request, 'dfirtrack_main/analysisstatus/analysisstatuss_add.html', {'form': form})

@login_required(login_url="/login")
def analysisstatuss_add_popup(request):
    if request.method == 'POST':
        form = AnalysisstatusForm(request.POST)
        if form.is_valid():
            analysisstatus = form.save(commit=False)
            analysisstatus.save()
            analysisstatus.logger(str(request.user), " ANALYSISSTATUSDETAIL_ADD_POPUP_EXECUTED")
            messages.success(request, 'Analysisstatus added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = AnalysisstatusForm()
        debug_logger(str(request.user), " ANALYSISSTATUS_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/analysisstatus/analysisstatuss_add_popup.html', {'form': form})

@login_required(login_url="/login")
def analysisstatuss_edit(request, pk):
    analysisstatus = get_object_or_404(Analysisstatus, pk=pk)
    if request.method == 'POST':
        form = AnalysisstatusForm(request.POST, instance=analysisstatus)
        if form.is_valid():
            analysisstatus = form.save(commit=False)
            analysisstatus.save()
            analysisstatus.logger(str(request.user), " ANALYSISSTATUS_EDIT_EXECUTED")
            messages.success(request, 'Analysisstatus edited')
            return redirect('/analysisstatuss')
    else:
        form = AnalysisstatusForm(instance=analysisstatus)
        analysisstatus.logger(str(request.user), " ANALYSISSTATUS_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/analysisstatus/analysisstatuss_edit.html', {'form': form})
