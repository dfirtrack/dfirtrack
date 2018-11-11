from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import SystemuserForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Systemuser

class Systemusers(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Systemuser
    template_name = 'dfirtrack_main/systemuser/systemusers_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " SYSTEMUSER_ENTERED")
        return Systemuser.objects.order_by('systemuser_name')

class SystemusersDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Systemuser
    template_name = 'dfirtrack_main/systemuser/systemusers_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        systemuser = self.object
        systemuser.logger(str(self.request.user), " SYSTEMUSERDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def systemusers_add(request):
    if request.method == 'POST':
        form = SystemuserForm(request.POST)
        if form.is_valid():
            systemuser = form.save(commit=False)
            systemuser.save()
            systemuser.logger(str(request.user), " SYSTEMUSER_ADD_EXECUTED")
            messages.success(request, 'Systemuser added')
            return redirect('/systemusers')
    else:
        form = SystemuserForm()
        debug_logger(str(request.user), " SYSTEMUSER_ADD_ENTERED")
    return render(request, 'dfirtrack_main/systemuser/systemusers_add.html', {'form': form})

@login_required(login_url="/login")
def systemusers_edit(request, pk):
    systemuser = get_object_or_404(Systemuser, pk=pk)
    if request.method == 'POST':
        form = SystemuserForm(request.POST, instance=systemuser)
        if form.is_valid():
            systemuser = form.save(commit=False)
            systemuser.save()
            systemuser.logger(str(request.user), " SYSTEMUSER_EDIT_EXECUTED")
            messages.success(request, 'Systemuser edited')
            return redirect('/systemusers')
    else:
        form = SystemuserForm(instance=systemuser)
        systemuser.logger(str(request.user), " SYSTEMUSER_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/systemuser/systemusers_edit.html', {'form': form})
