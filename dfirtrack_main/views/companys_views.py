from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import CompanyForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Company

class Companys(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Company
    template_name = 'dfirtrack_main/company/companys_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " COMPANY_ENTERED")
        return Company.objects.order_by('company_name')

class CompanysDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Company
    template_name = 'dfirtrack_main/company/companys_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.object
        company.logger(str(self.request.user), " COMPANYDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def companys_add(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            company.logger(str(request.user), " COMPANY_ADD_EXECUTED")
            messages.success(request, 'Company added')
            return redirect('/companys')
    else:
        form = CompanyForm()
        debug_logger(str(request.user), " COMPANY_ADD_ENTERED")
    return render(request, 'dfirtrack_main/company/companys_add.html', {'form': form})

@login_required(login_url="/login")
def companys_add_popup(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            company.logger(str(request.user), " COMPANY_ADD_POPUP_EXECUTED")
            messages.success(request, 'Company added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = CompanyForm()
        debug_logger(str(request.user), " COMPANY_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/company/companys_add_popup.html', {'form': form})

@login_required(login_url="/login")
def companys_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            company.logger(str(request.user), " COMPANY_EDIT_EXECUTED")
            messages.success(request, 'Company edited')
            return redirect('/companys')
    else:
        form = CompanyForm(instance=company)
        company.logger(str(request.user), " COMPANY_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/company/companys_edit.html', {'form': form})
