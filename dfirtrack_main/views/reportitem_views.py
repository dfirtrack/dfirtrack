from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from dfirtrack_main.forms import ReportitemForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Notestatus, Reportitem


class ReportitemList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Reportitem
    template_name = 'dfirtrack_main/reportitem/reportitem_list.html'
    context_object_name = 'reportitem_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " REPORTITEM_LIST_ENTERED")
        return Reportitem.objects.order_by('reportitem_id')


class ReportitemDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Reportitem
    template_name = 'dfirtrack_main/reportitem/reportitem_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reportitem = self.object
        reportitem.logger(str(self.request.user), " REPORTITEM_DETAIL_ENTERED")
        return context


class ReportitemCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Reportitem
    form_class = ReportitemForm
    template_name = 'dfirtrack_main/reportitem/reportitem_generic_form.html'

    def get(self, request, *args, **kwargs):

        # get id of first status objects sorted by name
        notestatus = Notestatus.objects.order_by('notestatus_name')[0].notestatus_id

        if 'system' in request.GET:
            system = request.GET['system']
            form = self.form_class(
                initial={
                    'notestatus': notestatus,
                    'system': system,
                }
            )
        else:
            form = self.form_class(
                initial={
                    'notestatus': notestatus,
                }
            )
        debug_logger(str(request.user), " REPORTITEM_ADD_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Add',
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            reportitem = form.save(commit=False)
            reportitem.reportitem_created_by_user_id = request.user
            reportitem.reportitem_modified_by_user_id = request.user
            reportitem.save()
            form.save_m2m()
            reportitem.logger(str(request.user), " REPORTITEM_ADD_EXECUTED")
            messages.success(request, 'Reportitem added')
            if 'documentation' in request.GET:
                return redirect(
                    reverse('documentation_list')
                    + f'#reportitem_id_{reportitem.reportitem_id}'
                )
            else:
                return redirect(
                    reverse('system_detail', args=(reportitem.system.system_id,))
                )
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Add',
                },
            )


class ReportitemUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Reportitem
    form_class = ReportitemForm
    template_name = 'dfirtrack_main/reportitem/reportitem_generic_form.html'

    def get(self, request, *args, **kwargs):
        reportitem = self.get_object()
        form = self.form_class(instance=reportitem)
        reportitem.logger(str(request.user), " REPORTITEM_EDIT_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Edit',
            },
        )

    def post(self, request, *args, **kwargs):
        reportitem = self.get_object()
        form = self.form_class(request.POST, instance=reportitem)
        if form.is_valid():
            reportitem = form.save(commit=False)
            reportitem.reportitem_modified_by_user_id = request.user
            reportitem.save()
            form.save_m2m()
            reportitem.logger(str(request.user), " REPORTITEM_EDIT_EXECUTED")
            messages.success(request, 'Reportitem edited')
            if 'documentation' in request.GET:
                return redirect(
                    reverse('documentation_list')
                    + f'#reportitem_id_{reportitem.reportitem_id}'
                )
            else:
                return redirect(
                    reverse('system_detail', args=(reportitem.system.system_id,))
                )
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Edit',
                },
            )
