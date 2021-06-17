from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Note
from dfirtrack_main.models import Reportitem


class DocumentationList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Reportitem
    template_name = 'dfirtrack_main/documentation/documentation_list.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        return Note.objects.order_by('note_title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        debug_logger(str(self.request.user), " DOCUMENTATION_LIST_ENTERED")
        context['reportitem_list'] = Reportitem.objects.order_by('system__system_name', 'headline__headline_name')
        return context
