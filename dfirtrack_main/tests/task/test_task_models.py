from datetime import datetime
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from dfirtrack_main.models import (
    System,
    Systemstatus,
    Task,
    Taskname,
    Taskpriority,
    Taskstatus,
)


class TaskModelTestCase(TestCase):
    """task model tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_task', password='Zta9LblLVMWdYoXMTBZE'
        )

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object
        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')

        # create object
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='prio_1')

        # create object
        taskstatus_1 = Taskstatus.objects.create(taskstatus_name='taskstatus_1')

        # create object
        Task.objects.create(
            taskname=taskname_1,
            taskpriority=taskpriority_1,
            taskstatus=taskstatus_1,
            system=system_1,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )

    def test_task_string(self):
        """test string representation"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # compare
        self.assertEqual(
            str(task_1),
            '['
            + str(task_1.task_id)
            + '] '
            + str(task_1.taskname)
            + ' ('
            + str(task_1.system)
            + ')',
        )

    def test_task_id_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_id').verbose_name
        # compare
        self.assertEqual(field_label, 'task id')

    def test_task_parent_task_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('parent_task').verbose_name
        # compare
        self.assertEqual(field_label, 'parent task')

    def test_task_taskname_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('taskname').verbose_name
        # compare
        self.assertEqual(field_label, 'taskname')

    def test_task_taskpriority_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('taskpriority').verbose_name
        # compare
        self.assertEqual(field_label, 'taskpriority')

    def test_task_taskstatus_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('taskstatus').verbose_name
        # compare
        self.assertEqual(field_label, 'taskstatus')

    def test_task_artifact_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('artifact').verbose_name
        # compare
        self.assertEqual(field_label, 'artifact')

    def test_task_case_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('case').verbose_name
        # compare
        self.assertEqual(field_label, 'case')

    def test_task_system_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('system').verbose_name
        # compare
        self.assertEqual(field_label, 'system')

    def test_task_assigned_to_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_assigned_to_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'task assigned to user id')

    def test_task_tag_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('tag').verbose_name
        # compare
        self.assertEqual(field_label, 'tag')

    def test_task_note_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_note').verbose_name
        # compare
        self.assertEqual(field_label, 'task note')

    def test_task_scheduled_time_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_scheduled_time').verbose_name
        # compare
        self.assertEqual(field_label, 'task scheduled time')

    def test_task_started_time_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_started_time').verbose_name
        # compare
        self.assertEqual(field_label, 'task started time')

    def test_task_finished_time_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_finished_time').verbose_name
        # compare
        self.assertEqual(field_label, 'task finished time')

    def test_task_due_time_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_due_time').verbose_name
        # compare
        self.assertEqual(field_label, 'task due time')

    def test_task_is_abandoned_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_is_abandoned').verbose_name
        # compare
        self.assertEqual(field_label, 'task is abandoned')

    def test_task_create_time_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_create_time').verbose_name
        # compare
        self.assertEqual(field_label, 'task create time')

    def test_task_modify_time_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_modify_time').verbose_name
        # compare
        self.assertEqual(field_label, 'task modify time')

    def test_task_created_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_created_by_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'task created by user id')

    def test_task_modified_by_user_id_attribute_label(self):
        """test attribute label"""

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get object
        task_1 = Task.objects.get(taskname=taskname_1)
        # get label
        field_label = task_1._meta.get_field('task_modified_by_user_id').verbose_name
        # compare
        self.assertEqual(field_label, 'task modified by user id')

    def test_task_times(self):
        """test task times depending on status"""

        # get user
        test_user = User.objects.get(username='testuser_task')
        # get object
        taskname = Taskname.objects.create(taskname_name='task_times')
        # get object
        taskpriority = Taskpriority.objects.get(taskpriority_name='prio_1')
        # get object
        taskstatus_pending = Taskstatus.objects.get(taskstatus_name='10_pending')
        taskstatus_working = Taskstatus.objects.get(taskstatus_name='20_working')
        taskstatus_done = Taskstatus.objects.get(taskstatus_name='30_done')

        # create object
        task_times = Task.objects.create(
            taskname=taskname,
            taskpriority=taskpriority,
            taskstatus=taskstatus_pending,
            task_created_by_user_id=test_user,
            task_modified_by_user_id=test_user,
        )

        # compare
        self.assertEqual(task_times.task_started_time, None)
        self.assertEqual(task_times.task_finished_time, None)

        # mock timezone.now()
        dt_1 = datetime(2021, 10, 8, 13, 1, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=dt_1):

            # update object
            task_times.taskstatus = taskstatus_working
            task_times.save()

        # compare
        self.assertEqual(task_times.task_started_time, dt_1)
        self.assertEqual(task_times.task_finished_time, None)

        # mock timezone.now()
        dt_2 = datetime(2021, 10, 8, 13, 2, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=dt_2):

            # update object
            task_times.save()

        # compare
        self.assertEqual(task_times.task_started_time, dt_1)
        self.assertEqual(task_times.task_finished_time, None)

        # mock timezone.now()
        dt_3 = datetime(2021, 10, 8, 13, 3, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=dt_3):

            # update object
            task_times.taskstatus = taskstatus_done
            task_times.save()

        # compare
        self.assertEqual(task_times.task_started_time, dt_1)
        self.assertEqual(task_times.task_finished_time, dt_3)

        # mock timezone.now()
        dt_4 = datetime(2021, 10, 8, 13, 4, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=dt_4):

            # update object
            task_times.save()

        # compare
        self.assertEqual(task_times.task_started_time, dt_1)
        self.assertEqual(task_times.task_finished_time, dt_3)

        # mock timezone.now()
        dt_5 = datetime(2021, 10, 8, 13, 5, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=dt_5):

            # update object
            task_times.taskstatus = taskstatus_working
            task_times.save()

        # compare
        self.assertEqual(task_times.task_started_time, dt_1)
        self.assertEqual(task_times.task_finished_time, None)

        # mock timezone.now()
        dt_6 = datetime(2021, 10, 8, 13, 6, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=dt_6):

            # update object
            task_times.taskstatus = taskstatus_pending
            task_times.save()

        # compare
        self.assertEqual(task_times.task_started_time, None)
        self.assertEqual(task_times.task_finished_time, None)

        # mock timezone.now()
        dt_7 = datetime(2021, 10, 8, 13, 7, tzinfo=timezone.utc)
        with patch.object(timezone, 'now', return_value=dt_7):

            # update object
            task_times.taskstatus = taskstatus_done
            task_times.save()

        # compare
        self.assertEqual(task_times.task_started_time, dt_7)
        self.assertEqual(task_times.task_finished_time, dt_7)
