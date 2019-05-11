from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.forms import ReportitemForm
from dfirtrack_main.models import Headline, System, Systemstatus

class ReportitemFormTestCase(TestCase):
    """ reportitem form tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_reportitem', password='6vrj2phUKrw6cjbbtN9V')
        test_user.save()

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        headline_1 = Headline.objects.create(headline_name='headline_1')

    def test_reportitem_system_label(self):

        # get object
        form = ReportitemForm()
        # compare
        self.assertEquals(form.fields['system'].label, 'System (*)')

    def test_reportitem_headline_label(self):

        # get object
        form = ReportitemForm()
        # compare
        self.assertEquals(form.fields['headline'].label, 'Headline (*)')

    def test_reportitem_subheadline_label(self):

        # get object
        form = ReportitemForm()
        # compare
        self.assertEquals(form.fields['reportitem_subheadline'].label, 'Subheadline')

    def test_reportitem_note_label(self):

        # get object
        form = ReportitemForm()
        # compare
        self.assertEquals(form.fields['reportitem_note'].label, 'Note (*)')

    def test_reportitem_note_empty_no_system(self):

        # get object
        form = ReportitemForm(data = {'reportitem_note': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_reportitem_note_filled_no_system(self):

        # get object
        form = ReportitemForm(data = {'reportitem_note': 'lorem ipsum'})
        # compare
        self.assertFalse(form.is_valid())

    def test_reportitem_note_filled_no_headline(self):

        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ReportitemForm(data = {
            'reportitem_note': 'lorem ipsum',
            'system': system_id,
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_reportitem_filled(self):

        # get foreign key object id
        headline_id = Headline.objects.get(headline_name='headline_1').headline_id
        # get foreign key object id
        system_id = System.objects.get(system_name='system_1').system_id
        # get object
        form = ReportitemForm(data = {
            'reportitem_note': 'lorem ipsum',
            'system': system_id,
            'headline': headline_id,
        })
        # compare
        self.assertTrue(form.is_valid())
