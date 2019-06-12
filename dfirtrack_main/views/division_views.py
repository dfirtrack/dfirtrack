from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import DivisionForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Division

class DivisionList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Division
    template_name = 'dfirtrack_main/division/divisions_list.html'
    context_object_name = 'division_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " DIVISION_ENTERED")
        return Division.objects.order_by('division_name')

class DivisionDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Division
    template_name = 'dfirtrack_main/division/divisions_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        division = self.object
        division.logger(str(self.request.user), " DIVISIONDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def divisions_add(request):
    if request.method == 'POST':
        form = DivisionForm(request.POST)
        if form.is_valid():
            division = form.save(commit=False)
            division.save()
            division.logger(str(request.user), " DIVISION_ADD_EXECUTED")
            messages.success(request, 'Division added')
            return redirect('/divisions')
    else:
        form = DivisionForm()
        debug_logger(str(request.user), " DIVISION_ADD_ENTERED")
    return render(request, 'dfirtrack_main/division/divisions_add.html', {'form': form})

@login_required(login_url="/login")
def divisions_edit(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == 'POST':
        form = DivisionForm(request.POST, instance=division)
        if form.is_valid():
            division = form.save(commit=False)
            division.save()
            division.logger(str(request.user), " DIVISION_EDIT_EXECUTED")
            messages.success(request, 'Division edited')
            return redirect('/divisions')
    else:
        form = DivisionForm(instance=division)
        division.logger(str(request.user), " DIVISION_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/division/divisions_edit.html', {'form': form})
