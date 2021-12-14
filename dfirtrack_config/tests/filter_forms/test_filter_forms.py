from django.test import TestCase

from dfirtrack_config.filter_forms import AssignmentFilterForm


class AssignmentFilterFormTestCase(TestCase):
    """assignment filter form tests"""

    def test_case_form_label(self):
        """test form label"""

        # get object
        form = AssignmentFilterForm()
        # compare
        self.assertEqual(form.fields['case'].label, 'Filter for case')

    def test_case_form_empty_label(self):
        """test form label"""

        # get object
        form = AssignmentFilterForm()
        # compare
        self.assertEqual(form.fields['case'].empty_label, 'Filter for case')

    def test_tag_form_label(self):
        """test form label"""

        # get object
        form = AssignmentFilterForm()
        # compare
        self.assertEqual(form.fields['tag'].label, 'Filter for tag')

    def test_tag_form_empty_label(self):
        """test form label"""

        # get object
        form = AssignmentFilterForm()
        # compare
        self.assertEqual(form.fields['tag'].empty_label, 'Filter for tag')

    def test_user_form_label(self):
        """test form label"""

        # get object
        form = AssignmentFilterForm()
        # compare
        self.assertEqual(form.fields['user'].label, 'Filter for user')

    def test_user_form_empty_label(self):
        """test form label"""

        # get object
        form = AssignmentFilterForm()
        # compare
        self.assertEqual(form.fields['user'].empty_label, 'No user assigned')

    def test_filter_assignment_view_keep_form_label(self):
        """test form label"""

        # get object
        form = AssignmentFilterForm()
        # compare
        self.assertEqual(
            form.fields['filter_assignment_view_keep'].label,
            'Remember filter settings (confirm by applying)',
        )

    def test_assignment_filter_form_empty(self):
        """test minimum form requirements / VALID"""

        # get object
        form = AssignmentFilterForm(data={})
        # compare
        self.assertTrue(form.is_valid())
