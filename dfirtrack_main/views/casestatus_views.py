from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Casestatus


class CasestatusList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Casestatus
    template_name = 'dfirtrack_main/casestatus/casestatus_list.html'
    context_object_name = 'casestatus_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), ' CASESTATUS_LIST_ENTERED')
        return Casestatus.objects.order_by('casestatus_name')


class CasestatusDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Casestatus
    template_name = 'dfirtrack_main/casestatus/casestatus_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        casestatus = self.object
        casestatus.logger(str(self.request.user), " CASESTATUS_DETAIL_ENTERED")
        return context
