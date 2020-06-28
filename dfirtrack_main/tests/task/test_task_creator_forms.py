from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.forms import TaskCreatorForm
from dfirtrack_main.models import System, Systemstatus, Tag, Tagcolor, Taskname, Taskpriority, Taskstatus

class TaskCreatorFormTestCase(TestCase):
    """ task form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_task_creator', password='PG9qF4TBduBmNNVP8l6o')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

#        # create object
#        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
#
#        # create object
#        Tag.objects.create(
#            tag_name = 'tag_1',
#            tagcolor = tagcolor_1,
#        )

        # create object
        taskname_1 = Taskname.objects.create(taskname_name='taskname_1')

        # create object
        taskpriority_1 = Taskpriority.objects.create(taskpriority_name='prio_1')

        # create object
        taskstatus_1 = Taskstatus.objects.create(taskstatus_name='taskstatus_1')

    def test_task_creator_taskname_form_label(self):
        """ test form label """

        # get object
        form = TaskCreatorForm()
        # compare
        self.assertEqual(form.fields['taskname'].label, 'Tasknames')

    def test_task_creator_system_form_label(self):
        """ test form label """

        # get object
        form = TaskCreatorForm()
        # compare
        self.assertEqual(form.fields['system'].label, 'Systems')

    def test_task_creator_taskpriority_form_label(self):
        """ test form label """

        # get object
        form = TaskCreatorForm()
        # compare
        self.assertEqual(form.fields['taskpriority'].label, 'Taskpriority')

    def test_task_creator_taskstatus_form_label(self):
        """ test form label """

        # get object
        form = TaskCreatorForm()
        # compare
        self.assertEqual(form.fields['taskstatus'].label, 'Taskstatus')

    def test_task_creator_assigned_to_user_id_form_label(self):
        """ test form label """

        # get object
        form = TaskCreatorForm()
        # compare
        self.assertEqual(form.fields['task_assigned_to_user_id'].label, 'Task assigned to user id')

    def test_task_creator_note_form_label(self):
        """ test form label """

        # get object
        form = TaskCreatorForm()
        # compare
        self.assertEqual(form.fields['task_note'].label, 'Task note')

    def test_task_creator_tag_form_label(self):
        """ test form label """

        # get object
        form = TaskCreatorForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Tag')

    def test_task_creator_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = TaskCreatorForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_task_creator_taskname_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        # get object
        form = TaskCreatorForm(data = {
            'taskname': taskname_id,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_task_creator_taskpriority_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        # get object
        taskpriority_id = Taskpriority.objects.get(taskpriority_name='prio_1').taskpriority_id
        # get object
        form = TaskCreatorForm(data = {
            'taskname': taskname_id,
            'taskpriority': taskpriority_id,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_task_creator_taskstatus_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
        # get object
        taskpriority_id = Taskpriority.objects.get(taskpriority_name='prio_1').taskpriority_id
        # get object
        taskstatus_id = Taskstatus.objects.get(taskstatus_name='taskstatus_1').taskstatus_id
        # get object
        form = TaskCreatorForm(data = {
            'taskname': taskname_id,
            'taskpriority': taskpriority_id,
            'taskstatus': taskstatus_id,
        })
        # compare
        self.assertFalse(form.is_valid())

#    # TODO: not working - should be valid
#    def test_task_creator_system_form_filled(self):
#        """ test minimum form requirements / VALID """
#
#        # get object
#        system_id = System.objects.get(system_name='system_1').system_id
#        # get object
#        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
#        # get object
#        taskpriority_id = Taskpriority.objects.get(taskpriority_name='prio_1').taskpriority_id
#        # get object
#        taskstatus_id = Taskstatus.objects.get(taskstatus_name='taskstatus_1').taskstatus_id
#        # get object
#        form = TaskCreatorForm(data = {
#            'system': system_id,
#            'taskname': taskname_id,
#            'taskpriority': taskpriority_id,
#            'taskstatus': taskstatus_id,
#        })
#        # compare
#        self.assertTrue(form.is_valid())

# TODO: will also not work because of problem above
#    def test_task_creator_assigned_to_user_id_form_filled(self):
#        """ test additional form content """
#
#        # get object
#        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
#        # get object
#        taskpriority_id = Taskpriority.objects.get(taskpriority_name='prio_1').taskpriority_id
#        # get object
#        taskstatus_id = Taskstatus.objects.get(taskstatus_name='taskstatus_1').taskstatus_id
#        # get user
#        test_user_id = User.objects.get(username='testuser_task_creator').id
#        # get object
#        form = TaskCreatorForm(data = {
#            'taskname': taskname_id,
#            'taskpriority': taskpriority_id,
#            'taskstatus': taskstatus_id,
#            'task_assigned_to_user_id': test_user_id,
#        })
#        # compare
#        self.assertTrue(form.is_valid())
#
#    def test_task_creator_note_form_filled(self):
#        """ test additional form content """
#
#        # get object
#        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
#        # get object
#        taskpriority_id = Taskpriority.objects.get(taskpriority_name='prio_1').taskpriority_id
#        # get object
#        taskstatus_id = Taskstatus.objects.get(taskstatus_name='taskstatus_1').taskstatus_id
#        # get object
#        form = TaskCreatorForm(data = {
#            'taskname': taskname_id,
#            'taskpriority': taskpriority_id,
#            'taskstatus': taskstatus_id,
#            'task_note': 'lorem ipsum'
#        })
#        # compare
#        self.assertTrue(form.is_valid())
#
## TODO: test does not work as expected, returns false instead of true
##    def test_task_creator_tag_form_filled(self):
##        """ test additional form content """
##
##        # get object
##        taskname_id = Taskname.objects.get(taskname_name='taskname_1').taskname_id
##        # get object
##        taskpriority_id = Taskpriority.objects.get(taskpriority_name='prio_1').taskpriority_id
##        # get object
##        taskstatus_id = Taskstatus.objects.get(taskstatus_name='taskstatus_1').taskstatus_id
##        # get object
##        tag_id = Tag.objects.get(tag_name='tag_1').tag_id
##        # get object
##        form = TaskCreatorForm(data = {
##            'taskname': taskname_id,
##            'taskpriority': taskpriority_id,
##            'taskstatus': taskstatus_id,
##            'tag': tag_id,
##        })
##        # compare
##        self.assertTrue(form.is_valid())
