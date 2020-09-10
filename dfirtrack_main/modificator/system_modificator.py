from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django_q.tasks import async_task
from dfirtrack_main.forms import SystemModificatorForm
from dfirtrack_main.logger.default_logger import debug_logger, error_logger, warning_logger
from dfirtrack_main.models import System, Tag

@login_required(login_url="/login")
def system_modificator(request):
    """ function to modify many systems at once (helper function to call the real function) """

    # form was valid to post
    if request.method == "POST":
        request_post = request.POST
        request_user = request.user

        # call async function
        async_task(
            "dfirtrack_main.modificator.system_modificator.system_modificator_async",
            request_post,
            request_user,
        )

        return redirect(reverse('system_list'))

    # show empty form
    else:
        form = SystemModificatorForm(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })

    # call logger
    debug_logger(str(request.user), " SYSTEM_MODIFICATOR_ENTERED")
    return render(request, 'dfirtrack_main/system/system_modificator.html', {'form': form})

def system_modificator_async(request_post, request_user):
    """ function to modify many systems at once """

    # call logger
    debug_logger(str(request_user), " SYSTEM_MODIFICATOR_BEGIN")

    # exctract lines from systemlist (list results from request object via large text area)
    lines = request_post.get('systemlist').splitlines()

    # iterate over lines
    for line in lines:

        # skip emtpy lines
        if line == '':
            warning_logger(str(request_user), " SYSTEM_MODIFICATOR_ROW_EMPTY")
            continue

        # check line for string
        if not isinstance(line, str):
            warning_logger(str(request_user), " SYSTEM_MODIFICATOR_NO_STRING")
            continue

        # check line for length of string
        if len(line) > 50:
            warning_logger(str(request_user), " SYSTEM_MODIFICATOR_LONG_STRING")
            continue

        # check for existence of system
        system = System.objects.filter(system_name = line)
        if system.count() == 0:
            # call logger
            error_logger(str(request_user), " SYSTEM_MODIFICATOR_SYSTEM_DOES_NOT_EXISTS " + "system_name:" + line)
            # leave this loop because system with this systemname does not exist
            continue
        elif system.count() > 1:
            # call logger
            error_logger(str(request_user), " SYSTEM_MODIFICATOR_SYSTEM_NOT_DISTINCT " + "system_name:" + line)
            # leave this loop because system with this systemname is not distinct
            continue

        # get existing system
        system = System.objects.get(system_name = line)

        # create form with request data
        form = SystemModificatorForm(request_post, instance = system)

        # extract tags (list results from request object via multiple choice field)
        tags = request_post.getlist('tag')

        # modify system
        if form.is_valid():

            # don't save form yet
            system = form.save(commit=False)

            # set system_name
            system.system_name = line

            # set auto values
            system.system_modified_by_user_id = request_user
            system.system_modify_time = timezone.now()

            # save object
            system.save()

            # call logger
            system.logger(str(request_user), ' SYSTEM_MODIFICATOR_EXECUTED')

            # TODO: add check for empty list
            # add tags (using save_m2m would replace existing tags)
            for tag_id in tags:
                # get object
                tag = Tag.objects.get(tag_id=tag_id)
                # add tag to system
                system.tag.add(tag)

    # call logger
    debug_logger(str(request_user), " SYSTEM_MODIFICATOR_END")
