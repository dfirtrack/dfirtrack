from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from dfirtrack_artifacts.models import Artifacttype
from dfirtrack_artifacts.forms import ArtifacttypeForm
from dfirtrack_main.logger.default_logger import debug_logger

class ArtifacttypeListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Artifacttype
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_list.html'
    context_object_name = 'artifacttype_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " ARTIFACTTYPE_LIST_ENTERED")
        return Artifacttype.objects.order_by('artifacttype_name')

class ArtifacttypeDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Artifacttype
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_detail.html'

    # TODO: does not work as expected (and in contrast to dfirtrack_main.views)
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    artifacttype = self.object
    #    artifacttype.logger(str(self.request.user), " ARTIFACTTYPE_DETAIL_ENTERED")
    #    return context

class ArtifacttypeCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Artifacttype
    form_class = ArtifacttypeForm
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_add.html'

class ArtifacttypeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Artifacttype
    form_class = ArtifacttypeForm
    template_name = 'dfirtrack_artifacts/artifacttype/artifacttype_edit.html'
