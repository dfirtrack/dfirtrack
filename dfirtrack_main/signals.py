from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from dfirtrack_artifacts.models import Artifact
from dfirtrack_main.async_messages import message_users
from dfirtrack_main.logger.default_logger import info_logger
from dfirtrack_main.models import Case, Reportitem, System


@receiver(pre_delete, sender=Artifact)
def artifact_pre_delete_task_set_abandoned(sender, instance, *args, **kwargs):
    """ check artifact related task for abandonment """

    # improve readability
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

    # improve readability
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

    # improve readability
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

@receiver(post_save, sender=Reportitem)
def reportitem_post_save_system_case(sender, instance, *args, **kwargs):
    """ link system to case if system's reportitem was set to case """

    # improve readability
    reportitem = instance

    # reportitem was linked with a case
    if reportitem.case:

        # improve readability
        reportitem_case = reportitem.case
        reportitem_system = reportitem.system

        # check whether reportitem's system is linked with reportitem's case
        if not reportitem_case in reportitem_system.case.all():

            # link reportitem's system with reportitem's case
            reportitem_system.case.add(reportitem_case)

            # get all users
            all_users = User.objects.all()

            # call message for all users
            message_users(
                all_users,
                f"System '{reportitem_system.system_name}' was assigned to case '{reportitem_case.case_name}' due to reportitem assignment.",
                constants.SUCCESS
            )

            # call logger
            info_logger('signal', f' SYSTEM_CASE_ASSIGNMENT system_id:{reportitem_system.system_id}|system_name:{reportitem_system.system_name}|case_id:{reportitem_case.case_id}|case_name:{reportitem_case.case_name}|reason:reportitem_assignment')
