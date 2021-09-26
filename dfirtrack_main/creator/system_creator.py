from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django_q.tasks import async_task

from dfirtrack_config.models import Workflow
from dfirtrack_main.async_messages.system_messages import final_messages
from dfirtrack_main.forms import SystemCreatorForm
from dfirtrack_main.logger.default_logger import (
    debug_logger,
    info_logger,
    warning_logger,
)
from dfirtrack_main.models import Analysisstatus, System, Systemstatus


@login_required(login_url="/login")
def system_creator(request):
    """ function to create many systems at once (helper function to call the real function) """

    # form was valid to post
    if request.method == "POST":

        # get objects from request object
        request_post = request.POST
        request_user = request.user

        # show immediate message for user
        messages.success(request, 'System creator started')

        # call async function
        async_task(
            "dfirtrack_main.creator.system_creator.system_creator_async",
            request_post,
            request_user,
        )

        # return directly to system list
        return redirect(reverse('system_list'))

    # show empty form
    else:

        # get id of first status objects sorted by name
        systemstatus = Systemstatus.objects.order_by('systemstatus_name')[0].systemstatus_id
        analysisstatus = Analysisstatus.objects.order_by('analysisstatus_name')[0].analysisstatus_id

        # get all workflows
        workflows = Workflow.objects.all()

        # show empty form with default values for convenience and speed reasons
        form = SystemCreatorForm(initial={
            'systemstatus': systemstatus,
            'analysisstatus': analysisstatus,
        })

        # call logger
        debug_logger(str(request.user), ' SYSTEM_CREATOR_ENTERED')

    return render(request, 'dfirtrack_main/system/system_creator.html', {'form': form, 'workflows': workflows})

def system_creator_async(request_post, request_user):
    """ function to create many systems at once """

    # call logger
    debug_logger(str(request_user), ' SYSTEM_CREATOR_START')

    # extract lines from systemlist (list results from request object via large text area)
    lines = request_post.get('systemlist').splitlines()

    #  count lines (needed for messages)
    number_of_lines = len(lines)

    # set systems_created_counter (needed for messages)
    systems_created_counter = 0

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
            warning_logger(str(request_user), ' SYSTEM_CREATOR_ROW_EMPTY')
            continue

        # check line for length of string
        if len(line) > 50:
            # autoincrement counter
            lines_faulty_counter += 1
            # call logger
            warning_logger(str(request_user), ' SYSTEM_CREATOR_LONG_STRING')
            continue

        # check for existence of system
        system = System.objects.filter(system_name = line)

        """ already existing system """

        # in case of existing system
        if system.count() > 0:
            # autoincrement counter
            systems_skipped_counter += 1
            # add system name to list of skipped systems
            skipped_systems.append(line)
            # call logger
            warning_logger(str(request_user), f' SYSTEM_CREATOR_SYSTEM_EXISTS system_name:{line}')
            # leave this loop because system with this systemname already exists
            continue

        """ new system """

        # create form with request data
        form = SystemCreatorForm(request_post)

        # create system
        if form.is_valid():

            """ object creation """

            # don't save form yet
            system = form.save(commit=False)

            # set system_name
            system.system_name = line

            # set auto values
            system.system_created_by_user_id = request_user
            system.system_modified_by_user_id = request_user

            # save object
            system.save()

            # save manytomany
            form.save_m2m()

            """ object counter / log """

            # autoincrement counter
            systems_created_counter  += 1

            # call logger
            system.logger(str(request_user), ' SYSTEM_CREATOR_EXECUTED')

            # apply workflows
            if workflows:
                error_code = Workflow.apply(workflows, system, request_user)
                if error_code:
                    system.logger(str(request_user), ' COULD_NOT_APPLY_WORKFLOW')
                else:
                    workflows_applied += workflow_count

    """ finish system creator """

    # call final messages
    final_messages(systems_created_counter, systems_skipped_counter, lines_faulty_counter, skipped_systems, number_of_lines, request_user, workflow_count, workflows_applied)

    # call logger
    info_logger(
        str(request_user),
        f' SYSTEM_CREATOR_STATUS'
        f' created:{systems_created_counter}'
        f'|skipped:{systems_skipped_counter}'
        f'|faulty_lines:{lines_faulty_counter}'
        f'|workflows_applied:{workflows_applied}'
    )

    # call logger
    debug_logger(str(request_user), ' SYSTEM_CREATOR_END')
