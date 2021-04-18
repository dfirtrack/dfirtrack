from django.test import TestCase
from django.urls import reverse
from dfirtrack_config.models import MainConfigModel

def set_main_overview(main_overview):
    """ change config """

    model = MainConfigModel.objects.get(main_config_name='MainConfig')
    model.main_overview = f'main_overview_{main_overview}'
    model.save()

class MainOverviewViewTestCase(TestCase):
    """ main overview view tests """

    def test_main_overview_system_url(self):
        """ test list view """

        # change config
        set_main_overview('system')

        # get reverse url
        url = reverse('main_overview')
        # compare
        self.assertEqual(url, '/system/')

# TODO: find a way to reload URLs during test
# like described in https://codeinthehole.com/tips/how-to-reload-djangos-url-config/ (obviously oudated)
#    def test_main_overview_artfact_url(self):
#        """ test list view """
#
#        # change config
#        set_main_overview('artfact')
#
#        # get reverse url
#        url = reverse('main_overview')
#        # compare
#        self.assertEqual(url, '/artfact/')
#
#    def test_main_overview_case_url(self):
#        """ test list view """
#
#        # change config
#        set_main_overview('case')
#
#        # get reverse url
#        url = reverse('main_overview')
#        # compare
#        self.assertEqual(url, '/case/')
#
#    def test_main_overview_tag_url(self):
#        """ test list view """
#
#        # change config
#        set_main_overview('tag')
#
#        # get reverse url
#        url = reverse('main_overview')
#        # compare
#        self.assertEqual(url, '/tag/')
#
#    def test_main_overview_task_url(self):
#        """ test list view """
#
#        # change config
#        set_main_overview('task')
#
#        # get reverse url
#        url = reverse('main_overview')
#        # compare
#        self.assertEqual(url, '/task/')

    def test_main_overview_default_url(self):
        """ test list view """

        # change config
        set_main_overview('foobar')

        # get reverse url
        url = reverse('main_overview')
        # compare
        self.assertEqual(url, '/system/')
