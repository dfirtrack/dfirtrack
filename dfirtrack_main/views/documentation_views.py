from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from dfirtrack_main.filter_forms import DocumentationFilterForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Note
from dfirtrack_main.models import Reportitem
from urllib.parse import urlencode, urlunparse


class DocumentationList(LoginRequiredMixin, FormView):
    login_url = '/login'
    form_class = DocumentationFilterForm
    template_name = 'dfirtrack_main/documentation/documentation_list.html'

    def get_context_data(self, **kwargs):
        """ filter objects according to GET parameters """

        # get context
        context = super().get_context_data(**kwargs)

        # initial query with desired ordering
        note_query = Note.objects.order_by('note_title')
        reportitem_query = Reportitem.objects.order_by('system__system_name', 'headline__headline_name')

        # create dict to initialize form values set by filtering in previous view
        form_initial = {}

        # filter for case
        if 'case' in self.request.GET:
            # get id
            case_id = self.request.GET['case']
            # filter objects
            note_query = note_query.filter(case=case_id)
            reportitem_query = reportitem_query.filter(case=case_id)
            # remember initial value for form
            form_initial['case'] = case_id

        # filter for notestatus
        if 'notestatus' in self.request.GET:
            # get id
            notestatus_id = self.request.GET['notestatus']
            # filter objects
            note_query = note_query.filter(notestatus=notestatus_id)
            reportitem_query = reportitem_query.filter(notestatus=notestatus_id)
            # remember initial value for form
            form_initial['notestatus'] = notestatus_id

        # filter for tag
        if 'tag' in self.request.GET:
            # get id
            tag_id = self.request.GET['tag']
            # filter objects
            note_query = note_query.filter(tag=tag_id)
            reportitem_query = reportitem_query.filter(tag=tag_id)
            # remember initial value for form
            form_initial['tag'] = tag_id

        # add to context
        context['note_list'] = note_query
        context['reportitem_list'] = reportitem_query

        # add to context
        context['form'] = self.form_class(initial = form_initial)

        # call logger
        debug_logger(str(self.request.user), " DOCUMENTATION_LIST_ENTERED")

        # return objects to template
        return context

    def form_valid(self, form):
        """ evaluate form data and call view again with GET parameters """

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
        return redirect(documentation_list_query, form)
