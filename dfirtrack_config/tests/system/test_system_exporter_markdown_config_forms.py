from django.test import TestCase

from dfirtrack_config.forms import SystemExporterMarkdownConfigForm


class SystemExporterMarkdownConfigFormTestCase(TestCase):
    """ system exporter markdown config form tests """

    def test_system_exporter_markdown_config_markdown_path_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterMarkdownConfigForm()
        # compare
        self.assertEqual(form.fields['markdown_path'].label, 'Path for the markdown documentation export')

    def test_system_exporter_markdown_config_markdown_sorting_form_label(self):
        """ test form label """

        # get object
        form = SystemExporterMarkdownConfigForm()
        # compare
        self.assertEqual(form.fields['markdown_sorting'].label, 'Choose sorting for system markdown export')

    def test_system_exporter_markdown_config_markdown_path_form_filled(self):
        """ test minimum form requirements / INVALID """

        # get object
        form = SystemExporterMarkdownConfigForm(data = {
            'markdown_path': '/tmp',
        })
        # compare
        self.assertFalse(form.is_valid())

    def test_system_exporter_markdown_config_all_fields_form_filled(self):
        """ test minimum form requirements / VALID """

        # get object
        form = SystemExporterMarkdownConfigForm(data = {
            'markdown_path': '/tmp',
            'markdown_sorting': 'sys',
        })
        # compare
        self.assertTrue(form.is_valid())

    def test_system_exporter_markdown_config_markdown_path_not_existent(self):
        """ test field validation """

        # get object
        form = SystemExporterMarkdownConfigForm(data = {
            'markdown_path': '/foobar',
            'markdown_sorting': 'dom',
        })
        # compare
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['markdown_path'], ['Markdown path does not exist.'])

    def test_system_exporter_markdown_config_markdown_path_no_write_permission(self):
        """ test field validation """

        # get object
        form = SystemExporterMarkdownConfigForm(data = {
            'markdown_path': '/root',
            'markdown_sorting': 'dom',
        })
        # compare
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['markdown_path'], ['No write permission for markdown path.'])
