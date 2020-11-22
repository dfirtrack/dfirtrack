from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from dfirtrack_artifacts.models import Artifact, Artifactpriority, Artifactstatus
from dfirtrack_config.models import Statushistory, StatushistoryEntry
from dfirtrack_main.models import Analysisstatus, System, Systemstatus, Task, Taskpriority, Taskstatus


@login_required(login_url="/login")
def statushistory_save(request):

    # create empty statushistory (just contains primary key and datetime field)
    statushistory = Statushistory.objects.create()

    # save number of artifacts
    artifacts_number = Artifact.objects.all().count()
    StatushistoryEntry.objects.create(
        statushistory = statushistory,
        statushistoryentry_model_name = 'artifacts_number',
        statushistoryentry_model_value = artifacts_number,
    )

    # save number of systems
    systems_number = System.objects.all().count()
    StatushistoryEntry.objects.create(
        statushistory = statushistory,
        statushistoryentry_model_name = 'systems_number',
        statushistoryentry_model_value = systems_number,
    )

    # save number of tasks
    tasks_number = Task.objects.all().count()
    StatushistoryEntry.objects.create(
        statushistory = statushistory,
        statushistoryentry_model_name = 'tasks_number',
        statushistoryentry_model_value = tasks_number,
    )

    # save analysisstatus
    analysisstatus_all = Analysisstatus.objects.all().order_by('analysisstatus_id')
    for analysisstatus in analysisstatus_all:
        systems_number_analysisstatus = System.objects.filter(analysisstatus=analysisstatus).count()
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'analysisstatus',
            statushistoryentry_model_key = analysisstatus.analysisstatus_name,
            statushistoryentry_model_value = systems_number_analysisstatus,
        )

    # save artifactpriority
    artifactpriority_all = Artifactpriority.objects.all().order_by('artifactpriority_id')
    for artifactpriority in artifactpriority_all:
        artifacts_number_artifactpriority = Artifact.objects.filter(artifactpriority=artifactpriority).count()
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'artifactpriority',
            statushistoryentry_model_key = artifactpriority.artifactpriority_name,
            statushistoryentry_model_value = artifacts_number_artifactpriority,
        )

    # save artifactstatus
    artifactstatus_all = Artifactstatus.objects.all().order_by('artifactstatus_id')
    for artifactstatus in artifactstatus_all:
        artifacts_number_artifactstatus = Artifact.objects.filter(artifactstatus=artifactstatus).count()
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'artifactstatus',
            statushistoryentry_model_key = artifactstatus.artifactstatus_name,
            statushistoryentry_model_value = artifacts_number_artifactstatus,
        )

    # save systemstatus
    systemstatus_all = Systemstatus.objects.all().order_by('systemstatus_id')
    for systemstatus in systemstatus_all:
        systems_number_systemstatus = System.objects.filter(systemstatus=systemstatus).count()
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'systemstatus',
            statushistoryentry_model_key = systemstatus.systemstatus_name,
            statushistoryentry_model_value = systems_number_systemstatus,
        )

    # save taskstatus
    taskstatus_all = Taskstatus.objects.all().order_by('taskstatus_id')
    for taskstatus in taskstatus_all:
        systems_number_taskstatus = Task.objects.filter(taskstatus=taskstatus).count()
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'taskstatus',
            statushistoryentry_model_key = taskstatus.taskstatus_name,
            statushistoryentry_model_value = systems_number_taskstatus,
        )

    # save taskpriority
    taskpriority_all = Taskpriority.objects.all().order_by('taskpriority_id')
    for taskpriority in taskpriority_all:
        systems_number_taskpriority = Task.objects.filter(taskpriority=taskpriority).count()
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'taskpriority',
            statushistoryentry_model_key = taskpriority.taskpriority_name,
            statushistoryentry_model_value = systems_number_taskpriority,
        )

    # create message
    messages.success(request, 'Statushistory saved')

    # reload page to show message
    return redirect(reverse('status'))
