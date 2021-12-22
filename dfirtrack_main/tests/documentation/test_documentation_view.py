import urllib.parse

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import (
    Case,
    Headline,
    Note,
    Notestatus,
    Reportitem,
    System,
    Systemstatus,
    Tag,
    Tagcolor,
)


def set_user_config(
    test_user,
    filter_documentation_list_case,
    filter_documentation_list_notestatus,
    filter_documentation_list_tag,
    filter_documentation_list_keep=True,
):
    """set user config"""

    # get config
    user_config = UserConfigModel.objects.get(user_config_username=test_user)
    # set values
    user_config.filter_documentation_list_case = filter_documentation_list_case
    user_config.filter_documentation_list_notestatus = (
        filter_documentation_list_notestatus
    )
    user_config.filter_documentation_list_tag = filter_documentation_list_tag
    user_config.filter_documentation_list_keep = filter_documentation_list_keep
    # save config
    user_config.save()

    # return to test
    return


class DocumentationViewTestCase(TestCase):
    """documentation view tests"""

    @classmethod
    def setUpTestData(cls):
        """one time setup"""

        # create user
        test_user = User.objects.create_user(
            username='testuser_documentation', password='dRekxM3R5frr'
        )

        # create config
        UserConfigModel.objects.create(user_config_username=test_user)

        # case
        case_1 = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        # headline
        headline_1 = Headline.objects.create(headline_name='headline_1')

        # notestatus
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')
        Notestatus.objects.create(notestatus_name='notestatus_2')

        # systemstatus
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # system
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # tagcolor
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # tag
        Tag.objects.create(tag_name='tag_1', tagcolor=tagcolor_1)

        """ notes """

        # no case / no tag
        Note.objects.create(
            note_title='note_plain',
            note_content='lorem ipsum',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
        )

        # 1 case / no tag
        Note.objects.create(
            note_title='note_case',
            note_content='lorem ipsum',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
            case=case_1,
        )

        # no case / 1 tag
        note_tag = Note.objects.create(
            note_title='note_tag',
            note_content='lorem ipsum',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
        )

        note_tag.tag.set(Tag.objects.filter(tag_name='tag_1'))

        # 1 case / 1 tag
        note_both = Note.objects.create(
            note_title='note_both',
            note_content='lorem ipsum',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
            case=case_1,
        )

        note_both.tag.set(Tag.objects.filter(tag_name='tag_1'))

        """ reportitems """

        # no case / no tag
        Reportitem.objects.create(
            reportitem_note='reportitem_plain',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
        )

        # 1 case / no tag
        Reportitem.objects.create(
            reportitem_note='reportitem_case',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
            case=case_1,
        )

        # no case / 1 tag
        reportitem_tag = Reportitem.objects.create(
            reportitem_note='reportitem_tag',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
        )

        reportitem_tag.tag.set(Tag.objects.filter(tag_name='tag_1'))

        # 1 case / 1 tag
        reportitem_both = Reportitem.objects.create(
            reportitem_note='reportitem_both',
            headline=headline_1,
            notestatus=notestatus_1,
            system=system_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
            case=case_1,
        )

        reportitem_both.tag.set(Tag.objects.filter(tag_name='tag_1'))

    def test_documentation_list_not_logged_in(self):
        """test list view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/documentation/', safe='')
        # get response
        response = self.client.get('/documentation/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_documentation_list_logged_in(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_documentation_list_template(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_main/documentation/documentation_list.html'
        )

    def test_documentation_list_get_user_context(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_documentation')

    def test_documentation_list_redirect(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # create url
        destination = urllib.parse.quote('/documentation/', safe='/')
        # get response
        response = self.client.get('/documentation', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_documentation_list_no_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        note_plain = Note.objects.get(note_title='note_plain')
        note_case = Note.objects.get(note_title='note_case')
        note_tag = Note.objects.get(note_title='note_tag')
        note_both = Note.objects.get(note_title='note_both')
        reportitem_plain = Reportitem.objects.get(reportitem_note='reportitem_plain')
        reportitem_case = Reportitem.objects.get(reportitem_note='reportitem_case')
        reportitem_tag = Reportitem.objects.get(reportitem_note='reportitem_tag')
        reportitem_both = Reportitem.objects.get(reportitem_note='reportitem_both')

        # change config
        set_user_config(test_user, None, None, None)

        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertContains(response, note_plain.note_title)
        self.assertContains(response, note_case.note_title)
        self.assertContains(response, note_tag.note_title)
        self.assertContains(response, note_both.note_title)
        self.assertContains(response, reportitem_plain.reportitem_note)
        self.assertContains(response, reportitem_case.reportitem_note)
        self.assertContains(response, reportitem_tag.reportitem_note)
        self.assertContains(response, reportitem_both.reportitem_note)

    def test_documentation_list_case_filter_context(self):
        """case filter applied"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        note_plain = Note.objects.get(note_title='note_plain')
        note_case = Note.objects.get(note_title='note_case')
        note_tag = Note.objects.get(note_title='note_tag')
        note_both = Note.objects.get(note_title='note_both')
        reportitem_plain = Reportitem.objects.get(reportitem_note='reportitem_plain')
        reportitem_case = Reportitem.objects.get(reportitem_note='reportitem_case')
        reportitem_tag = Reportitem.objects.get(reportitem_note='reportitem_tag')
        reportitem_both = Reportitem.objects.get(reportitem_note='reportitem_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        set_user_config(test_user, case_1, None, None)

        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertNotContains(response, note_plain.note_title)
        self.assertContains(response, note_case.note_title)
        self.assertNotContains(response, note_tag.note_title)
        self.assertContains(response, note_both.note_title)
        self.assertNotContains(response, reportitem_plain.reportitem_note)
        self.assertContains(response, reportitem_case.reportitem_note)
        self.assertNotContains(response, reportitem_tag.reportitem_note)
        self.assertContains(response, reportitem_both.reportitem_note)

    def test_documentation_list_notestatus_filter_context(self):
        """notestatus filter applied"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        note_plain = Note.objects.get(note_title='note_plain')
        note_case = Note.objects.get(note_title='note_case')
        note_tag = Note.objects.get(note_title='note_tag')
        note_both = Note.objects.get(note_title='note_both')
        reportitem_plain = Reportitem.objects.get(reportitem_note='reportitem_plain')
        reportitem_case = Reportitem.objects.get(reportitem_note='reportitem_case')
        reportitem_tag = Reportitem.objects.get(reportitem_note='reportitem_tag')
        reportitem_both = Reportitem.objects.get(reportitem_note='reportitem_both')

        # change config
        notestatus_2 = Notestatus.objects.get(notestatus_name='notestatus_2')
        set_user_config(test_user, None, notestatus_2, None)

        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertNotContains(response, note_plain.note_title)
        self.assertNotContains(response, note_case.note_title)
        self.assertNotContains(response, note_tag.note_title)
        self.assertNotContains(response, note_both.note_title)
        self.assertNotContains(response, reportitem_plain.reportitem_note)
        self.assertNotContains(response, reportitem_case.reportitem_note)
        self.assertNotContains(response, reportitem_tag.reportitem_note)
        self.assertNotContains(response, reportitem_both.reportitem_note)

    def test_documentation_list_tag_filter_context(self):
        """tag filter applied"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        note_plain = Note.objects.get(note_title='note_plain')
        note_case = Note.objects.get(note_title='note_case')
        note_tag = Note.objects.get(note_title='note_tag')
        note_both = Note.objects.get(note_title='note_both')
        reportitem_plain = Reportitem.objects.get(reportitem_note='reportitem_plain')
        reportitem_case = Reportitem.objects.get(reportitem_note='reportitem_case')
        reportitem_tag = Reportitem.objects.get(reportitem_note='reportitem_tag')
        reportitem_both = Reportitem.objects.get(reportitem_note='reportitem_both')

        # change config
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, None, None, tag_1)

        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertNotContains(response, note_plain.note_title)
        self.assertNotContains(response, note_case.note_title)
        self.assertContains(response, note_tag.note_title)
        self.assertContains(response, note_both.note_title)
        self.assertNotContains(response, reportitem_plain.reportitem_note)
        self.assertNotContains(response, reportitem_case.reportitem_note)
        self.assertContains(response, reportitem_tag.reportitem_note)
        self.assertContains(response, reportitem_both.reportitem_note)

    def test_documentation_list_case_and_tag_filter_context(self):
        """case and tag filter applied"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        note_plain = Note.objects.get(note_title='note_plain')
        note_case = Note.objects.get(note_title='note_case')
        note_tag = Note.objects.get(note_title='note_tag')
        note_both = Note.objects.get(note_title='note_both')
        reportitem_plain = Reportitem.objects.get(reportitem_note='reportitem_plain')
        reportitem_case = Reportitem.objects.get(reportitem_note='reportitem_case')
        reportitem_tag = Reportitem.objects.get(reportitem_note='reportitem_tag')
        reportitem_both = Reportitem.objects.get(reportitem_note='reportitem_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, None, tag_1)

        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertNotContains(response, note_plain.note_title)
        self.assertNotContains(response, note_case.note_title)
        self.assertNotContains(response, note_tag.note_title)
        self.assertContains(response, note_both.note_title)
        self.assertNotContains(response, reportitem_plain.reportitem_note)
        self.assertNotContains(response, reportitem_case.reportitem_note)
        self.assertNotContains(response, reportitem_tag.reportitem_note)
        self.assertContains(response, reportitem_both.reportitem_note)

    def test_documentation_list_all_filter_context(self):
        """all filters applied"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        note_plain = Note.objects.get(note_title='note_plain')
        note_case = Note.objects.get(note_title='note_case')
        note_tag = Note.objects.get(note_title='note_tag')
        note_both = Note.objects.get(note_title='note_both')
        reportitem_plain = Reportitem.objects.get(reportitem_note='reportitem_plain')
        reportitem_case = Reportitem.objects.get(reportitem_note='reportitem_case')
        reportitem_tag = Reportitem.objects.get(reportitem_note='reportitem_tag')
        reportitem_both = Reportitem.objects.get(reportitem_note='reportitem_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, notestatus_1, tag_1)

        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertNotContains(response, note_plain.note_title)
        self.assertNotContains(response, note_case.note_title)
        self.assertNotContains(response, note_tag.note_title)
        self.assertContains(response, note_both.note_title)
        self.assertNotContains(response, reportitem_plain.reportitem_note)
        self.assertNotContains(response, reportitem_case.reportitem_note)
        self.assertNotContains(response, reportitem_tag.reportitem_note)
        self.assertContains(response, reportitem_both.reportitem_note)

    def test_documentation_list_keep_filter(self):
        """keep filter settings via config setting"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, notestatus_1, tag_1, True)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)

        # compare - settings before request
        self.assertEqual(user_config.filter_documentation_list_case, case_1)
        self.assertEqual(user_config.filter_documentation_list_notestatus, notestatus_1)
        self.assertEqual(user_config.filter_documentation_list_tag, tag_1)
        self.assertEqual(user_config.filter_documentation_list_keep, True)

        # get response, should keep filter config
        self.client.get('/documentation/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_documentation_list_case, case_1)
        self.assertEqual(user_config.filter_documentation_list_notestatus, notestatus_1)
        self.assertEqual(user_config.filter_documentation_list_tag, tag_1)
        self.assertEqual(user_config.filter_documentation_list_keep, True)

    def test_documentation_list_reset_filter(self):
        """reset filter settings via config setting"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        note_plain = Note.objects.get(note_title='note_plain')
        note_case = Note.objects.get(note_title='note_case')
        note_tag = Note.objects.get(note_title='note_tag')
        note_both = Note.objects.get(note_title='note_both')
        reportitem_plain = Reportitem.objects.get(reportitem_note='reportitem_plain')
        reportitem_case = Reportitem.objects.get(reportitem_note='reportitem_case')
        reportitem_tag = Reportitem.objects.get(reportitem_note='reportitem_tag')
        reportitem_both = Reportitem.objects.get(reportitem_note='reportitem_both')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, notestatus_1, tag_1, False)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)

        # compare - settings before request
        self.assertEqual(user_config.filter_documentation_list_case, case_1)
        self.assertEqual(user_config.filter_documentation_list_notestatus, notestatus_1)
        self.assertEqual(user_config.filter_documentation_list_tag, tag_1)
        self.assertEqual(user_config.filter_documentation_list_keep, False)

        # get response, should reset filter config
        response = self.client.get('/documentation/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_documentation_list_case, None)
        self.assertEqual(user_config.filter_documentation_list_notestatus, None)
        self.assertEqual(user_config.filter_documentation_list_tag, None)
        self.assertEqual(user_config.filter_documentation_list_keep, False)
        # compare - filter active for the last time
        self.assertNotContains(response, note_plain.note_title)
        self.assertNotContains(response, note_case.note_title)
        self.assertNotContains(response, note_tag.note_title)
        self.assertContains(response, note_both.note_title)
        self.assertNotContains(response, reportitem_plain.reportitem_note)
        self.assertNotContains(response, reportitem_case.reportitem_note)
        self.assertNotContains(response, reportitem_tag.reportitem_note)
        self.assertContains(response, reportitem_both.reportitem_note)

        # get response again, filter should not be active any more
        response = self.client.get('/documentation/')
        # compare - filter inactive
        self.assertContains(response, note_plain.note_title)
        self.assertContains(response, note_case.note_title)
        self.assertContains(response, note_tag.note_title)
        self.assertContains(response, note_both.note_title)
        self.assertContains(response, reportitem_plain.reportitem_note)
        self.assertContains(response, reportitem_case.reportitem_note)
        self.assertContains(response, reportitem_tag.reportitem_note)
        self.assertContains(response, reportitem_both.reportitem_note)

    def test_documentation_list_post_empty(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # create post data, empty string has to be provided to avoid MultiValueDictKeyError because these fields are not part of ModelForm
        data_dict = {
            'case': '',
            'notestatus': '',
            'tag': '',
        }

        # get response
        self.client.post('/documentation/', data_dict)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertEqual(user_config.filter_documentation_list_case, None)
        self.assertEqual(user_config.filter_documentation_list_notestatus, None)
        self.assertEqual(user_config.filter_documentation_list_tag, None)
        self.assertEqual(user_config.filter_documentation_list_keep, False)

    def test_documentation_list_post_all(self):
        """test list view"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')
        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create post data
        data_dict = {
            'case': case_1.case_id,
            'notestatus': notestatus_1.notestatus_id,
            'tag': tag_1.tag_id,
            'filter_documentation_list_keep': 'on',
        }

        # get response
        self.client.post('/documentation/', data_dict)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)
        # compare
        self.assertEqual(user_config.filter_documentation_list_case, case_1)
        self.assertEqual(user_config.filter_documentation_list_notestatus, notestatus_1)
        self.assertEqual(user_config.filter_documentation_list_tag, tag_1)
        self.assertEqual(user_config.filter_documentation_list_keep, True)

    def test_documentation_clear_filter_not_logged_in(self):
        """test clear_filter view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/documentation/clear_filter/', safe=''
        )
        # get response
        response = self.client.get('/documentation/clear_filter/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_documentation_clear_filter_redirect(self):
        """test clear_filter view"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # create url
        destination = urllib.parse.quote('/documentation/', safe='/')
        # get response
        response = self.client.get('/documentation/clear_filter/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_documentation_clear_filter_config(self):
        """clear filter settings via URL"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get user
        test_user = User.objects.get(username='testuser_documentation')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, notestatus_1, tag_1, False)

        # get config
        user_config = UserConfigModel.objects.get(user_config_username=test_user)

        # compare - settings before request
        self.assertEqual(user_config.filter_documentation_list_case, case_1)
        self.assertEqual(user_config.filter_documentation_list_notestatus, notestatus_1)
        self.assertEqual(user_config.filter_documentation_list_tag, tag_1)
        self.assertEqual(user_config.filter_documentation_list_keep, False)

        # get response, should clear filter config, but keep 'filter_documentation_list_keep'
        self.client.get('/documentation/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_documentation_list_case, None)
        self.assertEqual(user_config.filter_documentation_list_notestatus, None)
        self.assertEqual(user_config.filter_documentation_list_tag, None)
        self.assertEqual(user_config.filter_documentation_list_keep, False)

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, notestatus_1, tag_1, True)

        # refresh config
        user_config.refresh_from_db()
        # compare - settings before request
        self.assertEqual(user_config.filter_documentation_list_case, case_1)
        self.assertEqual(user_config.filter_documentation_list_notestatus, notestatus_1)
        self.assertEqual(user_config.filter_documentation_list_tag, tag_1)
        self.assertEqual(user_config.filter_documentation_list_keep, True)

        # get response, should reset filter config, but keep 'filter_documentation_list_keep'
        self.client.get('/documentation/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_documentation_list_case, None)
        self.assertEqual(user_config.filter_documentation_list_notestatus, None)
        self.assertEqual(user_config.filter_documentation_list_tag, None)
        self.assertEqual(user_config.filter_documentation_list_keep, True)

    def test_documentation_list_filter_message(self):
        """test filter warning message"""

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')

        # get user
        test_user = User.objects.get(username='testuser_documentation')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        set_user_config(test_user, case_1, None, None, True)

        # get response
        response = self.client.get('/documentation/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(messages[0]), 'Filter is active. Items might be incomplete.'
        )
