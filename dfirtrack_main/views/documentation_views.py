from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from dfirtrack_main.filter_forms import DocumentationChoiceForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Note
from dfirtrack_main.models import Reportitem
from urllib.parse import urlencode, urlunparse


class DocumentationList(LoginRequiredMixin, FormView):
    login_url = '/login'
    form_class = DocumentationChoiceForm
    template_name = 'dfirtrack_main/documentation/documentation_list.html'

    def get_context_data(self, **kwargs):

        # get context
        context = super().get_context_data(**kwargs)

        """ query note """

        # initial query with desired ordering
        note_query = Note.objects.order_by('note_title')

        # filter for case
        if 'case' in self.request.GET:
            case_id = self.request.GET['case']
            note_query = note_query.filter(case=case_id)

        # filter for notestatus
        if 'notestatus' in self.request.GET:
            notestatus_id = self.request.GET['notestatus']
            note_query = note_query.filter(notestatus=notestatus_id)

        # filter for tag
        # TODO: filter for tag (m2m)

        # add to context
        context['note_list'] = note_query

        """ query reportitem """

        # initial query with desired ordering
        reportitem_query = Reportitem.objects.order_by('system__system_name', 'headline__headline_name')

        # filter for case
        # TODO: filter for case

        # filter for notestatus
        # TODO: filter for notestatus

        # add to context
        context['reportitem_list'] = reportitem_query

        # call logger
        debug_logger(str(self.request.user), " DOCUMENTATION_LIST_ENTERED")

        # return objects to template
        return context

    def form_valid(self, form):

        # create parameter dict
        params = {}

        # case
        if form.data['case']:
            params['case'] = form.data['case']

        # notestatus
        if form.data['notestatus']:
            params['notestatus'] = form.data['notestatus']

        # tag
        if form.data['tag']:
            params['tag'] = form.data['tag']

        # build url
        urlpath = reverse('documentation_list')
        urlquery = urlencode(params)
        documentation_list_query = urlunparse(('','',urlpath,'',urlquery,''))

        # call view with queries
        return redirect(documentation_list_query)
