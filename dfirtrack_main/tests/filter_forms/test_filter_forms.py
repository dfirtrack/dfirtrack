from django.test import TestCase

from dfirtrack_main.filter_forms import DocumentationFilterForm, SystemFilterForm


class DocumentationFilterFormTestCase(TestCase):
    """documentation filter form tests"""

    def test_case_form_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(form.fields['case'].label, 'Filter for case')

    def test_case_form_empty_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(form.fields['case'].empty_label, 'Filter for case')

    def test_notestatus_form_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(form.fields['notestatus'].label, 'Filter for notestatus')

    def test_notestatus_form_empty_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(form.fields['notestatus'].empty_label, 'Filter for notestatus')

    def test_tag_form_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Filter for tag')

    def test_tag_form_empty_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(form.fields['tag'].empty_label, 'Filter for tag')

    def test_filter_documentation_list_keep_form_label(self):
        """test form label"""

        # get object
        form = DocumentationFilterForm()
        # compare
        self.assertEqual(
            form.fields['filter_documentation_list_keep'].label,
            'Remember filter settings (confirm by applying)',
        )

    def test_documentation_filter_form_empty(self):
        """test minimum form requirements / VALID"""

        # get object
        form = DocumentationFilterForm(data={})
        # compare
        self.assertTrue(form.is_valid())


class SystemFilterFormTestCase(TestCase):
    """system filter form tests"""

    def test_case_form_label(self):
        """test form label"""

        # get object
        form = SystemFilterForm()
        # compare
        self.assertEqual(form.fields['case'].label, 'Filter for case')

    def test_case_form_empty_label(self):
        """test form label"""

        # get object
        form = SystemFilterForm()
        # compare
        self.assertEqual(form.fields['case'].empty_label, 'Filter for case')

    def test_tag_form_label(self):
        """test form label"""

        # get object
        form = SystemFilterForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Filter for tag')

    def test_tag_form_empty_label(self):
        """test form label"""

        # get object
        form = SystemFilterForm()
        # compare
        self.assertEqual(form.fields['tag'].empty_label, 'Filter for tag')

    def test_filter_system_list_keep_form_label(self):
        """test form label"""

        # get object
        form = SystemFilterForm()
        # compare
        self.assertEqual(
            form.fields['filter_system_list_keep'].label,
            'Remember filter settings (confirm by applying)',
        )

    def test_system_filter_form_empty(self):
        """test minimum form requirements / VALID"""

        # get object
        form = SystemFilterForm(data={})
        # compare
        self.assertTrue(form.is_valid())
