from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.filter_forms import DocumentationFilterForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case
from dfirtrack_main.models import Note
from dfirtrack_main.models import Notestatus
from dfirtrack_main.models import Reportitem
from dfirtrack_main.models import Tag
from urllib.parse import urlencode, urlunparse


class DocumentationList(LoginRequiredMixin, FormView):
    login_url = '/login'
    form_class = DocumentationFilterForm
    template_name = 'dfirtrack_main/documentation/documentation_list.html'

    def get_context_data(self, **kwargs):
        """ filter objects according to GET parameters """

        # get context
        context = super().get_context_data(**kwargs)

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(user_config_username=self.request.user)

        # initial query with desired ordering
        note_query = Note.objects.order_by('note_title')
        reportitem_query = Reportitem.objects.order_by('system__system_name', 'headline__headline_name')

        # create dict to initialize form values set by filtering in previous view
        form_initial = {}

        # check box if persistence option was provided
        if user_config.filter_documentation_list_keep:
            # set initial value for form
            form_initial['filter_documentation_list_keep'] = True
        else:
            form_initial['filter_documentation_list_keep'] = False

        # get case from config
        if user_config.filter_documentation_list_case:
            # get id
            case_id = user_config.filter_documentation_list_case.case_id
            # filter objects
            note_query = note_query.filter(case=case_id)
            reportitem_query = reportitem_query.filter(case=case_id)
            # set initial value for form
            form_initial['case'] = case_id

        # get notestatus from config
        if user_config.filter_documentation_list_notestatus:
            # get id
            notestatus_id = user_config.filter_documentation_list_notestatus.notestatus_id
            # filter objects
            note_query = note_query.filter(notestatus=notestatus_id)
            reportitem_query = reportitem_query.filter(notestatus=notestatus_id)
            # set initial value for form
            form_initial['notestatus'] = notestatus_id

        # get tag from config
        if user_config.filter_documentation_list_tag:
            # get id
            tag_id = user_config.filter_documentation_list_tag.tag_id
            # filter objects
            note_query = note_query.filter(tag=tag_id)
            reportitem_query = reportitem_query.filter(tag=tag_id)
            # set initial value for form
            form_initial['tag'] = tag_id

        # add to context
        context['note_list'] = note_query
        context['reportitem_list'] = reportitem_query

        # add to context
        context['form'] = self.form_class(initial = form_initial)

        # filter: clean filtering after providing filter results if persistence option was not selected
        if not user_config.filter_documentation_list_keep:
            # unset filter case
            user_config.filter_documentation_list_case = None
            # unset filter notestatus
            user_config.filter_documentation_list_notestatus = None
            # unset filter tag
            user_config.filter_documentation_list_tag = None
            # save config
            user_config.save()

        # call logger
        debug_logger(str(self.request.user), " DOCUMENTATION_LIST_ENTERED")

        # return objects to template
        return context

    def form_valid(self, form):
        """ save form data to config and call view again """

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(user_config_username=self.request.user)

# TODO: [test] form does not seem to be valid at all if object is not available (any more)

        # filter: save filter choices from form in 'documentation_list' to database and call 'documentation_list' again with the new filter options

        # get case from form and save to config
        if form.data['case']:
            try:
                documentation_list_case = Case.objects.get(case_id=form.data['case'])
                user_config.filter_documentation_list_case = documentation_list_case
            except Case.DoesNotExist:
                user_config.filter_documentation_list_case = None
                messages.warning(self.request, 'Case used for filtering does not exist.')
        else:
            user_config.filter_documentation_list_case = None

        # get notestatus from form and save to config
        if form.data['notestatus']:
            try:
                documentation_list_notestatus = Notestatus.objects.get(notestatus_id=form.data['notestatus'])
                user_config.filter_documentation_list_notestatus = documentation_list_notestatus
            except Notestatus.DoesNotExist:
                user_config.filter_documentation_list_notestatus = None
                messages.warning(self.request, 'Notestatus used for filtering does not exist.')
        else:
            user_config.filter_documentation_list_notestatus = None

        # get tag from form and save to config
        if form.data['tag']:
            try:
                documentation_list_tag = Tag.objects.get(tag_id=form.data['tag'])
                user_config.filter_documentation_list_tag = documentation_list_tag
            except Tag.DoesNotExist:
                user_config.filter_documentation_list_tag = None
                messages.warning(self.request, 'Tag used for filtering does not exist.')
        else:
            user_config.filter_documentation_list_tag = None

        # avoid MultiValueDictKeyError by providing default False if checkbox was empty
        if form.data.get('filter_documentation_list_keep', False):
            user_config.filter_documentation_list_keep = True
        else:
            user_config.filter_documentation_list_keep = False

        # save config
        user_config.save()

        # call view again
        return redirect(reverse('documentation_list'))

@login_required(login_url="/login")
def clear_documentation_list_filter(request):
    """ clear documentation list filter """

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(user_config_username=request.user)

    # clear values
    user_config.filter_documentation_list_case = None
    user_config.filter_documentation_list_notestatus = None
    user_config.filter_documentation_list_tag = None

    # save config
    user_config.save()

    return redirect(reverse('documentation_list'))
