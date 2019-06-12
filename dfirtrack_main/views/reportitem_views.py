from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import ReportitemForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Reportitem

class ReportitemList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Reportitem
    template_name = 'dfirtrack_main/reportitem/reportitems_list.html'
    context_object_name = 'reportitem_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " REPORTITEM_ENTERED")
        return Reportitem.objects.order_by('reportitem_id')

class ReportitemDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Reportitem
    template_name = 'dfirtrack_main/reportitem/reportitems_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reportitem = self.object
        reportitem.logger(str(self.request.user), " REPORTITEMDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def reportitems_add(request):
    if request.method == 'POST':
        form = ReportitemForm(request.POST)
        if form.is_valid():
            reportitem = form.save(commit=False)
            reportitem.reportitem_created_by_user_id = request.user
            reportitem.reportitem_modified_by_user_id = request.user
            reportitem.save()
            reportitem.logger(str(request.user), " REPORTITEM_ADD_EXECUTED")
            messages.success(request, 'Reportitem added')
            return redirect('/systems/' + str(reportitem.system.system_id))
    else:
        if request.method == 'GET' and 'system' in request.GET:
            system = request.GET['system']
            form = ReportitemForm(initial={
                'system': system,
            })
        else:
            form = ReportitemForm()
        debug_logger(str(request.user), " REPORTITEM_ADD_ENTERED")
    return render(request, 'dfirtrack_main/reportitem/reportitems_add.html', {'form': form})

@login_required(login_url="/login")
def reportitems_edit(request, pk):
    reportitem = get_object_or_404(Reportitem, pk=pk)
    if request.method == 'POST':
        form = ReportitemForm(request.POST, instance=reportitem)
        if form.is_valid():
            reportitem = form.save(commit=False)
            reportitem.reportitem_modified_by_user_id = request.user
            reportitem.save()
            reportitem.logger(str(request.user), " REPORTITEM_EDIT_EXECUTED")
            messages.success(request, 'Reportitem edited')
            return redirect('/systems/' + str(reportitem.system.system_id))
    else:
        form = ReportitemForm(instance=reportitem)
        reportitem.logger(str(request.user), " REPORTITEM_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/reportitem/reportitems_edit.html', {'form': form})
