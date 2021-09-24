import urllib.parse

from django.contrib.auth.models import User
from django.test import TestCase

from dfirtrack_main.models import (
    Case,
    Headline,
    Notestatus,
    Reportitem,
    System,
    Systemstatus,
    Tag,
    Tagcolor,
)


class ReportitemAPIViewTestCase(TestCase):
    """reportitem API view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )

        """ case """

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        """ headline """

        # create object
        headline_1 = Headline.objects.create(headline_name='headline_reportitem_api_1')

        """ notestatus """

        # create object
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')

        """ system """

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_api_1 = System.objects.create(
            system_name='system_api_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        """ tag """

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(
            tagcolor=tagcolor_1,
            tag_name='tag_1',
        )

        """ reportitem """

        # create object
        Reportitem.objects.create(
            headline=headline_1,
            reportitem_note='lorem ipsum',
            notestatus=notestatus_1,
            system=system_api_1,
            reportitem_created_by_user_id=test_user,
            reportitem_modified_by_user_id=test_user,
        )

    def test_reportitem_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/reportitem/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_reportitem_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # get response
        response = self.client.get('/api/reportitem/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_list_api_method_post(self):
        """POST is allowed"""

        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_reportitem_api').id
        # create object
        headline_reportitem_api_2 = Headline.objects.create(
            headline_name='headline_reportitem_api_2'
        )
        # get objects
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        system_api_1 = System.objects.get(system_name='system_api_1')
        # create POST string
        poststring = {
            "headline": headline_reportitem_api_2.headline_id,
            "reportitem_subheadline": "subheadline reportitem api 2",  # TODO: for some reason API requires reportitem_subheadline
            "reportitem_note": "lorem ipsum",
            "notestatus": notestatus_1.notestatus_id,
            "system": system_api_1.system_id,
            "reportitem_created_by_user_id": test_user_id,
            "reportitem_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        reportitem_api_2_none = Reportitem.objects.filter(
            headline=headline_reportitem_api_2
        )
        # compare
        self.assertEqual(len(reportitem_api_2_none), 0)
        # get response
        response = self.client.post(
            '/api/reportitem/', data=poststring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        reportitem_api_2 = Reportitem.objects.get(headline=headline_reportitem_api_2)
        # compare
        self.assertEqual(
            reportitem_api_2.reportitem_subheadline, 'subheadline reportitem api 2'
        )
        self.assertEqual(reportitem_api_2.reportitem_note, 'lorem ipsum')
        self.assertEqual(reportitem_api_2.notestatus, notestatus_1)
        self.assertEqual(reportitem_api_2.system, system_api_1)

    def test_reportitem_list_api_method_post_all_id(self):
        """POST is allowed"""

        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_reportitem_api').id
        # create object
        headline_reportitem_api_3 = Headline.objects.create(
            headline_name='headline_reportitem_api_3'
        )
        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        notestatus_1 = Notestatus.objects.get(notestatus_name='notestatus_1')
        system_api_1 = System.objects.get(system_name='system_api_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create POST string
        poststring = {
            "headline": headline_reportitem_api_3.headline_id,
            "reportitem_subheadline": "subheadline reportitem api 3",  # TODO: for some reason API requires reportitem_subheadline
            "reportitem_note": "lorem ipsum",
            "case": case_1.case_id,
            "notestatus": notestatus_1.notestatus_id,
            "system": system_api_1.system_id,
            "tag": [
                tag_1.tag_id,
            ],
            "reportitem_created_by_user_id": test_user_id,
            "reportitem_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        reportitem_api_3_none = Reportitem.objects.filter(
            headline=headline_reportitem_api_3
        )
        # compare
        self.assertEqual(len(reportitem_api_3_none), 0)
        # get response
        response = self.client.post(
            '/api/reportitem/', data=poststring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        reportitem_api_3 = Reportitem.objects.get(headline=headline_reportitem_api_3)
        # compare
        self.assertEqual(reportitem_api_3.headline, headline_reportitem_api_3)
        self.assertEqual(
            reportitem_api_3.reportitem_subheadline, 'subheadline reportitem api 3'
        )
        self.assertEqual(reportitem_api_3.reportitem_note, 'lorem ipsum')
        self.assertEqual(reportitem_api_3.case, case_1)
        self.assertEqual(reportitem_api_3.notestatus, notestatus_1)
        self.assertEqual(reportitem_api_3.system, system_api_1)
        self.assertTrue(reportitem_api_3.tag.filter(tag_name='tag_1').exists())

    def test_reportitem_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # create url
        destination = urllib.parse.quote('/api/reportitem/', safe='/')
        # get response
        response = self.client.get('/api/reportitem', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_reportitem_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        headline_reportitem_api_1 = Headline.objects.get(
            headline_name='headline_reportitem_api_1'
        )
        # get object
        reportitem_api_1 = Reportitem.objects.get(headline=headline_reportitem_api_1)
        # get response
        response = self.client.get(
            '/api/reportitem/' + str(reportitem_api_1.reportitem_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 401)

    def test_reportitem_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        headline_reportitem_api_1 = Headline.objects.get(
            headline_name='headline_reportitem_api_1'
        )
        # get object
        reportitem_api_1 = Reportitem.objects.get(headline=headline_reportitem_api_1)
        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # get response
        response = self.client.get(
            '/api/reportitem/' + str(reportitem_api_1.reportitem_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitem_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        headline_reportitem_api_1 = Headline.objects.get(
            headline_name='headline_reportitem_api_1'
        )
        # get object
        reportitem_api_1 = Reportitem.objects.get(headline=headline_reportitem_api_1)
        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # get response
        response = self.client.delete(
            '/api/reportitem/' + str(reportitem_api_1.reportitem_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_reportitem_detail_api_method_put(self):
        """PUT is allowed"""

        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_reportitem_api').id
        # get objects
        headline_reportitem_api_1 = Headline.objects.get(
            headline_name='headline_reportitem_api_1'
        )
        reportitem_api_1 = Reportitem.objects.get(headline=headline_reportitem_api_1)
        system_api_1 = System.objects.get(system_name='system_api_1')
        # create objects
        new_headline_reportitem_api_1 = Headline.objects.create(
            headline_name='new_headline_reportitem_api_1'
        )
        notestatus_2 = Notestatus.objects.create(notestatus_name='notestatus_2')
        # create url
        destination = urllib.parse.quote(
            '/api/reportitem/' + str(reportitem_api_1.reportitem_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "headline": new_headline_reportitem_api_1.headline_id,
            "reportitem_subheadline": "new subheadline reportitem api 1",  # TODO: for some reason API requires reportitem_subheadline
            "reportitem_note": "lorem ipsum",
            "notestatus": notestatus_2.notestatus_id,
            "system": system_api_1.system_id,
            "reportitem_created_by_user_id": test_user_id,
            "reportitem_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        new_reportitem_api_1 = Reportitem.objects.get(
            headline=new_headline_reportitem_api_1
        )
        # compare
        self.assertEqual(
            new_reportitem_api_1.reportitem_subheadline,
            'new subheadline reportitem api 1',
        )
        self.assertEqual(new_reportitem_api_1.reportitem_note, 'lorem ipsum')
        self.assertEqual(new_reportitem_api_1.notestatus, notestatus_2)
        self.assertEqual(new_reportitem_api_1.system, system_api_1)

    def test_reportitem_detail_api_method_put_all_id(self):
        """PUT is allowed"""

        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_reportitem_api').id
        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        headline_reportitem_api_1 = Headline.objects.get(
            headline_name='headline_reportitem_api_1'
        )
        reportitem_api_1 = Reportitem.objects.get(headline=headline_reportitem_api_1)
        system_api_1 = System.objects.get(system_name='system_api_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create objects
        new_headline_reportitem_api_2 = Headline.objects.create(
            headline_name='new_headline_reportitem_api_2'
        )
        notestatus_3 = Notestatus.objects.create(notestatus_name='notestatus_3')
        # create url
        destination = urllib.parse.quote(
            '/api/reportitem/' + str(reportitem_api_1.reportitem_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "headline": new_headline_reportitem_api_2.headline_id,
            "reportitem_subheadline": "new subheadline reportitem api 2",  # TODO: for some reason API requires reportitem_subheadline
            "reportitem_note": "lorem ipsum",
            "case": case_1.case_id,
            "notestatus": notestatus_3.notestatus_id,
            "system": system_api_1.system_id,
            "tag": [
                tag_1.tag_id,
            ],
            "reportitem_created_by_user_id": test_user_id,
            "reportitem_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        new_reportitem_api_2 = Reportitem.objects.get(
            headline=new_headline_reportitem_api_2
        )
        # compare
        self.assertEqual(
            new_reportitem_api_2.reportitem_subheadline,
            'new subheadline reportitem api 2',
        )
        self.assertEqual(new_reportitem_api_2.reportitem_note, 'lorem ipsum')
        self.assertEqual(new_reportitem_api_2.case, case_1)
        self.assertEqual(new_reportitem_api_2.notestatus, notestatus_3)
        self.assertEqual(new_reportitem_api_2.system, system_api_1)
        self.assertTrue(new_reportitem_api_2.tag.filter(tag_name='tag_1').exists())

    def test_reportitem_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        headline_reportitem_api_1 = Headline.objects.get(
            headline_name='headline_reportitem_api_1'
        )
        # get object
        reportitem_api_1 = Reportitem.objects.get(headline=headline_reportitem_api_1)
        # login testuser
        self.client.login(
            username='testuser_reportitem_api', password='8tFw47zfEbIdrAtyrOGg'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/reportitem/' + str(reportitem_api_1.reportitem_id) + '/', safe='/'
        )
        # get response
        response = self.client.get(
            '/api/reportitem/' + str(reportitem_api_1.reportitem_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
