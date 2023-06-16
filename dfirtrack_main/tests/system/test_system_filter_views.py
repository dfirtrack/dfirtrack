import urllib.parse

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import Case, System, Systemstatus, Tag, Tagcolor


def set_user_config(test_user, filter_list_case, filter_list_tag):
    """ " set user config"""

    # get config
    user_config = UserConfigModel.objects.get(
        user_config_username=test_user, filter_view='system_list'
    )
    # set values
    user_config.filter_list_case = filter_list_case
    if filter_list_tag:
        user_config.filter_list_tag.set(
            [
                filter_list_tag,
            ]
        )
    else:
        user_config.filter_list_tag.clear()
    # save config
    user_config.save()

    # return to test
    return


class SystemFilterViewTestCase(TestCase):
    """system filter view tests"""

    @classmethod
    def setUpTestData(cls):
        """one time setup"""

        # create user
        test_user = User.objects.create_user(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )

        # create config
        UserConfigModel.objects.create(
            user_config_username=test_user, filter_view='system_list'
        )

        # case
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        # systemstatus
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # tagcolor
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # tag
        Tag.objects.create(tag_name='tag_1', tagcolor=tagcolor_1)

        # no case / no tag
        System.objects.create(
            system_name='system_plain',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # 1 case / no tag
        system_case = System.objects.create(
            system_name='system_case',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        system_case.case.set(Case.objects.filter(case_name='case_1'))

        # no case / 1 tag
        system_tag = System.objects.create(
            system_name='system_tag',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        system_tag.tag.set(Tag.objects.filter(tag_name='tag_1'))

        # 1 case / 1 tag
        system_both = System.objects.create(
            system_name='system_both',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        system_both.case.set(Case.objects.filter(case_name='case_1'))
        system_both.tag.set(Tag.objects.filter(tag_name='tag_1'))

    def test_system_list_no_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
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
        response = self.client.post(
            '/filter/system/',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'system_name',
                'columns[2][data]': 'systemstatus',
                'draw': '1',
            },
        )
        # compare
        self.assertContains(response, system_plain.system_name)
        self.assertContains(response, system_case.system_name)
        self.assertContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_case_filter_context(self):
        """case filter applied"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
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
        response = self.client.post(
            '/filter/system/?system=all',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'system_name',
                'columns[2][data]': 'systemstatus',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_tag_filter_context(self):
        """tag filter applied"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
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
        response = self.client.post(
            '/filter/system/?system=all',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'system_name',
                'columns[2][data]': 'systemstatus',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_case_and_tag_filter_context(self):
        """case and tag filter applied"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
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
        response = self.client.post(
            '/filter/system/?system=all',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'system_name',
                'columns[2][data]': 'systemstatus',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_case_filter_json_provider(self):
        """case and tag filter applied"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')

        # get response with default JSON request
        response = self.client.post(
            f'/filter/system/?case={case_1.case_id}',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'system_name',
                'columns[2][data]': 'systemstatus',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_tag_filter_json_provider(self):
        """case and tag filter applied"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
        # get objects
        system_plain = System.objects.get(system_name='system_plain')
        system_case = System.objects.get(system_name='system_case')
        system_tag = System.objects.get(system_name='system_tag')
        system_both = System.objects.get(system_name='system_both')

        # change config
        tag_1 = Tag.objects.get(tag_name='tag_1')

        # get response with default JSON request
        response = self.client.post(
            f'/filter/system/?tag={tag_1.tag_id}',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'system_name',
                'columns[2][data]': 'systemstatus',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertContains(response, system_tag.system_name)
        self.assertContains(response, system_both.system_name)

    def test_system_list_search_filter_context(self):
        """case and tag filter applied in conjunction with datatable search"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
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
            system_name='system_very_unique_name',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )
        system_very_unique_name.case.set(Case.objects.filter(case_name='case_1'))
        system_very_unique_name.tag.set(Tag.objects.filter(tag_name='tag_1'))

        # get response with default JSON request
        response = self.client.post(
            '/filter/system/',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': 'system_very_unique_name',
                'columns[1][data]': 'system_name',
                'columns[2][data]': 'systemstatus',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, system_plain.system_name)
        self.assertNotContains(response, system_case.system_name)
        self.assertNotContains(response, system_tag.system_name)
        self.assertNotContains(response, system_both.system_name)
        self.assertContains(response, system_very_unique_name.system_name)

    def test_system_list_get_without_json(self):
        """call of '/system/' alone does not touch config regardless of keep value"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # get response
        self.client.get('/system/')

        # get config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='system_list'
        )
        # compare
        self.assertEqual(user_config.filter_list_case, case_1)
        self.assertEqual(user_config.filter_list_tag.first(), tag_1)

    def test_system_list_post_empty(self):
        """test list view"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # get config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='system_list'
        )

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # create post data, empty string has to be provided to avoid MultiValueDictKeyError because these fields are not part of ModelForm
        data_dict = {'user_config_id': user_config.user_config_id}
        # get response
        self.client.post('/system/', data_dict)

        # refresh user config object
        user_config.refresh_from_db()

        # compare
        self.assertEqual(user_config.filter_list_case, None)
        self.assertEqual(user_config.filter_list_tag.first(), None)

    def test_system_list_post_all(self):
        """test list view"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # get config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='system_list'
        )

        # change config
        set_user_config(test_user, None, None)

        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create post data
        data_dict = {
            'filter_list_case': case_1.case_id,
            'filter_list_tag': [
                tag_1.tag_id,
            ],
            'user_config_id': user_config.user_config_id,
        }
        # get response
        self.client.post('/system/', data_dict)

        # get config
        user_config.refresh_from_db()

        # compare
        self.assertEqual(user_config.filter_list_case, case_1)
        self.assertEqual(user_config.filter_list_tag.first(), tag_1)

    def test_system_clear_filter_not_logged_in(self):
        """test clear_filter view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/clear_filter/', safe=''
        )
        # get response
        response = self.client.get('/system/clear_filter/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_clear_filter_redirect(self):
        """test clear_filter view"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/clear_filter/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_clear_filter_config(self):
        """reset filter settings via URL"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # get config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='system_list'
        )

        # compare - settings before request
        self.assertEqual(user_config.filter_list_case, case_1)
        self.assertEqual(user_config.filter_list_tag.first(), tag_1)

        # get response, should reset filter config
        self.client.get('/system/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_list_case, None)
        self.assertEqual(user_config.filter_list_tag.first(), None)

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # refresh config
        user_config.refresh_from_db()
        # compare - settings before request
        self.assertEqual(user_config.filter_list_case, case_1)
        self.assertEqual(user_config.filter_list_tag.first(), tag_1)

        # get response, should reset filter config
        self.client.get('/system/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_list_case, None)
        self.assertEqual(user_config.filter_list_tag.first(), None)

    def test_system_list_filter_message(self):
        """test filter warning message"""

        # login testuser
        self.client.login(
            username='testuser_system_filter', password='9PUdBmEvJv5WCdFXEYf6'
        )

        # get user
        test_user = User.objects.get(username='testuser_system_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        set_user_config(test_user, case_1, None)

        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(messages[0]), 'Filter is active. Systems might be incomplete.'
        )
