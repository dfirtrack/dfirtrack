import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import System, Systemstatus


def set_user_config_toogle_false(test_user):
    """set toggle flags in user config to false"""

    # get config
    user_config = UserConfigModel.objects.get(user_config_username=test_user)
    # set values
    user_config.filter_system_detail_show_artifact = False
    user_config.filter_system_detail_show_artifact_closed = False
    user_config.filter_system_detail_show_task = False
    user_config.filter_system_detail_show_task_closed = False
    user_config.filter_system_detail_show_technical_information = False
    user_config.filter_system_detail_show_timeline = False
    user_config.filter_system_detail_show_virtualization_information = False
    user_config.filter_system_detail_show_company_information = False
    user_config.filter_system_detail_show_systemuser = False
    user_config.filter_system_detail_show_analystmemo = False
    user_config.filter_system_detail_show_reportitem = False
    # save config
    user_config.save()

    # return to test
    return


def set_user_config_toogle_true(test_user):
    """set toggle flags in user config to true"""

    # get config
    user_config = UserConfigModel.objects.get(user_config_username=test_user)
    # set values
    user_config.filter_system_detail_show_artifact = True
    user_config.filter_system_detail_show_artifact_closed = True
    user_config.filter_system_detail_show_task = True
    user_config.filter_system_detail_show_task_closed = True
    user_config.filter_system_detail_show_technical_information = True
    user_config.filter_system_detail_show_timeline = True
    user_config.filter_system_detail_show_virtualization_information = True
    user_config.filter_system_detail_show_company_information = True
    user_config.filter_system_detail_show_systemuser = True
    user_config.filter_system_detail_show_analystmemo = True
    user_config.filter_system_detail_show_reportitem = True
    # save config
    user_config.save()

    # return to test
    return


class SystemToggleTestCase(TestCase):
    """system toggle tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')

        # create config
        UserConfigModel.objects.get_or_create(user_config_username=test_user)

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

    def test_system_detail_artifact_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_artifact/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_artifact/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_artifact_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#artifact', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_artifact/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_artifact_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_artifact/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_artifact')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_artifact_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_artifact/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_artifact)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_artifact'])

    def test_system_detail_artifact_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_artifact/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_artifact)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_artifact'])

    def test_system_detail_task_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_task/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_task/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_task_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#task', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_task/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_task_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_task/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_task')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_task_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_task/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_task)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_task'])

    def test_system_detail_task_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_task/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_task)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_task'])

    def test_system_detail_task_closed_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_task_closed/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_task_closed/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_task_closed_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#task', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_task_closed/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_task_closed_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_task_closed/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_task_closed')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_task_closed_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_task_closed/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_task_closed)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_task_closed'])

    def test_system_detail_task_closed_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_task_closed/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_task_closed)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_task_closed'])

    def test_system_detail_technical_information_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_technical_information/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_technical_information/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_technical_information_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#technical_information', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_technical_information/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_technical_information_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_technical_information/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_technical_information')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_technical_information_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_technical_information/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_technical_information)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_technical_information'])

    def test_system_detail_technical_information_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_technical_information/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_technical_information)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_technical_information'])

    def test_system_detail_timeline_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_timeline/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_timeline/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_timeline_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#timeline', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_timeline/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_timeline_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_timeline/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_timeline')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_timeline_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_timeline/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_timeline)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_timeline'])

    def test_system_detail_timeline_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_timeline/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_timeline)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_timeline'])

    def test_system_detail_virtualization_information_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_virtualization_information/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_virtualization_information/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_virtualization_information_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#virtualization_information', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_virtualization_information/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_virtualization_information_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_virtualization_information/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_virtualization_information')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_virtualization_information_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_virtualization_information/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_virtualization_information)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_virtualization_information'])

    def test_system_detail_virtualization_information_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_virtualization_information/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_virtualization_information)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_virtualization_information'])

    def test_system_detail_company_information_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_company_information/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_company_information/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_company_information_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#company_information', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_company_information/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_company_information_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_company_information/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_company_information')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_company_information_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_company_information/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_company_information)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_company_information'])

    def test_system_detail_company_information_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_company_information/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_company_information)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_company_information'])

    def test_system_detail_systemuser_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_systemuser/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_systemuser/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_systemuser_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#systemuser', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_systemuser/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_systemuser_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_systemuser/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_systemuser')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_systemuser_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_systemuser/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_systemuser)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_systemuser'])

    def test_system_detail_systemuser_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_systemuser/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_systemuser)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_systemuser'])

    def test_system_detail_analystmemo_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_analystmemo/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_analystmemo/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_analystmemo_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#analystmemo', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_analystmemo/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_analystmemo_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_analystmemo/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_analystmemo')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_analystmemo_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_analystmemo/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_analystmemo)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_analystmemo'])

    def test_system_detail_analystmemo_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_analystmemo/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_analystmemo)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_analystmemo'])

    def test_system_detail_reportitem_toggle_not_logged_in(self):
        """test toggle view"""

        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote(f'/system/{system_1.system_id}/toggle_reportitem/', safe='')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_reportitem/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_reportitem_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/#reportitem', safe='/#')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_reportitem/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_detail_reportitem_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # create url
        destination = urllib.parse.quote(f'/system/{system_1.system_id}/toggle_reportitem/', safe='/')
        # get response
        response = self.client.get(f'/system/{system_1.system_id}/toggle_reportitem')
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=302)

    def test_system_detail_reportitem_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_reportitem/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_system_detail_show_reportitem)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertTrue(response.context['show_reportitem'])

    def test_system_detail_reportitem_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(username='testuser_system_toggle', password='V1z7IQhdpWRYKkqdMLDt')
        # get object
        system_1 = System.objects.get(system_name='system_1')
        # get user
        test_user = User.objects.get(username='testuser_system_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get(f'/system/{system_1.system_id}/toggle_reportitem/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_system_detail_show_reportitem)
        # reload system detail to get response context
        response = self.client.get(f'/system/{system_1.system_id}/')
        # compare
        self.assertFalse(response.context['show_reportitem'])
