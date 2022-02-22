from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.filter_forms import DocumentationFilterForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Case, Note, Notestatus, Reportitem, Tag


class DocumentationList(LoginRequiredMixin, FormView):
    login_url = '/login'
    form_class = DocumentationFilterForm
    template_name = 'dfirtrack_main/documentation/documentation_list.html'

    def get_context_data(self, **kwargs):
        """filter objects according to GET parameters"""

        """prologue"""

        # get context
        context = super().get_context_data(**kwargs)

        # get config
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=self.request.user
        )

        """form preparation / filter"""

        # initialize filter flag (needed for messages)
        filter_flag = False

        # initial query with desired ordering
        note_query = Note.objects.order_by('note_title')
        reportitem_query = Reportitem.objects.order_by(
            'system__system_name', 'headline__headline_name'
        )

        # get case from config
        if user_config.filter_documentation_list_case:
            # get id
            case_id = user_config.filter_documentation_list_case.case_id
            # filter objects
            note_query = note_query.filter(case=case_id)
            reportitem_query = reportitem_query.filter(case=case_id)
            # set filter flag
            filter_flag = True
            

        # get notestatus from config
        if user_config.filter_documentation_list_notestatus:
            # get id
            notestatus_id = (
                user_config.filter_documentation_list_notestatus.notestatus_id
            )
            # filter objects
            note_query = note_query.filter(notestatus=notestatus_id)
            reportitem_query = reportitem_query.filter(notestatus=notestatus_id)
            # set filter flag
            filter_flag = True            

        # get tag from config
        if user_config.filter_documentation_list_tag:
            # get id
            tag_id = user_config.filter_documentation_list_tag.tag_id
            # filter objects
            note_query = note_query.filter(tag=tag_id)
            reportitem_query = reportitem_query.filter(tag=tag_id)
            # set filter flag
            filter_flag = True            

        # add to context
        context['note_list'] = note_query
        context['reportitem_list'] = reportitem_query

        # add to context
        context['form'] = self.form_class(instance=user_config)

        # call logger
        debug_logger(str(self.request.user), " DOCUMENTATION_LIST_ENTERED")

        # info message that filter is active (not for user filtering)
        if filter_flag:
            messages.info(self.request, 'Filter is active. Items might be incomplete.')

        # return objects to template
        return context

    def post(self, request, *args, **kwargs):
        """save form data to config and call view again"""
        user_config, created = UserConfigModel.objects.get_or_create(
            user_config_username=request.POST.get('user_config_username')
        )

        form = self.form_class(request.POST, instance=user_config)

        if form.is_valid():
            user_config = form.save(commit=False)
            user_config.save()
            form.save_m2m()

        # call view again
        return redirect(reverse('documentation_list'))


@login_required(login_url="/login")
def clear_documentation_list_filter(request):
    """clear documentation list filter"""

    # get config
    user_config, created = UserConfigModel.objects.get_or_create(
        user_config_username=request.user
    )

    # clear values
    user_config.filter_documentation_list_case = None
    user_config.filter_documentation_list_notestatus = None
    user_config.filter_documentation_list_tag = None

    # save config
    user_config.save()

    return redirect(reverse('documentation_list'))
