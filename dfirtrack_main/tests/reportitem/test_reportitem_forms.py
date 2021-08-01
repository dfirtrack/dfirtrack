from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.forms import ReportitemForm
from dfirtrack_main.models import Headline, Notestatus, System, Systemstatus


class ReportitemFormTestCase(TestCase):
    """reportitem form tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username="testuser_reportitem", password="6vrj2phUKrw6cjbbtN9V"
        )

        # create object
        Headline.objects.create(headline_name="headline_1")
        Notestatus.objects.create(notestatus_name="notestatus_1")
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name="systemstatus_1")

        # create object
        System.objects.create(
            system_name="system_1",
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

    def test_reportitem_headline_form_label(self):
        """test form label"""

        # get object
        form = ReportitemForm()
        # compare
        self.assertEqual(form.fields["headline"].label, "Headline (*)")
        self.assertEqual(form.fields["headline"].empty_label, "Select headline")

    def test_reportitem_case_form_label(self):
        """test form label"""

        # get object
        form = ReportitemForm()
        # compare
        self.assertEqual(form.fields["case"].label, "Corresponding case")
        self.assertEqual(form.fields["case"].empty_label, "Select case (optional)")

    def test_reportitem_notestatus_form_label(self):
        """test form label"""

        # get object
        form = ReportitemForm()
        # compare
        self.assertEqual(form.fields["notestatus"].label, "Notestatus (*)")

    def test_reportitem_system_form_label(self):
        """test form label"""

        # get object
        form = ReportitemForm()
        # compare
        self.assertEqual(form.fields["system"].label, "System (*)")
        self.assertEqual(form.fields["system"].empty_label, "Select system")

    def test_reportitem_tag_form_label(self):
        """test form label"""

        # get object
        form = ReportitemForm()
        # compare
        self.assertEqual(form.fields["tag"].label, "Tags")

    def test_reportitem_subheadline_form_label(self):
        """test form label"""

        # get object
        form = ReportitemForm()
        # compare
        self.assertEqual(form.fields["reportitem_subheadline"].label, "Subheadline")

    def test_reportitem_note_form_label(self):
        """test form label"""

        # get object
        form = ReportitemForm()
        # compare
        self.assertEqual(form.fields["reportitem_note"].label, "Note (*)")

    def test_reportitem_form_empty(self):
        """test minimum form requirements / INVALID"""

        # get object
        form = ReportitemForm(data={})
        # compare
        self.assertFalse(form.is_valid())

    def test_reportitem_note_form_filled(self):
        """test minimum form requirements / INVALID"""

        # get object
        form = ReportitemForm(
            data={
                "reportitem_note": "lorem ipsum",
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_reportitem_notestatus_form_filled(self):
        """test minimum form requirements / INVALID"""

        # get foreign key object id
        notestatus_id = Notestatus.objects.get(
            notestatus_name="notestatus_1"
        ).notestatus_id
        # get object
        form = ReportitemForm(
            data={
                "reportitem_note": "lorem ipsum",
                "notestatus": notestatus_id,
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_reportitem_system_form_filled(self):
        """test minimum form requirements / INVALID"""

        # get foreign key object id
        notestatus_id = Notestatus.objects.get(
            notestatus_name="notestatus_1"
        ).notestatus_id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = ReportitemForm(
            data={
                "reportitem_note": "lorem ipsum",
                "notestatus": notestatus_id,
                "system": system_id,
            }
        )
        # compare
        self.assertFalse(form.is_valid())

    def test_reportitem_headline_form_filled(self):
        """test minimum form requirements / VALID"""

        # get foreign key object id
        headline_id = Headline.objects.get(headline_name="headline_1").headline_id
        notestatus_id = Notestatus.objects.get(
            notestatus_name="notestatus_1"
        ).notestatus_id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = ReportitemForm(
            data={
                "reportitem_note": "lorem ipsum",
                "headline": headline_id,
                "notestatus": notestatus_id,
                "system": system_id,
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_reportitem_subheadline_form_filled(self):
        """test additional form content"""

        # get foreign key object id
        headline_id = Headline.objects.get(headline_name="headline_1").headline_id
        notestatus_id = Notestatus.objects.get(
            notestatus_name="notestatus_1"
        ).notestatus_id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = ReportitemForm(
            data={
                "reportitem_note": "lorem ipsum",
                "headline": headline_id,
                "notestatus": notestatus_id,
                "system": system_id,
                "reportitem_subheadline": "subheadline_1",
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_reportitem_subheadline_proper_chars(self):
        """test for max length"""

        # get foreign key object id
        headline_id = Headline.objects.get(headline_name="headline_1").headline_id
        notestatus_id = Notestatus.objects.get(
            notestatus_name="notestatus_1"
        ).notestatus_id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = ReportitemForm(
            data={
                "reportitem_note": "lorem ipsum",
                "headline": headline_id,
                "notestatus": notestatus_id,
                "system": system_id,
                "reportitem_subheadline": "s" * 100,
            }
        )
        # compare
        self.assertTrue(form.is_valid())

    def test_reportitem_subheadline_too_many_chars(self):
        """test for max length"""

        # get foreign key object id
        headline_id = Headline.objects.get(headline_name="headline_1").headline_id
        notestatus_id = Notestatus.objects.get(
            notestatus_name="notestatus_1"
        ).notestatus_id
        system_id = System.objects.get(system_name="system_1").system_id
        # get object
        form = ReportitemForm(
            data={
                "reportitem_note": "lorem ipsum",
                "headline": headline_id,
                "notestatus": notestatus_id,
                "system": system_id,
                "reportitem_subheadline": "s" * 101,
            }
        )
        # compare
        self.assertFalse(form.is_valid())
