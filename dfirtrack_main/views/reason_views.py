from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import ReasonForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Reason

class ReasonList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Reason
    template_name = 'dfirtrack_main/reason/reasons_list.html'
    context_object_name = 'reason_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " REASON_ENTERED")
        return Reason.objects.order_by('reason_name')

class ReasonDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Reason
    template_name = 'dfirtrack_main/reason/reasons_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reason = self.object
        reason.logger(str(self.request.user), " REASONDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def reasons_add(request):
    if request.method == 'POST':
        form = ReasonForm(request.POST)
        if form.is_valid():
            reason = form.save(commit=False)
            reason.save()
            reason.logger(str(request.user), " REASON_ADD_EXECUTED")
            messages.success(request, 'Reason added')
            return redirect('/reasons')
    else:
        form = ReasonForm()
        debug_logger(str(request.user), " REASON_ADD_ENTERED")
    return render(request, 'dfirtrack_main/reason/reasons_add.html', {'form': form})

@login_required(login_url="/login")
def reasons_add_popup(request):
    if request.method == 'POST':
        form = ReasonForm(request.POST)
        if form.is_valid():
            reason = form.save(commit=False)
            reason.save()
            reason.logger(str(request.user), " REASON_ADD_POPUP_EXECUTED")
            messages.success(request, 'Reason added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = ReasonForm()
        debug_logger(str(request.user), " REASON_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/reason/reasons_add_popup.html', {'form': form})

@login_required(login_url="/login")
def reasons_edit(request, pk):
    reason = get_object_or_404(Reason, pk=pk)
    if request.method == 'POST':
        form = ReasonForm(request.POST, instance=reason)
        if form.is_valid():
            reason = form.save(commit=False)
            reason.save()
            reason.logger(str(request.user), " REASON_EDIT_EXECUTED")
            messages.success(request, 'Reason edited')
            return redirect('/reasons')
    else:
        form = ReasonForm(instance=reason)
        reason.logger(str(request.user), " REASON_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/reason/reasons_edit.html', {'form': form})
