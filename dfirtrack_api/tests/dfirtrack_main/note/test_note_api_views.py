import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import Case, Note, Notestatus, Tag, Tagcolor


class NoteAPIViewTestCase(TestCase):
    """note API view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd'
        )

        # create object
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')

        """ case """

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        """ tag """

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(
            tagcolor=tagcolor_1,
            tag_name='tag_1',
        )

        """ note """

        # create object - main testing note
        Note.objects.create(
            note_title='note_api_1',
            notestatus=notestatus_1,
            note_created_by_user_id=test_user,
            note_modified_by_user_id=test_user,
        )

    def test_note_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/note/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_note_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get response
        response = self.client.get('/api/note/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_list_api_method_post(self):
        """POST is allowed"""

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get user
        test_user_id = User.objects.get(username='testuser_note_api').id
        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        # create POST string
        poststring = {
            "note_title": "note_api_2",
            "note_content": "lorem ipsum",
            "note_version": 0,
            "notestatus": notestatus_1.notestatus_id,
            "note_created_by_user_id": test_user_id,
            "note_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        note_api_2_none = Note.objects.filter(note_title='note_api_2')
        # compare
        self.assertEqual(len(note_api_2_none), 0)
        # get response
        response = self.client.post(
            '/api/note/', data=poststring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        note_api_2 = Note.objects.get(note_title='note_api_2')
        # compare
        self.assertEqual(note_api_2.note_title, 'note_api_2')
        self.assertEqual(note_api_2.note_content, 'lorem ipsum')
        self.assertEqual(note_api_2.note_version, 1)
        self.assertEqual(note_api_2.notestatus, notestatus_1)

    def test_note_list_api_method_post_all_id(self):
        """POST is allowed"""

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get user
        test_user_id = User.objects.get(username='testuser_note_api').id
        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create POST string
        poststring = {
            "note_title": "note_api_3",
            "note_content": "lorem ipsum",
            "note_version": 0,
            "case": case_1.case_id,
            "notestatus": notestatus_1.notestatus_id,
            "tag": [
                tag_1.tag_id,
            ],
            "note_created_by_user_id": test_user_id,
            "note_modified_by_user_id": test_user_id,
            "note_assigned_to_user_id": test_user_id,
        }
        # check for existence of object
        note_api_3_none = Note.objects.filter(note_title='note_api_3')
        # compare
        self.assertEqual(len(note_api_3_none), 0)
        # get response
        response = self.client.post(
            '/api/note/', data=poststring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        note_api_3 = Note.objects.get(note_title='note_api_3')
        # compare
        self.assertEqual(note_api_3.note_title, 'note_api_3')
        self.assertEqual(note_api_3.note_content, 'lorem ipsum')
        self.assertEqual(note_api_3.note_version, 1)
        self.assertEqual(note_api_3.case, case_1)
        self.assertEqual(note_api_3.notestatus, notestatus_1)
        self.assertTrue(note_api_3.tag.filter(tag_name='tag_1').exists())

    def test_note_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # create url
        destination = urllib.parse.quote('/api/note/', safe='/')
        # get response
        response = self.client.get('/api/note', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_note_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # get response
        response = self.client.get('/api/note/' + str(note_api_1.note_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_note_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get response
        response = self.client.get('/api/note/' + str(note_api_1.note_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get response
        response = self.client.delete('/api/note/' + str(note_api_1.note_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_note_detail_api_method_put(self):
        """PUT is allowed"""

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get user
        test_user_id = User.objects.get(username='testuser_note_api').id
        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # create objects
        notestatus_2 = Notestatus.objects.create(notestatus_name='notestatus_2')
        # create url
        destination = urllib.parse.quote(
            '/api/note/' + str(note_api_1.note_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "note_title": "new_note_api_1",
            "note_content": "lorem ipsum",
            "note_version": 1,
            "notestatus": notestatus_2.notestatus_id,
            "note_created_by_user_id": test_user_id,
            "note_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        new_note_api_1 = Note.objects.get(note_title='new_note_api_1')
        # compare
        self.assertEqual(new_note_api_1.note_title, 'new_note_api_1')
        self.assertEqual(new_note_api_1.note_content, 'lorem ipsum')
        self.assertEqual(new_note_api_1.note_version, 2)
        self.assertEqual(new_note_api_1.notestatus, notestatus_2)

    def test_note_detail_api_method_put_all_id(self):
        """PUT is allowed"""

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get user
        test_user_id = User.objects.get(username='testuser_note_api').id
        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create objects
        notestatus_3 = Notestatus.objects.create(notestatus_name='notestatus_3')
        # create url
        destination = urllib.parse.quote(
            '/api/note/' + str(note_api_1.note_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "note_title": "new_note_api_2",
            "note_content": "lorem ipsum",
            "note_version": 1,
            "case": case_1.case_id,
            "notestatus": notestatus_3.notestatus_id,
            "tag": [
                tag_1.tag_id,
            ],
            "note_created_by_user_id": test_user_id,
            "note_modified_by_user_id": test_user_id,
            "note_assigned_to_user_id": test_user_id,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        new_note_api_2 = Note.objects.get(note_title='new_note_api_2')
        # compare
        self.assertEqual(new_note_api_2.note_title, 'new_note_api_2')
        self.assertEqual(new_note_api_2.note_content, 'lorem ipsum')
        self.assertEqual(new_note_api_2.note_version, 2)
        self.assertEqual(new_note_api_2.case, case_1)
        self.assertEqual(new_note_api_2.notestatus, notestatus_3)
        self.assertTrue(new_note_api_2.tag.filter(tag_name='tag_1').exists())

    def test_note_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # create url
        destination = urllib.parse.quote(
            '/api/note/' + str(note_api_1.note_id) + '/', safe='/'
        )
        # get response
        response = self.client.get('/api/note/' + str(note_api_1.note_id), follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
