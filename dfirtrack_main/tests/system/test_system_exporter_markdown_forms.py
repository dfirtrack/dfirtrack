from django.test import TestCase
from dfirtrack_main.config_forms import SystemExporterMarkdownForm

class SystemExporterMarkdownFormTestCase(TestCase):
    """ system exporter markdown form tests """

    @classmethod
    def setUpTestData(cls):

        pass

    def test_system_exporter_markdown_config_markdown_path_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterMarkdownForm()
        # compare
        self.assertEqual(form.fields['markdown_path'].label, 'Path for the markdown documentation export')

    def test_system_exporter_markdown_config_markdown_sorting_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterMarkdownForm()
        # compare
        self.assertEqual(form.fields['markdown_sorting'].label, 'Choose sorting for system markdown export')

    def test_system_exporter_markdown_config_form_empty(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemExporterMarkdownForm(data = {})
        # compare
        self.assertFalse(form.is_valid())

    def test_system_exporter_markdown_config_markdown_path_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemExporterMarkdownForm(data = {
            'markdown_path': '/tmp',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_exporter_markdown_config_markdown_sorting_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemExporterMarkdownForm(data = {
            'markdown_sorting': '/tmp',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_exporter_markdown_config_all_fields_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        form = SystemExporterMarkdownForm(data = {
            'markdown_path': '/tmp',
            'markdown_sorting': 'systemsorted',
        })
        # compare
        self.assertTrue(form.is_valid())
