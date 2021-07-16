from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Note
from dfirtrack_main.models import Notestatus
from dfirtrack_main.models import Case
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Tagcolor
import urllib.parse


class DocumentationViewTestCase(TestCase):
    """ documentation view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_documentation', password='dRekxM3R5frr')

        #create objects
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        #create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(tag_name='tag_1', tagcolor = tagcolor_1)

        # create object
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')

        # create object
        Note.objects.create(
            note_title='note_1',
            note_content = 'lorem ipsum',
            notestatus = notestatus_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )

    def test_documentation_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/documentation/', safe='')
        # get response
        response = self.client.get('/documentation/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_documentation_list_logged_in(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_documentation_list_template(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/documentation/documentation_list.html')

    def test_documentation_list_get_user_context(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get response
        response = self.client.get('/documentation/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_documentation')

    def test_documentation_list_redirect(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # create url
        destination = urllib.parse.quote('/documentation/', safe='/')
        # get response
        response = self.client.get('/documentation', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_documentation_filter_redirect(self):
        """ test list view """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # create url
        destination = urllib.parse.quote('/documentation/', safe='/')
        # get response
        response = self.client.get('/documentation', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_documentation_filter_case(self):
        """ test documentation filter """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get object
        case_1 = Case.objects.get(case_name='case_1')
        note_1 = Note.objects.get(note_title='note_1')
        test_user = User.objects.get(username='testuser_documentation')
        # create note
        case_note = Note.objects.create(
            note_title="Case Note Testcase",
            note_content="Lorem ipsum",
            case=case_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user
        )
        # create url
        filter_url = urllib.parse.quote(f'/documentation/?case={case_1.case_id}', safe='/?=')
        # get response
        response = self.client.get(filter_url, follow=True)

        # check
        self.assertContains(response, case_note.note_title)
        self.assertNotContains(response, note_1.note_title)

    def test_documentation_filter_tag(self):
        """ test documentation filter """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')
        note_1 = Note.objects.get(note_title='note_1')
        test_user = User.objects.get(username='testuser_documentation')
        # create note
        tag_note = Note.objects.create(
            note_title="Tag Note Testcase",
            note_content="Lorem ipsum",
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user
        )
        tag_note.tag.set(Tag.objects.filter(tag_name=tag_1.tag_name))
        # create url
        filter_url = urllib.parse.quote(f'/documentation/?tag={tag_1.tag_id}', safe='/?=')
        # get response
        response = self.client.get(filter_url, follow=True)

        # check
        self.assertContains(response, tag_note.note_title)
        self.assertNotContains(response, note_1.note_title)

    def test_documentation_filter_notestatus(self):
        """ test documentation filter """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get object
        notestatus_2 = Notestatus.objects.create(notestatus_name='notestatus_2')
        note_1 = Note.objects.get(note_title='note_1')
        test_user = User.objects.get(username='testuser_documentation')
        # create note
        notestatus_note = Note.objects.create(
            note_title="Tag Note Testcase",
            note_content="Lorem ipsum",
            notestatus=notestatus_2,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )
        # create url
        filter_url = urllib.parse.quote(f'/documentation/?notestatus={notestatus_2.notestatus_id}', safe='/?=')
        # get response
        response = self.client.get(filter_url, follow=True)

        # check
        self.assertContains(response, notestatus_note.note_title)
        self.assertNotContains(response, note_1.note_title)

    def test_documentation_form_data_redirect_case(self):
        """ test documentation form data redirect """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get object
        case_1 = Case.objects.get(case_name='case_1')

        form_data = {
            'case': case_1.case_id,
            'tag': '',
            'notestatus': ''
        }
        response = self.client.post('/documentation/', form_data)
        # create url
        destination = urllib.parse.quote(f'/documentation/?case={case_1.case_id}', safe='/?=')

        # check
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_documentation_form_data_redirect_tag(self):
        """ test documentation form data redirect """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get object
        tag_1 = Tag.objects.get(tag_name='tag_1')

        form_data = {
            'case': '',
            'tag': tag_1.tag_id,
            'notestatus': ''
        }
        response = self.client.post('/documentation/', form_data)
        # create url
        destination = urllib.parse.quote(f'/documentation/?tag={tag_1.tag_id}', safe='/?=')

        # check
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_documentation_form_data_redirect_notestatus(self):
        """ test documentation form data redirect """

        # login testuser
        self.client.login(username='testuser_documentation', password='dRekxM3R5frr')
        # get object
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')

        form_data = {
            'case': '',
            'tag': '',
            'notestatus': notestatus_1.notestatus_id
        }
        response = self.client.post('/documentation/', form_data)
        # create url
        destination = urllib.parse.quote(f'/documentation/?notestatus={notestatus_1.notestatus_id}', safe='/?=')

        # check
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
