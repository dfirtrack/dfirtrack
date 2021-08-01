from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.urls import reverse
from django_q.tasks import async_task

from dfirtrack_main.async_messages import message_user
from dfirtrack_main.forms import CaseCreatorForm
from dfirtrack_main.logger.default_logger import debug_logger, info_logger
from dfirtrack_main.models import Case, System


@login_required(login_url="/login")
def case_creator(request):
    """function to assign many cases to systems and vice versa (helper function to call the real function)"""

    # form was valid to post
    if request.method == "POST":

        # get form
        form = CaseCreatorForm(request.POST)

        # form was valid
        if form.is_valid():

            # get objects from request object
            request_post = request.POST
            request_user = request.user

            # show immediate message for user
            messages.success(request, "Case creator started")

            # call async function
            async_task(
                "dfirtrack_main.creator.case_creator.case_creator_async",
                request_post,
                request_user,
            )

            # return directly to case list
            return redirect(reverse("case_list"))

    # show empty form
    else:
        form = CaseCreatorForm()

        # call logger
        debug_logger(str(request.user), " CASE_CREATOR_ENTERED")

    return render(request, "dfirtrack_main/case/case_creator.html", {"form": form})


def case_creator_async(request_post, request_user):
    """function to assign many cases to systems and vice versa"""

    # call logger
    debug_logger(str(request_user), " CASE_CREATOR_START")

    # extract cases (list results from request object via multiple choice field)
    cases = request_post.getlist("case")

    # extract systems (list results from request object via multiple choice field)
    systems = request_post.getlist("system")

    # set cases_affected_counter (needed for messages)
    cases_affected_counter = 0

    # set systems_affected_counter (needed for messages)
    systems_affected_counter = 0

    # iterate over systems
    for system_id in systems:

        # autoincrement counter
        systems_affected_counter += 1

        # iterate over cases
        for case_id in cases:

            # create form with request data
            form = CaseCreatorForm(request_post)

            # create relation
            if form.is_valid():

                """object creation"""

                # get objects
                system = System.objects.get(system_id=system_id)
                case = Case.objects.get(case_id=case_id)

                # add case to system
                system.case.add(case)

                """ object counter / log """

                # autoincrement counter
                cases_affected_counter += 1

                # call logger
                system.logger(str(request_user), " CASE_CREATOR_EXECUTED")

    """ finish case importer """

    # fix case number (other meaning than with tag creator
    cases_affected_counter = int(cases_affected_counter / systems_affected_counter)

    # call final message
    message_user(
        request_user,
        f"{cases_affected_counter} cases assigned to {systems_affected_counter} systems.",
        constants.SUCCESS,
    )

    # call logger
    info_logger(
        str(request_user),
        f" CASE_CREATOR_STATUS"
        f" cases_affected:{cases_affected_counter}"
        f"|systems_affected:{systems_affected_counter}",
    )

    # call logger
    debug_logger(str(request_user), " CASE_CREATOR_END")
