from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django_q.tasks import async_task
from dfirtrack_main.async_messages import message_user
from dfirtrack_main.forms import SystemCreatorForm
from dfirtrack_main.logger.default_logger import debug_logger, error_logger, info_logger, warning_logger
from dfirtrack_main.models import System


# TODO: test messages

@login_required(login_url="/login")
def system_creator(request):
    """ function to create many systems at once (helper function to call the real function) """

    # form was valid to post
    if request.method == "POST":

        # get objects from request object
        request_post = request.POST
        request_user = request.user

        # get time for messages
        creator_time = timezone.now().strftime('[%Y-%m-%d %H:%M:%S]')

        # create string for messages
        creator_time_string = 'System creator ' + creator_time + ' '

        # show immediate message for user
        messages.success(request, creator_time_string + 'started')

        # call async function
        async_task(
            "dfirtrack_main.creator.system_creator.system_creator_async",
            request_post,
            request_user,
            creator_time_string,
        )

        # return directly to system list
        return redirect(reverse('system_list'))

    # show empty form
    else:
        form = SystemCreatorForm(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })

        # call logger
        debug_logger(str(request.user), ' SYSTEM_CREATOR_ENTERED')

    return render(request, 'dfirtrack_main/system/system_creator.html', {'form': form})

def system_creator_async(request_post, request_user, creator_time_string):
    """ function to create many systems at once """

    # call logger
    debug_logger(str(request_user), ' SYSTEM_CREATOR_BEGIN')

    # exctract lines from systemlist (list results from request object via large text area)
    lines = request_post.get('systemlist').splitlines()

    #  count lines (needed for messages)
    number_of_lines = len(lines)

    # set lines faulty counter (needed for messages)
    lines_faulty_counter = 0

    # set systems_created_counter (needed for messages)
    systems_created_counter = 0

    # set systems_skipped_counter (needed for messages)
    systems_skipped_counter = 0

    # create empty list (needed for messages)
    skipped_systems = []

    # iterate over lines
    for line in lines:

        # skip emtpy lines
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
            error_logger(str(request_user), ' SYSTEM_CREATOR_SYSTEM_EXISTS ' + 'system_name:' + line)
            # leave this loop because system with this systemname already exists
            continue

        """ new system """

        # create form with request data
        form = SystemCreatorForm(request_post)

        # create system
        if form.is_valid():

            # don't save form yet
            system = form.save(commit=False)

            # set system_name
            system.system_name = line

            # set auto values
            system.system_created_by_user_id = request_user
            system.system_modified_by_user_id = request_user
            system.system_modify_time = timezone.now()

            # save object
            system.save()

            # save manytomany
            form.save_m2m()

            # autoincrement counter
            systems_created_counter  += 1

            # call logger
            system.logger(str(request_user), ' SYSTEM_CREATOR_EXECUTED')

    """ call final messages """

    # finish message
    message_user(request_user, creator_time_string + 'finished', constants.SUCCESS)

    if systems_created_counter > 0:
        if systems_created_counter  == 1:
            message_user(request_user, str(systems_created_counter) + ' system was created.', constants.SUCCESS)
        else:
            message_user(request_user, str(systems_created_counter) + ' systems were created.', constants.SUCCESS)

    if systems_skipped_counter > 0:
        if systems_skipped_counter  == 1:
            message_user(request_user, str(systems_skipped_counter) + ' system was skipped. ' + str(skipped_systems), constants.ERROR)
        else:
            message_user(request_user, str(systems_skipped_counter) + ' systems were skipped. ' + str(skipped_systems), constants.ERROR)

    if lines_faulty_counter > 0:
        if lines_faulty_counter  == 1:
            message_user(request_user, str(lines_faulty_counter) + ' line out of ' + str(number_of_lines) + ' lines was faulty (see log file for details).', constants.WARNING)
        else:
            message_user(request_user, str(lines_faulty_counter) + ' lines out of ' + str(number_of_lines) + ' lines were faulty (see log file for details).', constants.WARNING)

    # call logger
    info_logger(str(request_user), ' SYSTEM_CREATOR_STATUS ' + 'created:' + str(systems_created_counter) + '|' + 'skipped:' + str(systems_skipped_counter) + '|' + 'faulty_lines:' + str(lines_faulty_counter))

    # call logger
    debug_logger(str(request_user), ' SYSTEM_CREATOR_END')
