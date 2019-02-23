from django.test import TestCase
from dfirtrack_main.models import Taskname

class TasknameModelTestCase(TestCase):
    """ taskname model tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Taskname.objects.create(taskname_name='taskname_1')

    def test_taskname_string(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # compare
        self.assertEqual(str(taskname_1), 'taskname_1')

    def test_taskname_name_label(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get label
        field_label = taskname_1._meta.get_field('taskname_name').verbose_name
        # compare
        self.assertEquals(field_label, 'taskname name')

    def test_taskname_name_length(self):

        # get object
        taskname_1 = Taskname.objects.get(taskname_name='taskname_1')
        # get max length
        max_length = taskname_1._meta.get_field('taskname_name').max_length
        # compare
        self.assertEquals(max_length, 50)
