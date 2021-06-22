from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from dfirtrack_main.models import Casetype
from dfirtrack_main.forms import CasetypeForm
from dfirtrack_main.logger.default_logger import debug_logger

class CasetypeList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Casetype
    template_name = 'dfirtrack_main/casetype/casetype_list.html'
    context_object_name = 'casetype_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " CASETYPE_LIST_ENTERED")
        return Casetype.objects.order_by('casetype_name')

class CasetypeDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Casetype
    template_name = 'dfirtrack_main/casetype/casetype_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        casetype = self.object
        casetype.logger(str(self.request.user), ' CASETYPE_DETAIL_ENTERED')
        return context

class CasetypeCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Casetype
    form_class = CasetypeForm
    template_name = 'dfirtrack_main/casetype/casetype_generic_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        debug_logger(str(request.user), ' CASETYPE_ADD_ENTERED')
        return render(request, self.template_name, {
            'form': form,
            'title': 'Add',
        })

    def form_valid(self, form):
        self.object = form.save()
        self.object.logger(str(self.request.user), ' CASETYPE_ADD_EXECUTED')
        messages.success(self.request, 'Casetype added')
        return super().form_valid(form)

class CasetypeUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Casetype
    form_class = CasetypeForm
    template_name = 'dfirtrack_main/casetype/casetype_generic_form.html'

    def get(self, request, *args, **kwargs):
        casetype = self.get_object()
        form = self.form_class(instance = casetype)
        casetype.logger(str(request.user), ' CASETYPE_EDIT_ENTERED')
        return render(request, self.template_name, {
            'form': form,
            'title': 'Edit',
        })

    def form_valid(self, form):
        self.object = form.save()
        self.object.logger(str(self.request.user), ' CASETYPE_EDIT_EXECUTED')
        messages.success(self.request, 'Casetype edited')
        return super().form_valid(form)
