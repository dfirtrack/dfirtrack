from django.test import TestCase
from dfirtrack_main.forms import TasknameForm

class TasknameFormTestCase(TestCase):
    """ taskname form tests """

    def test_taskname_name_label(self):

        # get object
        form = TasknameForm()
        # compare
        self.assertEquals(form.fields['taskname_name'].label, 'Taskname (*)')

    def test_taskname_name_empty(self):

        # get object
        form = TasknameForm(data = {'taskname_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_taskname_name_filled(self):

        # get object
        form = TasknameForm(data = {'taskname_name': 'taskname_1'})
        # compare
        self.assertTrue(form.is_valid())

    def test_taskname_name_proper_chars(self):

        # get object
        form = TasknameForm(data = {'taskname_name': 'tttttttttttttttttttttttttttttttttttttttttttttttttt'})
        # compare
        self.assertTrue(form.is_valid())

    def test_taskname_name_too_many_chars(self):

        # get object
        form = TasknameForm(data = {'taskname_name': 'ttttttttttttttttttttttttttttttttttttttttttttttttttt'})
        # compare
        self.assertFalse(form.is_valid())
