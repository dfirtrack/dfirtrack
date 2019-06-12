from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import SystemtypeForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Systemtype

class SystemtypeList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Systemtype
    template_name = 'dfirtrack_main/systemtype/systemtypes_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " SYSTEMTYPE_ENTERED")
        return Systemtype.objects.order_by('systemtype_name')

class SystemtypeDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Systemtype
    template_name = 'dfirtrack_main/systemtype/systemtypes_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        systemtype = self.object
        systemtype.logger(str(self.request.user), " SYSTEMTYPEDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def systemtypes_add(request):
    if request.method == 'POST':
        form = SystemtypeForm(request.POST)
        if form.is_valid():
            systemtype = form.save(commit=False)
            systemtype.save()
            systemtype.logger(str(request.user), " SYSTEMTYPE_ADD_EXECUTED")
            messages.success(request, 'Systemtype added')
            return redirect('/systemtypes')
    else:
        form = SystemtypeForm()
        debug_logger(str(request.user), " SYSTEMTYPE_ADD_ENTERED")
    return render(request, 'dfirtrack_main/systemtype/systemtypes_add.html', {'form': form})

@login_required(login_url="/login")
def systemtypes_add_popup(request):
    if request.method == 'POST':
        form = SystemtypeForm(request.POST)
        if form.is_valid():
            systemtype = form.save(commit=False)
            systemtype.save()
            systemtype.logger(str(request.user), " SYSTEMTYPE_ADD_POPUP_EXECUTED")
            messages.success(request, 'Systemtype added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = SystemtypeForm()
        debug_logger(str(request.user), " SYSTEMTYPE_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/systemtype/systemtypes_add_popup.html', {'form': form})

@login_required(login_url="/login")
def systemtypes_edit(request, pk):
    systemtype = get_object_or_404(Systemtype, pk=pk)
    if request.method == 'POST':
        form = SystemtypeForm(request.POST, instance=systemtype)
        if form.is_valid():
            systemtype = form.save(commit=False)
            systemtype.save()
            systemtype.logger(str(request.user), " SYSTEMTYPE_EDIT_EXECUTED")
            messages.success(request, 'Systemtype edited')
            return redirect('/systemtypes')
    else:
        form = SystemtypeForm(instance=systemtype)
        systemtype.logger(str(request.user), " SYSTEMTYPE_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/systemtype/systemtypes_edit.html', {'form': form})
