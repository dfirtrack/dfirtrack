from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django_q.tasks import async_task
from dfirtrack_main.async_messages import message_user
from dfirtrack_main.forms import SystemModificatorForm
from dfirtrack_main.logger.default_logger import debug_logger, error_logger, info_logger, warning_logger
from dfirtrack_main.models import System, Tag, Company


@login_required(login_url="/login")
def system_modificator(request):
    """ function to modify many systems at once (helper function to call the real function) """

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
        show_systemlist = bool(int(request.GET.get('systemlist', 0)))
        form = SystemModificatorForm(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        }, use_system_charfield = show_systemlist)

        # call logger
        debug_logger(str(request.user), ' SYSTEM_MODIFICATOR_ENTERED')

    return render(request, 'dfirtrack_main/system/system_modificator.html', {'form': form})

def system_modificator_async(request_post, request_user):
    """ function to modify many systems at once """

    # call logger
    debug_logger(str(request_user), ' SYSTEM_MODIFICATOR_BEGIN')

    # exctract lines from systemlist (list results either from request object via multiline selector or via large text area)
    lines = request_post.getlist('systemlist')
    system_char_field_used = False
    # if large text area was used, the list contains only one entry with (one or more) line breaks
    if len(lines) == 1 and ("\r\n" in lines[0] or not lines[0].isdigit()):
        system_char_field_used = True
        lines=lines[0].splitlines()

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

    # iterate over lines
    for line in lines:

        # skip emtpy lines
        if line == '':
            # autoincrement counter
            lines_faulty_counter += 1
            # call logger
            warning_logger(str(request_user), ' SYSTEM_MODIFICATOR_ROW_EMPTY')
            continue

        # check line for string
        if not isinstance(line, str):   # coverage: ignore branch
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
            system = System.objects.filter(system_name = line)
        else:
            system = System.objects.filter(system_id = line)

        """ handling non-existing or non-unique systems 2 """

        # system does not exist
        if system.count() == 0:
            # autoincrement counter
            systems_skipped_counter += 1
            # add system name to list of skipped systems
            skipped_systems.append(line)
            # call logger
            error_logger(str(request_user), ' SYSTEM_MODIFICATOR_SYSTEM_DOES_NOT_EXISTS ' + 'system_id/system_name:' + line)
            # leave this loop because system with this systemname does not exist
            continue
        # more than one system exists
        elif system.count() > 1:
            # autoincrement counter
            systems_skipped_counter += 1
            # add system name to list of skipped systems
            skipped_systems.append(line)
            # call logger
            error_logger(str(request_user), ' SYSTEM_MODIFICATOR_SYSTEM_NOT_DISTINCT ' + 'system_id/system_name:' + line)
            # leave this loop because system with this systemname is not distinct
            continue

        # get existing system
        if system_char_field_used:
            system = System.objects.get(system_name = line)
        else:
            system = System.objects.get(system_id = line)

        """ new system """

        # create form with request data
        form = SystemModificatorForm(request_post, instance = system, use_system_charfield = system_char_field_used)

        # extract tags (list results from request object via multiple choice field)
        tags = request_post.getlist('tag')

        # extract companies (list results from request object via multiple choice field)
        companies = request_post.getlist('company')

        # modify system
        if form.is_valid():

            """ object modification """

            # don't save form yet
            system = form.save(commit=False)

            # set auto values
            system.system_modified_by_user_id = request_user
            system.system_modify_time = timezone.now()

            # save object
            system.save()

            """ object counter / log """

            # autoincrement counter
            systems_modified_counter  += 1

            # call logger
            system.logger(str(request_user), ' SYSTEM_MODIFICATOR_EXECUTED')

            """ many 2 many """

            # TODO: add check for empty list
            # add tags (using save_m2m would replace existing tags)
            for tag_id in tags:
                # get object
                tag = Tag.objects.get(tag_id=tag_id)
                # add tag to system
                system.tag.add(tag)

            for company_id in companies:
                # get object
                company = Company.objects.get(company_id=company_id)
                # add company to system
                system.company.add(company)

    """ call final messages """

    # finish message
    message_user(request_user, 'System modificator finished', constants.SUCCESS)

    # number messages

    if systems_modified_counter > 0:
        if systems_modified_counter  == 1:
            message_user(request_user, str(systems_modified_counter) + ' system was modified.', constants.SUCCESS)
        else:
            message_user(request_user, str(systems_modified_counter) + ' systems were modified.', constants.SUCCESS)

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
    info_logger(str(request_user), ' SYSTEM_MODIFICATOR_STATUS ' + 'modified:' + str(systems_modified_counter) + '|' + 'skipped:' + str(systems_skipped_counter) + '|' + 'faulty_lines:' + str(lines_faulty_counter))

    # call logger
    debug_logger(str(request_user), " SYSTEM_MODIFICATOR_END")
