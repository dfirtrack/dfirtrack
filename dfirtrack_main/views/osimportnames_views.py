from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import OsimportnameForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Osimportname

class OsimportnameList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Osimportname
    template_name = 'dfirtrack_main/osimportname/osimportnames_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " OSIMPORTNAME_ENTERED")
        return Osimportname.objects.order_by('osimportname_name')

@login_required(login_url="/login")
def osimportnames_add(request):
    if request.method == 'POST':
        form = OsimportnameForm(request.POST)
        if form.is_valid():
            osimportname = form.save(commit=False)
            osimportname.save()
            osimportname.logger(str(request.user), " OSIMPORTNAME_ADD_EXECUTED")
            messages.success(request, 'OS-Importname added')
            return redirect('/osimportnames')
    else:
        form = OsimportnameForm()
        debug_logger(str(request.user), " OSIMPORTNAME_ADD_ENTERED")
    return render(request, 'dfirtrack_main/osimportname/osimportnames_add.html', {'form': form})

@login_required(login_url="/login")
def osimportnames_edit(request, pk):
    osimportname = get_object_or_404(Osimportname, pk=pk)
    if request.method == 'POST':
        form = OsimportnameForm(request.POST, instance=osimportname)
        if form.is_valid():
            osimportname = form.save(commit=False)
            osimportname.save()
            osimportname.logger(str(request.user), " OSIMPORTNAME_EDIT_EXECUTED")
            messages.success(request, 'OS-Importname edited')
            return redirect('/osimportnames')
    else:
        form = OsimportnameForm(instance=osimportname)
        osimportname.logger(str(request.user), " OSIMPORTNAME_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/osimportname/osimportnames_edit.html', {'form': form})
