from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django_q.tasks import async_task

from dfirtrack_artifacts.models import Artifactpriority, Artifactstatus, Artifacttype
from dfirtrack_artifacts.forms import ArtifactCreatorForm
from dfirtrack_main.async_messages import message_user
from dfirtrack_main.logger.default_logger import debug_logger, info_logger
from dfirtrack_main.models import Case, System, Tag


@login_required(login_url="/login")
def artifact_creator(request):
    """ function to create many artifacts for many systems at once (helper function to call the real function) """

    # form was valid to post
    if request.method == 'POST':

        # get form
        form = ArtifactCreatorForm(request.POST)

        # form was valid
        if form.is_valid():

            # get objects from request object
            request_post = request.POST
            request_user = request.user

            # show immediate message for user
            messages.success(request, 'Artifact creator started')

            # call async function
            async_task(
                "dfirtrack_artifacts.creator.artifact_creator.artifact_creator_async",
                request_post,
                request_user,
            )

            # return directly to artifact list
            return redirect(reverse('artifacts_artifact_list'))

    # show empty form
    else:

        # get id of first status objects sorted by name
        artifactpriority = Artifactpriority.objects.order_by('artifactpriority_name')[0].artifactpriority_id
        artifactstatus = Artifactstatus.objects.order_by('artifactstatus_name')[0].artifactstatus_id

        form = ArtifactCreatorForm(initial={
            'artifactpriority': artifactpriority,
            'artifactstatus': artifactstatus,
        })

        # call logger
        debug_logger(str(request.user), ' ARTIFACT_CREATOR_ENTERED')

    return render(request, 'dfirtrack_artifacts/artifact/artifact_creator.html', {'form': form})

def artifact_creator_async(request_post, request_user):
    """ function to create many artifacts for many systems at once """

    # call logger
    debug_logger(str(request_user), ' ARTIFACT_CREATOR_START')

    # extract artifacttypes (list results from request object via multiple choice field)
    artifacttypes = request_post.getlist('artifacttype')

    # extract systems (list results from request object via multiple choice field)
    systems = request_post.getlist('system')

    # set artifacts_created_counter (needed for messages)
    artifacts_created_counter = 0

    # set system_artifacts_created_counter (needed for messages)
    system_artifacts_created_counter = 0

    # iterate over systems
    for system in systems:

        # autoincrement counter
        system_artifacts_created_counter  += 1

        # iterate over artifacttypes
        for artifacttype in artifacttypes:

            # create form with request data
            form = ArtifactCreatorForm(request_post)

            # create artifact
            if form.is_valid():

                """ object creation """

                # don't save form yet
                artifact = form.save(commit=False)

                # set artifacttype and system
                artifact.artifacttype = Artifacttype.objects.get(artifacttype_id=artifacttype)
                artifact.system = System.objects.get(system_id=system)

                # set auto values
                artifact.artifact_created_by_user_id = request_user
                artifact.artifact_modified_by_user_id = request_user

#                # get taskstatus objects for comparing
#                taskstatus_working = Taskstatus.objects.get(taskstatus_name='20_working')
#                taskstatus_done = Taskstatus.objects.get(taskstatus_name='30_done')
#
#                # set times depending on submitted taskstatus
#                if task.taskstatus == taskstatus_working:
#                    task.task_started_time = timezone.now()
#                if task.taskstatus == taskstatus_done:
#                    task.task_started_time = timezone.now()
#                    task.task_finished_time = timezone.now()

                # save object
                artifact.save()

                # save manytomany
                form.save_m2m()

                """ object counter / log """

                # autoincrement counter
                artifacts_created_counter  += 1

                # call logger
                artifact.logger( str(request_user), ' ARTIFACT_CREATOR_EXECUTED')

    """ finish artifact creator """

    # call final message
    message_user(
        request_user,
        f'{artifacts_created_counter} artifacts created for {system_artifacts_created_counter} systems.',
        constants.SUCCESS
    )

    # call logger
    info_logger(
        str(request_user),
        f' ARTIFACT_CREATOR_STATUS'
        f' artifacts_created:{artifacts_created_counter}'
        f'|systems_affected:{system_artifacts_created_counter}'
    )

    # call logger
    debug_logger(str(request_user), ' ARTIFACT_CREATOR_END')
