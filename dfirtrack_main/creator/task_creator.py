from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django_q.tasks import async_task
from dfirtrack_main.forms import TaskCreatorForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import System, Taskname, Taskstatus

@login_required(login_url="/login")
def task_creator(request):
    """ function to create many tasks for many systems at once (helper function to call the real function) """

    # form was valid to post
    if request.method == 'POST':
        request_post = request.POST
        request_user = request.user

        # call async function
        async_task(
            "dfirtrack_main.creator.task_creator.task_creator_async",
            request_post,
            request_user,
        )

        return redirect(reverse('task_list'))

    # show empty form
    else:
        form = TaskCreatorForm(initial={
            'taskpriority': 2,
            'taskstatus': 1,
        })

        # call logger
        debug_logger(str(request.user), " TASK_CREATOR_ENTERED")
    return render(request, 'dfirtrack_main/task/task_creator.html', {'form': form})

def task_creator_async(request_post, request_user):
    """ function to create many tasks for many systems at once """

    # call logger
    debug_logger(str(request_user), " TASK_CREATOR_BEGIN")

    # extract tasknames (list results from request object via multiple choice field)
    tasknames = request_post.getlist('taskname')

    # extract systems (list results from request object via multiple choice field)
    systems = request_post.getlist('system')

    # iterate over tasknames
    for taskname in tasknames:

        # iterate over systems
        for system in systems:

            # create form with request data
            form = TaskCreatorForm(request_post)

            # create task
            if form.is_valid():

                # dont't save form yet
                task = form.save(commit=False)

                # set taskname and system
                task.taskname = Taskname.objects.get(taskname_id=taskname)
                task.system = System.objects.get(system_id=system)

                # set auto values
                task.task_created_by_user_id = request_user
                task.task_modified_by_user_id = request_user

                # get taskstatus objects for comparing
                taskstatus_working = Taskstatus.objects.get(taskstatus_name='Working')
                taskstatus_done = Taskstatus.objects.get(taskstatus_name='Done')

                # set times depending on submitted taskstatus
                if task.taskstatus == taskstatus_working:
                    task.task_started_time = timezone.now()
                if task.taskstatus == taskstatus_done:
                    task.task_started_time = timezone.now()
                    task.task_finished_time = timezone.now()

                # save object
                task.save()

                # save manytomany
                form.save_m2m()

                tags = task.tag.all()
                taglist = []
                tagstring = 'None'
                for tag in tags:
                    taglist.append(tag.tag_name)
                    tagstring = ','.join(taglist)

                # call logger
                task.logger( str(request_user), " TASK_CREATOR_EXECUTED")

    # call logger
    debug_logger(str(request_user), " TASK_CREATOR_END")
