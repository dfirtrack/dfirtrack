from django.db.models.signals import pre_delete
from django.dispatch import receiver
from dfirtrack_artifacts.models import Artifact
from dfirtrack_main.models import Case, System


@receiver(pre_delete, sender=Artifact)
def artifact_pre_delete_task_set_abandoned(sender, instance, *args, **kwargs):
    """ check artifact related task for abandonment """

    # improve readabiltiy
    artifact = instance

    # get tasks associated with artifact
    tasks = artifact.task_set.all()

    # if there any tasks for this artifact
    if tasks:

        # remove all tasks from artifact (otherwise 'self.artifact' would be still existing)
        artifact.task_set.clear()

        # iterate over tasks
        for task in tasks:

            # refresh object
            task.refresh_from_db()

            # trigger abandonment check
            task.save()

@receiver(pre_delete, sender=Case)
def case_pre_delete_task_set_abandoned(sender, instance, *args, **kwargs):
    """ check case related task for abandonment """

    # improve readabiltiy
    case = instance

    # get tasks associated with case
    tasks = case.task_set.all()

    # if there any tasks for this case
    if tasks:

        # remove all tasks from case (otherwise 'self.case' would be still existing)
        case.task_set.clear()

        # iterate over tasks
        for task in tasks:

            # refresh object
            task.refresh_from_db()

            # trigger abandonment check
            task.save()

@receiver(pre_delete, sender=System)
def system_pre_delete_task_set_abandoned(sender, instance, *args, **kwargs):
    """ check system related task for abandonment """

    # improve readabiltiy
    system = instance

    # get tasks associated with system
    tasks = system.task_set.all()

    # if there any tasks for this system
    if tasks:

        # remove all tasks from system (otherwise 'self.system' would be still existing)
        system.task_set.clear()

        # iterate over tasks
        for task in tasks:

            # refresh object
            task.refresh_from_db()

            # trigger abandonment check
            task.save()
