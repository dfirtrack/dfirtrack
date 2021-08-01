import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import (
    Case,
    Casepriority,
    Casestatus,
    Note,
    Notestatus,
    Tag,
    Tagcolor,
)


class NoteViewTestCase(TestCase):
    """ note view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')

        # create object
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')

        # create object
        Note.objects.create(
            note_title = 'note_1',
            note_content = 'lorem ipsum',
            notestatus = notestatus_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # create object
        Tag.objects.create(tag_name='tag_1', tagcolor = tagcolor_1)

        # create objects
        casepriority_1 = Casepriority.objects.create(casepriority_name='casepriority_1')
        casestatus_1 = Casestatus.objects.create(casestatus_name='casestatus_1')

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
            casepriority = casepriority_1,
            casestatus = casestatus_1,
        )

    def test_note_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/note/', safe='')
        # get response
        response = self.client.get('/note/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_list_logged_in(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_list_template(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/note/note_list.html')

    def test_note_list_get_user_context(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_note')

    def test_note_list_redirect(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # create url
        destination = urllib.parse.quote('/note/', safe='/')
        # get response
        response = self.client.get('/note', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_note_detail_not_logged_in(self):
        """ test detail view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/note/' + str(note_1.note_id) + '/', safe='')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_detail_logged_in(self):
        """ test detail view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_detail_template(self):
        """ test detail view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/note/note_detail.html')

    def test_note_detail_get_user_context(self):
        """ test detail view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_note')

    def test_note_detail_redirect(self):
        """ test detail view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # create url
        destination = urllib.parse.quote('/note/' + str(note_1.note_id) + '/', safe='/')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_note_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/note/add/', safe='')
        # get response
        response = self.client.get('/note/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_add_logged_in(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_add_template(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/note/note_generic_form.html')

    def test_note_add_get_user_context(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_note')

    def test_note_add_redirect(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # create url
        destination = urllib.parse.quote('/note/add/', safe='/')
        # get response
        response = self.client.get('/note/add', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_note_add_post_redirect(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get objects
        notestatus_id = Notestatus.objects.get(notestatus_name = 'notestatus_1').notestatus_id
        # create post data
        data_dict = {
            'note_title': 'note_add_post_test',
            'note_content': 'lorem ipsum',
            'notestatus': notestatus_id,
        }
        # get response
        response = self.client.post('/note/add/', data_dict)
        # get object
        note_add_post_test = Note.objects.get(note_title='note_add_post_test')
        # create url
        destination = urllib.parse.quote('/note/' + str(note_add_post_test.note_id) + '/', safe='/')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(note_add_post_test.note_version, 1)

    def test_note_add_post_invalid_reload(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/note/add/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_add_post_invalid_template(self):
        """ test add view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/note/add/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/note/note_generic_form.html')

    def test_note_edit_not_logged_in(self):
        """ test edit view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/note/' + str(note_1.note_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_edit_logged_in(self):
        """ test edit view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_edit_template(self):
        """ test edit view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/note/note_generic_form.html')

    def test_note_edit_get_user_context(self):
        """ test edit view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_note')

    def test_note_edit_redirect(self):
        """ test edit view """

        # get object
        note_1 = Note.objects.get(note_title='note_1')
        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # create url
        destination = urllib.parse.quote('/note/' + str(note_1.note_id) + '/edit/', safe='/')
        # get response
        response = self.client.get('/note/' + str(note_1.note_id) + '/edit', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_note_edit_post_redirect(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get user
        test_user = User.objects.get(username='testuser_note')
        # get objects
        notestatus_1 = Notestatus.objects.get(notestatus_name = 'notestatus_1')
        # create object
        note_1 = Note.objects.create(
            note_title = 'note_edit_post_test_1',
            note_content = 'lorem ipsum',
            notestatus = notestatus_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )
        # get note version because it needs to be (hidden) part of the form
        note_version = Note.objects.get(note_title='note_edit_post_test_1').note_version
        # compare
        self.assertEqual(note_1.note_version, 1)
        # create post data
        data_dict = {
            'note_title': 'note_edit_post_test_2',
            'note_content': 'lorem ipsum',
            'note_version': note_version,
            'notestatus': notestatus_1.notestatus_id,
        }
        # get response
        response = self.client.post('/note/' + str(note_1.note_id) + '/edit/', data_dict)
        # create url
        destination = urllib.parse.quote('/note/' + str(note_1.note_id) + '/', safe='/')
        # get object
        note_edit_post_test_2 = Note.objects.get(note_title='note_edit_post_test_2')
        # compare
        self.assertEqual(note_edit_post_test_2.note_version, 2)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_edit_post_invalid_reload(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get object
        note_id = Note.objects.get(note_title='note_1').note_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/note/' + str(note_id) + '/edit/', data_dict)
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_edit_post_invalid_template(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get object
        note_id = Note.objects.get(note_title='note_1').note_id
        # create post data
        data_dict = {}
        # get response
        response = self.client.post('/note/' + str(note_id) + '/edit/', data_dict)
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/note/note_generic_form.html')

    def test_note_edit_documentation_redirect(self):
        """ test note edit documentation redirect """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get object
        note_1 = Note.objects.get(note_title='note_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # create post data
        data_dict = data_dict = {
            'note_title': note_1.note_title,
            'note_content': 'lorem ipsum',
            'note_version': note_1.note_version,
            'notestatus': notestatus_1.notestatus_id,
        }
        # get response
        response = self.client.post('/note/' + str(note_1.note_id) + '/edit/?documentation', data_dict)
        # create url
        destination = urllib.parse.quote(f'/documentation/#note_id_{note_1.note_id}', safe='/#')

        # check
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_add_documentation_redirect(self):
        """ test note add documentation redirect """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # create post data
        data_dict = data_dict = {
            'note_title': "test add note redirect",
            'note_content': 'lorem ipsum',
            'notestatus': notestatus_1.notestatus_id,
        }
        # get response
        response = self.client.post('/note/add/?documentation', data_dict)
        # get latest note
        new_note = Note.objects.latest('note_create_time')
        # create url
        destination = urllib.parse.quote(f'/documentation/#note_id_{new_note.note_id}', safe='/#')

        # check
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_edit_valid_tag(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get user
        test_user = User.objects.get(username='testuser_note')
        # get objects
        notestatus_1 = Notestatus.objects.get(notestatus_name = 'notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create object
        note_1 = Note.objects.create(
            note_title = 'tag_note_edit_post_test_1',
            note_content = 'lorem ipsum',
            notestatus = notestatus_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'note_title': 'tag_note_edit_post_test_2',
            'note_content': 'lorem ipsum',
            'note_version': note_1.note_version,
            'notestatus': notestatus_1.notestatus_id,
            'tag': [tag_1.tag_id, ]
        }
        # get response
        response = self.client.post('/note/' + str(note_1.note_id) + '/edit/', data_dict)
        # create url
        destination = urllib.parse.quote('/note/' + str(note_1.note_id) + '/', safe='/')
        # get object
        note_edit_post_test_2 = Note.objects.get(note_title='tag_note_edit_post_test_2')
        # compare
        self.assertEqual(len(note_edit_post_test_2.tag.all()), 1)
        self.assertEqual(note_edit_post_test_2.tag.all()[0].tag_name, 'tag_1')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_note_edit_valid_case(self):
        """ test edit view """

        # login testuser
        self.client.login(username='testuser_note', password='oh8Szsuk8BpbEJ1RRL21')
        # get user
        test_user = User.objects.get(username='testuser_note')
        # get objects
        notestatus_1 = Notestatus.objects.get(notestatus_name = 'notestatus_1')
        case_1 = Case.objects.get(case_name='case_1')
        # create object
        note_1 = Note.objects.create(
            note_title = 'case_note_edit_post_test_1',
            note_content = 'lorem ipsum',
            notestatus = notestatus_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )
        # create post data
        data_dict = {
            'note_title': 'case_note_edit_post_test_2',
            'note_content': 'lorem ipsum',
            'note_version': note_1.note_version,
            'notestatus': notestatus_1.notestatus_id,
            'case': [case_1.case_id, ]
        }
        # get response
        response = self.client.post('/note/' + str(note_1.note_id) + '/edit/', data_dict)
        # create url
        destination = urllib.parse.quote('/note/' + str(note_1.note_id) + '/', safe='/')
        # get object
        note_edit_post_test_2 = Note.objects.get(note_title='case_note_edit_post_test_2')
        # compare
        self.assertEqual(note_edit_post_test_2.case.case_name, 'case_1')
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
