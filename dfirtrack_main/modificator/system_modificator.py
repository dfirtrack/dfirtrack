from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django_q.tasks import async_task

from dfirtrack_config.models import Workflow
from dfirtrack_main.async_messages.system_messages import final_messages
from dfirtrack_main.forms import SystemModificatorForm
from dfirtrack_main.logger.default_logger import (
    debug_logger,
    info_logger,
    warning_logger,
)
from dfirtrack_main.models import (
    Analysisstatus,
    Company,
    Contact,
    Location,
    Serviceprovider,
    System,
    Systemstatus,
    Tag,
)


@login_required(login_url="/login")
def system_modificator(request):
    """function to modify many systems at once (helper function to call the real function)"""

    # form was valid to post
    if request.method == "POST":

        # get objects from request object
        request_post = request.POST
        request_user = request.user

        # show immediate message for user
        messages.success(request, 'System modificator started')

        # call async function
        async_task(
            "dfirtrack_main.modificator.system_modificator.system_modificator_async",
            request_post,
            request_user,
        )

        # return directly to system list
        return redirect(reverse('system_list'))

    # show empty form
    else:

        # get id of first status objects sorted by name
        systemstatus = Systemstatus.objects.order_by('systemstatus_name')[
            0
        ].systemstatus_id
        analysisstatus = Analysisstatus.objects.order_by('analysisstatus_name')[
            0
        ].analysisstatus_id

        show_systemlist = bool(int(request.GET.get('systemlist', 0)))

        # workflows
        workflows = Workflow.objects.all()

        # show empty form with default values for convenience and speed reasons
        form = SystemModificatorForm(
            initial={
                'systemstatus': systemstatus,
                'analysisstatus': analysisstatus,
                'company_delete': 'keep_not_add',
                'tag_delete': 'keep_not_add',
                'contact_delete': 'keep_existing',
                'location_delete': 'keep_existing',
                'serviceprovider_delete': 'keep_existing',
            },
            use_system_charfield=show_systemlist,
        )

        # call logger
        debug_logger(str(request.user), ' SYSTEM_MODIFICATOR_ENTERED')

    return render(
        request,
        'dfirtrack_main/system/system_modificator.html',
        {'form': form, 'workflows': workflows},
    )


def system_modificator_async(request_post, request_user):
    """function to modify many systems at once"""

    # call logger
    debug_logger(str(request_user), ' SYSTEM_MODIFICATOR_START')

    # extract lines from systemlist (list results either from request object via multiline selector or via large text area)
    lines = request_post.getlist('systemlist')
    system_char_field_used = False
    # if large text area was used, the list contains only one entry with (one or more) line breaks
    if len(lines) == 1 and ("\r\n" in lines[0] or not lines[0].isdigit()):
        system_char_field_used = True
        lines = lines[0].splitlines()

    """ prepare and start loop """

    #  count lines (needed for messages)
    number_of_lines = len(lines)

    # set systems_modified_counter (needed for messages)
    systems_modified_counter = 0

    # set systems_skipped_counter (needed for messages)
    systems_skipped_counter = 0

    # set lines_faulty_counter (needed for messages)
    lines_faulty_counter = 0

    # create empty list (needed for messages)
    skipped_systems = []

    # workflows to apply
    workflows = request_post.getlist("workflow")

    # set workflows_applied (needed for messages)
    if workflows:
        workflow_count = len(workflows)
    else:
        workflow_count = 0
    workflows_applied = 0

    # iterate over lines
    for line in lines:

        # skip empty lines
        if line == '':
            # autoincrement counter
            lines_faulty_counter += 1
            # call logger
            warning_logger(str(request_user), ' SYSTEM_MODIFICATOR_ROW_EMPTY')
            continue

        # check line for string
        if not isinstance(line, str):  # coverage: ignore branch
            # autoincrement counter
            lines_faulty_counter += 1
            # call logger
            warning_logger(str(request_user), ' SYSTEM_MODIFICATOR_NO_STRING')
            continue

        # check line for length of string
        if len(line) > 50:
            # autoincrement counter
            lines_faulty_counter += 1
            # call logger
            warning_logger(str(request_user), ' SYSTEM_MODIFICATOR_LONG_STRING')
            continue

        # check for existence of system
        if system_char_field_used:
            system = System.objects.filter(system_name=line)
        else:
            system = System.objects.filter(system_id=line)

        """ handling non-existing (== 0) or non-unique (> 1) systems """

        # system does not exist
        if system.count() == 0:

            # autoincrement counter
            systems_skipped_counter += 1
            # add system name to list of skipped systems
            skipped_systems.append(line)
            # call logger
            warning_logger(
                str(request_user),
                f' SYSTEM_MODIFICATOR_SYSTEM_DOES_NOT_EXISTS system_id/system_name:{line}',
            )
            # leave this loop because system with this systemname does not exist
            continue

        # more than one system exists
        elif system.count() > 1:

            # autoincrement counter
            systems_skipped_counter += 1
            # add system name to list of skipped systems
            skipped_systems.append(line)
            # call logger
            warning_logger(
                str(request_user),
                f' SYSTEM_MODIFICATOR_SYSTEM_NOT_DISTINCT system_id/system_name:{line}',
            )
            # leave this loop because system with this systemname is not distinct
            continue

        """ unique system (== 1) """

        # get existing system
        if system_char_field_used:
            system = System.objects.get(system_name=line)
        else:
            system = System.objects.get(system_id=line)

        # create form with request data
        form = SystemModificatorForm(
            request_post, instance=system, use_system_charfield=system_char_field_used
        )

        # extract tags (list results from request object via multiple choice field)
        tags = request_post.getlist('tag')

        # extract companies (list results from request object via multiple choice field)
        companies = request_post.getlist('company')

        # TODO: [code] add condition for invalid form

        # modify system
        if form.is_valid():

            """object modification"""

            # don't save form yet
            system = form.save(commit=False)

            # set auto values
            system.system_modified_by_user_id = request_user

            """ fk non-model fields """

            # replace / delete, if 'switch_new / Switch to selected item or none' was selected
            if form['contact_delete'].value() == 'switch_new':

                # replace, if value was submitted via form
                if form['contact'].value():
                    contact_id = form['contact'].value()
                    contact = Contact.objects.get(contact_id=contact_id)
                    system.contact = contact
                # delete, if form field was empty
                else:
                    system.contact = None

            # replace / delete, if 'switch_new / Switch to selected item or none' was selected
            if form['location_delete'].value() == 'switch_new':

                # replace, if value was submitted via form
                if form['location'].value():
                    location_id = form['location'].value()
                    location = Location.objects.get(location_id=location_id)
                    system.location = location
                # delete, if form field was empty
                else:
                    system.location = None

            # replace / delete, if 'switch_new / Switch to selected item or none' was selected
            if form['serviceprovider_delete'].value() == 'switch_new':

                # replace, if value was submitted via form
                if form['serviceprovider'].value():
                    serviceprovider_id = form['serviceprovider'].value()
                    serviceprovider = Serviceprovider.objects.get(
                        serviceprovider_id=serviceprovider_id
                    )
                    system.serviceprovider = serviceprovider
                # delete, if form field was empty
                else:
                    system.serviceprovider = None

            # save object
            system.save()

            """ object counter / log """

            # autoincrement counter
            systems_modified_counter += 1

            # call logger
            system.logger(str(request_user), ' SYSTEM_MODIFICATOR_EXECUTED')

            """ many 2 many """

            # remove existing relations if 'remove_and_add / Delete existing and add new items' was selected
            if form['tag_delete'].value() == 'remove_and_add':

                # remove all m2m
                system.tag.clear()

            # add new relations if not 'keep_not_add / Do not change and keep existing' was selected
            if form['tag_delete'].value() != 'keep_not_add':

                # add new tags (using save_m2m would replace existing tags it there were any)
                for tag_id in tags:
                    # get object
                    tag = Tag.objects.get(tag_id=tag_id)
                    # add tag to system
                    system.tag.add(tag)

            # remove existing relations if 'remove_and_add / Delete existing and add new items' was selected
            if form['company_delete'].value() == 'remove_and_add':

                # remove all m2m
                system.company.clear()

            # add new relations if not 'keep_not_add / Do not change and keep existing' was selected
            if form['company_delete'].value() != 'keep_not_add':

                # add new companies (using save_m2m would replace existing companies it there were any)
                for company_id in companies:
                    # get object
                    company = Company.objects.get(company_id=company_id)
                    # add company to system
                    system.company.add(company)

            # apply workflows
            if workflows:
                error_code = Workflow.apply(workflows, system, request_user)
                if error_code:
                    system.logger(str(request_user), ' COULD_NOT_APPLY_WORKFLOW')
                else:
                    workflows_applied += workflow_count

    """ finish system modificator """

    # call final messages
    final_messages(
        systems_modified_counter,
        systems_skipped_counter,
        lines_faulty_counter,
        skipped_systems,
        number_of_lines,
        request_user,
        workflow_count,
        workflows_applied,
    )

    # call logger
    info_logger(
        str(request_user),
        f' SYSTEM_MODIFICATOR_STATUS'
        f' modified:{systems_modified_counter}'
        f'|skipped:{systems_skipped_counter}'
        f'|faulty_lines:{lines_faulty_counter}',
    )

    # call logger
    debug_logger(str(request_user), ' SYSTEM_MODIFICATOR_END')
