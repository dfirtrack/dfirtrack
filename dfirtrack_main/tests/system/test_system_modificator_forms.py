from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.forms import SystemModificatorForm
from dfirtrack_main.models import Analysisstatus, Systemstatus, Tag, Tagcolor

class SystemModificatorFormTestCase(TestCase):
    """ system modificator form tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(
            tag_name = 'tag_1',
            tagcolor = tagcolor_1,
        )
        Tag.objects.create(
            tag_name = 'tag_2',
            tagcolor = tagcolor_1,
        )


    def test_system_modificator_systemlist_form_label(self):
        """ test form label """

        # get object
        form = SystemModificatorForm()
        # compare
        self.assertEqual(form.fields['systemlist'].label, 'System list')

    def test_system_modificator_tag_form_label(self):
        """ test form label """

        # get object
        form = SystemModificatorForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Tag')

    def test_system_modificator_systemstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemModificatorForm()
        # compare
        self.assertEqual(form.fields['systemstatus'].label, 'Systemstatus')

    def test_system_modificator_analysisstatus_form_label(self):
        """ test form label """

        # get object
        form = SystemModificatorForm()
        # compare
        self.assertEqual(form.fields['analysisstatus'].label, 'Analysisstatus')

    def test_system_modificator_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemModificatorForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_system_modificator_systemlist_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemModificatorForm(data = {
            'systemlist': 'system_1',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_modificator_systemstatus_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        form = SystemModificatorForm(data = {
            'systemlist': 'system_1',
            'systemstatus': systemstatus_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_system_modificator_analysisstatus_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        analysisstatus_id = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1').analysisstatus_id
        # get object
        form = SystemModificatorForm(data = {
            'systemlist': 'system_1',
            'systemstatus': systemstatus_id,
            'analysisstatus': analysisstatus_id,
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_system_modificator_tag_form_filled(self):
        """ test additional form content """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        tag_1_id = Tag.objects.get(tag_name='tag_1').tag_id
        tag_2_id = Tag.objects.get(tag_name='tag_2').tag_id
        # get object
        form = SystemModificatorForm(data = {
            'systemlist': 'system_1',
            'systemstatus': systemstatus_id,
            'tag': [tag_1_id, tag_2_id],
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_system_modificator_systemlist_multi_line(self):
        """ test for multiple line input """

        # get object
        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
        # get object
        form = SystemModificatorForm(data = {
            'systemlist': 'system_1\nsystem_2\nsystem_3',
            'systemstatus': systemstatus_id,
        })
        # compare
        self.assertTrue(form.is_valid())
