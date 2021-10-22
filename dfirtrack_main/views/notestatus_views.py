from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Notestatus


class NotestatusList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Notestatus
    template_name = 'dfirtrack_main/notestatus/notestatus_list.html'
    context_object_name = 'notestatus_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " NOTESTATUS_ENTERED")
        return Notestatus.objects.order_by('notestatus_name')


class NotestatusDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Notestatus
    template_name = 'dfirtrack_main/notestatus/notestatus_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notestatus = self.object
        notestatus.logger(str(self.request.user), " NOTESTATUSDETAIL_ENTERED")
        return context
