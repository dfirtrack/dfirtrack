from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import AnalystmemoForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Analystmemo

class AnalystmemoList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Analystmemo
    template_name = 'dfirtrack_main/analystmemo/analystmemos_list.html'
    context_object_name = 'analystmemo_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " ANALYSTMEMO_ENTERED")
        return Analystmemo.objects.order_by('analystmemo_id')

class AnalystmemoDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Analystmemo
    template_name = 'dfirtrack_main/analystmemo/analystmemos_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        analystmemo = self.object
        analystmemo.logger(str(self.request.user), " ANALYSTMEMODETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def analystmemos_add(request):
    if request.method == 'POST':
        form = AnalystmemoForm(request.POST)
        if form.is_valid():
            analystmemo = form.save(commit=False)
            analystmemo.analystmemo_created_by_user_id = request.user
            analystmemo.analystmemo_modified_by_user_id = request.user
            analystmemo.save()
            analystmemo.logger(str(request.user), " ANALYSTMEMO_ADD_EXECUTED")
            messages.success(request, 'Analystmemo added')
            return redirect('/systems/' + str(analystmemo.system.system_id))
    else:
        if request.method == 'GET' and 'system' in request.GET:
            system = request.GET['system']
            form = AnalystmemoForm(initial={
                'system': system,
            })
        else:
            form = AnalystmemoForm()
        debug_logger(str(request.user), " ANALYSTMEMO_ADD_ENTERED")
    return render(request, 'dfirtrack_main/analystmemo/analystmemos_add.html', {'form': form})

@login_required(login_url="/login")
def analystmemos_edit(request, pk):
    analystmemo = get_object_or_404(Analystmemo, pk=pk)
    if request.method == 'POST':
        form = AnalystmemoForm(request.POST, instance=analystmemo)
        if form.is_valid():
            analystmemo = form.save(commit=False)
            analystmemo.analystmemo_modified_by_user_id = request.user
            analystmemo.save()
            analystmemo.logger(str(request.user), " ANALYSTMEMO_EDIT_EXECUTED")
            messages.success(request, 'Analystmemo edited')
            return redirect('/systems/' + str(analystmemo.system.system_id))
    else:
        form = AnalystmemoForm(instance=analystmemo)
        analystmemo.logger(str(request.user), " ANALYSTMEMO_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/analystmemo/analystmemos_edit.html', {'form': form})
