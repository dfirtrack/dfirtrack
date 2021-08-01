from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Casepriority


class CasepriorityList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Casepriority
    template_name = 'dfirtrack_main/casepriority/casepriority_list.html'
    context_object_name = 'casepriority_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), ' CASEPRIORITY_LIST_ENTERED')
        return Casepriority.objects.order_by('casepriority_name')


class CasepriorityDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Casepriority
    template_name = 'dfirtrack_main/casepriority/casepriority_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        casepriority = self.object
        casepriority.logger(str(self.request.user), " CASEPRIORITY_DETAIL_ENTERED")
        return context
