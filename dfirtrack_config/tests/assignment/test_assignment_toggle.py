import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.models import UserConfigModel


def set_user_config_toogle_false(test_user):
    """set toggle flags in user config to false"""

    # get config
    user_config = UserConfigModel.objects.get(user_config_username=test_user)
    # set values
    user_config.filter_assignment_view_show_artifact = False
    user_config.filter_assignment_view_show_case = False
    user_config.filter_assignment_view_show_note = False
    user_config.filter_assignment_view_show_reportitem = False
    user_config.filter_assignment_view_show_system = False
    user_config.filter_assignment_view_show_tag = False
    user_config.filter_assignment_view_show_task = False
    # save config
    user_config.save()

    # return to test
    return


def set_user_config_toogle_true(test_user):
    """set toggle flags in user config to true"""

    # get config
    user_config = UserConfigModel.objects.get(user_config_username=test_user)
    # set values
    user_config.filter_assignment_view_show_artifact = True
    user_config.filter_assignment_view_show_case = True
    user_config.filter_assignment_view_show_note = True
    user_config.filter_assignment_view_show_reportitem = True
    user_config.filter_assignment_view_show_system = True
    user_config.filter_assignment_view_show_tag = True
    user_config.filter_assignment_view_show_task = True
    # save config
    user_config.save()

    # return to test
    return


class AssignmentToggleTestCase(TestCase):
    """assignment toggle tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )

        # create config
        UserConfigModel.objects.get_or_create(user_config_username=test_user)

    def test_assignment_view_artifact_toggle_not_logged_in(self):
        """test toggle view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/toggle_artifact/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/toggle_artifact/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_artifact_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/#artifact', safe='/#')
        # get response
        response = self.client.get('/config/assignment/toggle_artifact/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_artifact_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote(
            '/config/assignment/toggle_artifact/', safe='/'
        )
        # get response
        response = self.client.get('/config/assignment/toggle_artifact')
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=302
        )

    def test_assignment_view_artifact_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get('/config/assignment/toggle_artifact/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_assignment_view_show_artifact)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(response.context['show_artifact'])

    def test_assignment_view_artifact_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get('/config/assignment/toggle_artifact/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_assignment_view_show_artifact)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertFalse(response.context['show_artifact'])

    def test_assignment_view_case_toggle_not_logged_in(self):
        """test toggle view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/toggle_case/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/toggle_case/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_case_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/#case', safe='/#')
        # get response
        response = self.client.get('/config/assignment/toggle_case/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_case_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/toggle_case/', safe='/')
        # get response
        response = self.client.get('/config/assignment/toggle_case')
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=302
        )

    def test_assignment_view_case_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get('/config/assignment/toggle_case/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_assignment_view_show_case)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(response.context['show_case'])

    def test_assignment_view_case_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get('/config/assignment/toggle_case/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_assignment_view_show_case)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertFalse(response.context['show_case'])

    def test_assignment_view_note_toggle_not_logged_in(self):
        """test toggle view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/toggle_note/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/toggle_note/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_note_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/#note', safe='/#')
        # get response
        response = self.client.get('/config/assignment/toggle_note/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_note_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/toggle_note/', safe='/')
        # get response
        response = self.client.get('/config/assignment/toggle_note')
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=302
        )

    def test_assignment_view_note_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get('/config/assignment/toggle_note/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_assignment_view_show_note)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(response.context['show_note'])

    def test_assignment_view_note_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get('/config/assignment/toggle_note/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_assignment_view_show_note)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertFalse(response.context['show_note'])

    def test_assignment_view_reportitem_toggle_not_logged_in(self):
        """test toggle view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/toggle_reportitem/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/toggle_reportitem/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_reportitem_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/#reportitem', safe='/#')
        # get response
        response = self.client.get('/config/assignment/toggle_reportitem/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_reportitem_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote(
            '/config/assignment/toggle_reportitem/', safe='/'
        )
        # get response
        response = self.client.get('/config/assignment/toggle_reportitem')
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=302
        )

    def test_assignment_view_reportitem_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get('/config/assignment/toggle_reportitem/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_assignment_view_show_reportitem)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(response.context['show_reportitem'])

    def test_assignment_view_reportitem_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get('/config/assignment/toggle_reportitem/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_assignment_view_show_reportitem)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertFalse(response.context['show_reportitem'])

    def test_assignment_view_system_toggle_not_logged_in(self):
        """test toggle view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/toggle_system/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/toggle_system/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_system_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/#system', safe='/#')
        # get response
        response = self.client.get('/config/assignment/toggle_system/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_system_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/toggle_system/', safe='/')
        # get response
        response = self.client.get('/config/assignment/toggle_system')
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=302
        )

    def test_assignment_view_system_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get('/config/assignment/toggle_system/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_assignment_view_show_system)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(response.context['show_system'])

    def test_assignment_view_system_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get('/config/assignment/toggle_system/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_assignment_view_show_system)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertFalse(response.context['show_system'])

    def test_assignment_view_tag_toggle_not_logged_in(self):
        """test toggle view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/toggle_tag/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/toggle_tag/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_tag_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/#tag', safe='/#')
        # get response
        response = self.client.get('/config/assignment/toggle_tag/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_tag_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/toggle_tag/', safe='/')
        # get response
        response = self.client.get('/config/assignment/toggle_tag')
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=302
        )

    def test_assignment_view_tag_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get('/config/assignment/toggle_tag/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_assignment_view_show_tag)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(response.context['show_tag'])

    def test_assignment_view_tag_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get('/config/assignment/toggle_tag/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_assignment_view_show_tag)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertFalse(response.context['show_tag'])

    def test_assignment_view_task_toggle_not_logged_in(self):
        """test toggle view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/config/assignment/toggle_task/', safe=''
        )
        # get response
        response = self.client.get('/config/assignment/toggle_task/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_task_toggle_logged_in(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/#task', safe='/#')
        # get response
        response = self.client.get('/config/assignment/toggle_task/')
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_assignment_view_task_toggle_redirect(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # create url
        destination = urllib.parse.quote('/config/assignment/toggle_task/', safe='/')
        # get response
        response = self.client.get('/config/assignment/toggle_task')
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=302
        )

    def test_assignment_view_task_toggle_context_true(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to false
        set_user_config_toogle_false(test_user)
        # get response
        self.client.get('/config/assignment/toggle_task/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertTrue(user_config.filter_assignment_view_show_task)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertTrue(response.context['show_task'])

    def test_assignment_view_task_toggle_context_false(self):
        """test toggle view"""

        # login testuser
        self.client.login(
            username='testuser_assignment_toggle', password='KAeyjTTJP7DzWKpdhKla'
        )
        # get user
        test_user = User.objects.get(username='testuser_assignment_toggle')
        # set toggle flags in user config to true
        set_user_config_toogle_true(test_user)
        # get response
        self.client.get('/config/assignment/toggle_task/')
        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertFalse(user_config.filter_assignment_view_show_task)
        # reload assignment view to get response context
        response = self.client.get('/config/assignment/')
        # compare
        self.assertFalse(response.context['show_task'])
