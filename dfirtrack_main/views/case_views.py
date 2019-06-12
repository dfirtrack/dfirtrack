from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import CaseForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case

class CaseList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Case
    template_name = 'dfirtrack_main/case/cases_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " CASE_ENTERED")
        return Case.objects.order_by('case_name')

class CaseDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Case
    template_name = 'dfirtrack_main/case/cases_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        case = self.object
        case.logger(str(self.request.user), " CASEDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def cases_add(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.case_created_by_user_id = request.user
            case.save()
            case.logger(str(request.user), " CASES_ADD_EXECUTED")
            messages.success(request, 'Case added')
            return redirect('/cases')
    else:
        form = CaseForm()
        debug_logger(str(request.user), " CASES_ADD_ENTERED")
    return render(request, 'dfirtrack_main/case/cases_add.html', {'form': form})

@login_required(login_url="/login")
def cases_edit(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            case = form.save(commit=False)
            case.case_created_by_user_id = request.user
            case.save()
            case.logger(str(request.user), " CASES_EDIT_EXECUTED")
            messages.success(request, 'Case edited')
            return redirect('/cases')
    else:
        form = CaseForm(instance=case)
        case.logger(str(request.user), " CASES_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/case/cases_edit.html', {'form': form})
