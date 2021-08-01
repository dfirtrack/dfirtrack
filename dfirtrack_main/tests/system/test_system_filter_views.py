import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import Case, System, Systemstatus, Tag, Tagcolor


def set_user_config(test_user, filter_system_list_case, filter_system_list_tag, filter_system_list_keep=True):
    """" set user config """

    # get config
    user_config = UserConfigModel.objects.get(user_config_username=test_user)
    # set values
    user_config.filter_system_list_case = filter_system_list_case
    user_config.filter_system_list_tag = filter_system_list_tag
    user_config.filter_system_list_keep = filter_system_list_keep
    # save config
    user_config.save()

    # return to test
    return

class SystemFilterViewTestCase(TestCase):
    """ system filter view tests """

    @classmethod
    def setUpTestData(cls):
        """ one time setup """

        # create user
        test_user = User.objects.create_user(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')

        # create config
        UserConfigModel.objects.create(user_config_username=test_user)

        # case
        Case.objects.create(
            case_name = 'case_1',
            case_is_incident = True,
            case_created_by_user_id = test_user,
        )

        # systemstatus
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # tagcolor
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # tag
        Tag.objects.create(tag_name='tag_1', tagcolor = tagcolor_1)

        # no case / no tag
        System.objects.create(
            system_name = 'system_plain',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # 1 case / no tag
        system_case = System.objects.create(
            system_name = 'system_case',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        system_case.case.set(Case.objects.filter(case_name='case_1'))

        # no case / 1 tag
        system_tag = System.objects.create(
            system_name = 'system_tag',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        system_tag.tag.set(Tag.objects.filter(tag_name='tag_1'))

        # 1 case / 1 tag
        system_both = System.objects.create(
            system_name = 'system_both',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        system_both.case.set(Case.objects.filter(case_name='case_1'))
        system_both.tag.set(Tag.objects.filter(tag_name='tag_1'))

    def test_system_list_no_filter_context(self):
        """ no filter applied """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        set_user_config(test_user, None, None)

        # get response with default JSON request
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        # compare
        self.assertContains(response, system_plain.system_name)
        self.assertContains(response, system_case.system_name)
        self.assertContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_case_filter_context(self):
        """ case filter applied """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        set_user_config(test_user, case_1, None)

        # get response with default JSON request
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_tag_filter_context(self):
        """ tag filter applied """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, None, tag_1)

        # get response with default JSON request
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_case_and_tag_filter_context(self):
        """ case and tag filter applied """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # get response with default JSON request
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_search_filter_context(self):
        """ case and tag filter applied in conjunction with datatable search """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # add additional system
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        system_very_unique_name = System.objects.create(
            system_name = 'system_very_unique_name',
            systemstatus = systemstatus_1,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_very_unique_name.case.set(Case.objects.filter(case_name='case_1'))
        system_very_unique_name.tag.set(Tag.objects.filter(tag_name='tag_1'))

        # get response with default JSON request
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': 'system_very_unique_name', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertNotContains(response, system_both.system_name)
        self.assertContains(response, system_very_unique_name.system_name)

    def test_system_list_keep_filter(self):
        """ keep filter settings via config setting """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1, True)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)

        # compare - settings before request
        self.assertEqual(user_config.filter_system_list_case, case_1)
        self.assertEqual(user_config.filter_system_list_tag, tag_1)
        self.assertEqual(user_config.filter_system_list_keep, True)

        # get response, should keep filter config
        self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_system_list_case, case_1)
        self.assertEqual(user_config.filter_system_list_tag, tag_1)
        self.assertEqual(user_config.filter_system_list_keep, True)

    def test_system_list_reset_filter(self):
        """ reset filter settings via config setting """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1, False)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)

        # compare - settings before request
        self.assertEqual(user_config.filter_system_list_case, case_1)
        self.assertEqual(user_config.filter_system_list_tag, tag_1)
        self.assertEqual(user_config.filter_system_list_keep, False)

        # get response, should reset filter config
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_system_list_case, None)
        self.assertEqual(user_config.filter_system_list_tag, None)
        self.assertEqual(user_config.filter_system_list_keep, False)
        # compare - filter active for the last time
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

        # get response again, filter should not be active any more
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/system/')
        # compare - filter inactive
        self.assertContains(response, system_plain.system_name)
        self.assertContains(response, system_case.system_name)
        self.assertContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_get_without_json(self):
        """ call of '/system/' alone does not touch config regardless of keep value """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1, False)

        # get response
        self.client.get('/system/')

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertEqual(user_config.filter_system_list_case, case_1)
        self.assertEqual(user_config.filter_system_list_tag, tag_1)
        self.assertEqual(user_config.filter_system_list_keep, False)

    def test_system_list_post_empty(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1, True)

        # create post data, empty string has to be provided to avoid MultiValueDictKeyError because these fields are not part of ModelForm
        data_dict = {
            'case': '',
            'tag': '',
        }
        # get response
        self.client.post('/system/', data_dict)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertEqual(user_config.filter_system_list_case, None)
        self.assertEqual(user_config.filter_system_list_tag, None)
        self.assertEqual(user_config.filter_system_list_keep, False)

    def test_system_list_post_all(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        set_user_config(test_user, None, None, False)

        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create post data
        data_dict = {
            'case': case_1.case_id,
            'tag': tag_1.tag_id,
            'filter_system_list_keep': 'on',
        }
        # get response
        self.client.post('/system/', data_dict)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertEqual(user_config.filter_system_list_case, case_1)
        self.assertEqual(user_config.filter_system_list_tag, tag_1)
        self.assertEqual(user_config.filter_system_list_keep, True)

    def test_system_clear_filter_not_logged_in(self):
        """ test clear_filter view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/clear_filter/', safe='')
        # get response
        response = self.client.get('/system/clear_filter/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_clear_filter_redirect(self):
        """ test clear_filter view """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/clear_filter/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_clear_filter_config(self):
        """ reset filter settings via URL """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1, False)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)

        # compare - settings before request
        self.assertEqual(user_config.filter_system_list_case, case_1)
        self.assertEqual(user_config.filter_system_list_tag, tag_1)
        self.assertEqual(user_config.filter_system_list_keep, False)

        # get response, should reset filter config
        self.client.get('/system/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_system_list_case, None)
        self.assertEqual(user_config.filter_system_list_tag, None)
        self.assertEqual(user_config.filter_system_list_keep, False)

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1, True)

        # refresh config
        user_config.refresh_from_db()
        # compare - settings before request
        self.assertEqual(user_config.filter_system_list_case, case_1)
        self.assertEqual(user_config.filter_system_list_tag, tag_1)
        self.assertEqual(user_config.filter_system_list_keep, True)

        # get response, should reset filter config
        self.client.get('/system/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_system_list_case, None)
        self.assertEqual(user_config.filter_system_list_tag, None)
        self.assertEqual(user_config.filter_system_list_keep, True)

    def test_system_json_direct_call_redirect(self):
        """ test redirect for direct JSON call """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/json/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_random_referer(self):
        """ test redirect for call with yet unknown referer """

        # login testuser
        self.client.login(username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6')
        # get response
        response = self.client.get('/system/json/', {'order[0][column]': '1', 'order[0][dir]': 'asc', 'start': '0', 'length': '25', 'search[value]': '', 'columns[1][data]': 'system_name', 'columns[2][data]': 'systemstatus',  'draw': '1'}, HTTP_REFERER='/future_feature/')
        # compare
        self.assertEqual(response.status_code, 200)
