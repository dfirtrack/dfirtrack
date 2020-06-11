from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django_q.tasks import async_task
from dfirtrack_main.forms import SystemCreatorForm
from dfirtrack_main.logger.default_logger import debug_logger, error_logger, warning_logger
from dfirtrack_main.models import System

@login_required(login_url="/login")
def system_creator(request):
    """ function to create many systems at once (helper function to call the real function) """

    # form was valid to post
    if request.method == "POST":
        request_post = request.POST
        request_user = request.user

        # call async function
        async_task(
            "dfirtrack_main.creator.system_creator.system_creator_async",
            request_post,
            request_user,
        )

        return redirect(reverse('system_list'))

    # show empty form
    else:
        form = SystemCreatorForm(initial={
            'systemstatus': 2,
            'analysisstatus': 1,
        })

    # call logger
    debug_logger(str(request.user), " SYSTEM_CREATOR_ENTERED")
    return render(request, 'dfirtrack_main/system/system_creator.html', {'form': form})

def system_creator_async(request_post, request_user):
    """ function to create many systems at once """

    # call logger
    debug_logger(str(request_user), " SYSTEM_CREATOR_BEGIN")

    # exctract lines from systemlist (list results from request object via large text area)
    lines = request_post.get('systemlist').splitlines()

    # iterate over lines
    for line in lines:

        # skip emtpy lines
        if line == '':
            warning_logger(str(request_user), " SYSTEM_CREATOR_ROW_EMPTY")
            continue

        # check line for string
        if not isinstance(line, str):
            warning_logger(str(request_user), " SYSTEM_CREATOR_NO_STRING")
            continue

        # check line for length of string
        if len(line) > 50:
            warning_logger(str(request_user), " SYSTEM_CREATOR_LONG_STRING")
            continue

        # check for existence of system
        system = System.objects.filter(system_name = line)
        if system.count() > 0:
            # call logger
            error_logger(str(request_user), " SYSTEM_CREATOR_SYSTEM_EXISTS " + "system_name:" + line)
            # leave this loop because system with this systemname already exists
            continue

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

            # call logger
            system.logger(str(request_user), ' SYSTEM_CREATOR_EXECUTED')

    # call logger
    debug_logger(str(request_user), " SYSTEM_CREATOR_END")
