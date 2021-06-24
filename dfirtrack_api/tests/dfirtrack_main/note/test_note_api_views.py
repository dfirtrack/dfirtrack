from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import Case
from dfirtrack_main.models import Note
from dfirtrack_main.models import Notestatus
from dfirtrack_main.models import Tag
from dfirtrack_main.models import Tagcolor
import urllib.parse


class NoteAPIViewTestCase(TestCase):
    """ note API view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')

        # create object
        notestatus_1 = Notestatus.objects.create(notestatus_name='notestatus_1')

        """ case """

        # create object
        Case.objects.create(
            case_name = 'case_1',
            case_is_incident = True,
            case_created_by_user_id = test_user,
        )

        """ tag """

        # create object
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')

        # create object
        Tag.objects.create(
            tagcolor = tagcolor_1,
            tag_name = 'tag_1',
        )

        """ note """

        # create object - main testing note
        Note.objects.create(
            note_title = 'note_api_1',
            notestatus = notestatus_1,
            note_created_by_user_id = test_user,
            note_modified_by_user_id = test_user,
        )

    def test_note_list_api_unauthorized(self):
        """ unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/note/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_note_list_api_method_get(self):
        """ GET is allowed """

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get response
        response = self.client.get('/api/note/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_list_api_method_post(self):
        """ POST is allowed """

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
            "note_version": 1,
            "notestatus": notestatus_1.notestatus_id,
            "note_created_by_user_id": test_user_id,
            "note_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        note_api_2_none = Note.objects.filter(note_title='note_api_2')
        # compare
        self.assertEqual(len(note_api_2_none), 0)
        # get response
        response = self.client.post('/api/note/', data=poststring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        note_api_2 = Note.objects.get(note_title='note_api_2')
        # compare
        self.assertEqual(note_api_2.notestatus, notestatus_1)

#    def test_note_list_api_method_post_all_id(self):
#        """ POST is allowed """
#
#        # login testuser
#        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
#        # get user
#        test_user_id = User.objects.get(username='testuser_note_api').id
#        # get objects
#        case_1 = Case.objects.get(case_name='case_1')
#        notestatus_1 = notestatus.objects.get(notestatus_name='notestatus_1')
#        tag_1 = Tag.objects.get(tag_name='tag_1')
#        # create POST string
#        poststring = {
#            "note_title": "note_api_3",
#            "analysisstatus": analysisstatus_1.analysisstatus_id,
#            "case": [
#                case_1.case_id,
#            ],
#            "company": [
#                company_1.company_id,
#            ],
#            "contact": contact_1.contact_id,
#            "dnsname": dnsname_1.dnsname_id,
#            "domain": domain_1.domain_id,
#            "host_note": host_note_1.note_id,
#            "ip": [
#                ip_1.ip_id,
#            ],
#            "location": location_1.location_id,
#            "os": os_1.os_id,
#            "osarch": osarch_1.osarch_id,
#            "reason": reason_1.reason_id,
#            "recommendation": recommendation_1.recommendation_id,
#            "serviceprovider": serviceprovider_1.serviceprovider_id,
#            "notestatus": notestatus_1.notestatus_id,
#            "systemtype": systemtype_1.systemtype_id,
#            "tag": [
#                tag_1.tag_id,
#            ],
#            "system_lastbooted_time": '2021-05-10T21:15',
#            "system_deprecated_time": '2021-05-10T21:25',
#            "system_is_vm": True,
#            "note_created_by_user_id": test_user_id,
#            "note_modified_by_user_id": test_user_id,
#            "system_export_markdown": False,
#            "system_export_spreadsheet": False,
#        }
#        # check for existence of object
#        note_api_3_none = Note.objects.filter(note_title='note_api_3')
#        # compare
#        self.assertEqual(len(note_api_3_none), 0)
#        # get response
#        response = self.client.post('/api/note/', data=poststring, content_type='application/json')
#        # compare
#        self.assertEqual(response.status_code, 201)
#        # get object
#        note_api_3 = System.objects.get(note_title='system_api_3')
#        # compare
#        self.assertEqual(system_api_3.analysisstatus, analysisstatus_1)
#        self.assertEqual(system_api_3.contact, contact_1)
#        self.assertEqual(system_api_3.dnsname, dnsname_1)
#        self.assertEqual(system_api_3.domain, domain_1)
#        self.assertEqual(system_api_3.host_system, host_system_1)
#        self.assertEqual(system_api_3.location, location_1)
#        self.assertEqual(system_api_3.os, os_1)
#        self.assertEqual(system_api_3.osarch, osarch_1)
#        self.assertEqual(system_api_3.reason, reason_1)
#        self.assertEqual(system_api_3.recommendation, recommendation_1)
#        self.assertEqual(system_api_3.serviceprovider, serviceprovider_1)
#        self.assertEqual(system_api_3.systemstatus, systemstatus_1)
#        self.assertEqual(system_api_3.systemtype, systemtype_1)
#        self.assertTrue(system_api_3.case.filter(case_name='case_1').exists())
#        self.assertTrue(system_api_3.company.filter(company_name='company_1').exists())
#        self.assertTrue(system_api_3.ip.filter(ip_ip='127.0.0.1').exists())
#        self.assertTrue(system_api_3.tag.filter(tag_name='tag_1').exists())
#        self.assertEqual(system_api_3.system_lastbooted_time, datetime(2021, 5, 10, 21, 15, tzinfo=timezone.utc))
#        self.assertEqual(system_api_3.system_deprecated_time, datetime(2021, 5, 10, 21, 25, tzinfo=timezone.utc))
#        self.assertTrue(system_api_3.system_is_vm)
#        self.assertFalse(system_api_3.system_export_markdown)
#        self.assertFalse(system_api_3.system_export_spreadsheet)

    def test_note_list_api_redirect(self):
        """ test redirect with appending slash """

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # create url
        destination = urllib.parse.quote('/api/note/', safe='/')
        # get response
        response = self.client.get('/api/note', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_note_detail_api_unauthorized (self):
        """ unauthorized access is forbidden"""

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # get response
        response = self.client.get('/api/note/' + str(note_api_1.note_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_note_detail_api_method_get(self):
        """ GET is allowed """

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get response
        response = self.client.get('/api/note/' + str(note_api_1.note_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_note_detail_api_method_delete(self):
        """ DELETE is forbidden """

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get response
        response = self.client.delete('/api/note/' + str(note_api_1.note_id) + '/')
        # compare
        self.assertEqual(response.status_code, 405)

    def test_note_detail_api_method_put(self):
        """ PUT is allowed """

        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # get user
        test_user_id = User.objects.get(username='testuser_note_api').id
        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # create objects
        notestatus_2 = Notestatus.objects.create(notestatus_name='notestatus_2')
        # create url
        destination = urllib.parse.quote('/api/note/' + str(note_api_1.note_id) + '/', safe='/')
        # create PUT string
        putstring = {
            "note_title": "new_note_api_1",
            "note_content": "lorem ipsum",
            "note_version": note_api_1.note_version,
            "notestatus": notestatus_2.notestatus_id,
            "note_created_by_user_id": test_user_id,
            "note_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(destination, data=putstring, content_type='application/json')
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        new_note_api_1 = Note.objects.get(note_title='new_note_api_1')
        # compare
        self.assertEqual(new_note_api_1.notestatus, notestatus_2)

#    def test_system_detail_api_method_put_all_id(self):
#        """ PUT is allowed """
#
#        # login testuser
#        self.client.login(username='testuser_system_api', password='2to8VdHRHNUcNS7CXmDd')
#        # get user
#        test_user_id = User.objects.get(username='testuser_system_api').id
#        # get object
#        system_api_1 = System.objects.get(note_title='system_api_1')
#        # get objects
#        case_1 = Case.objects.get(case_name='case_1')
#        company_1 = Company.objects.get(company_name='company_1')
#        contact_1 = Contact.objects.get(contact_name='contact_1')
#        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
#        domain_1 = Domain.objects.get(domain_name='domain_1')
#        host_system_1 = System.objects.get(note_title='host_system_api_1')
#        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
#        location_1 = Location.objects.get(location_name='location_1')
#        os_1 = Os.objects.get(os_name='os_1')
#        osarch_1 = Osarch.objects.get(osarch_name='osarch_1')
#        reason_1 = Reason.objects.get(reason_name='reason_1')
#        recommendation_1 = Recommendation.objects.get(recommendation_name='recommendation_1')
#        serviceprovider_1 = Serviceprovider.objects.get(serviceprovider_name='serviceprovider_1')
#        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
#        tag_1 = Tag.objects.get(tag_name='tag_1')
#        # create objects
#        analysisstatus_3 = Analysisstatus.objects.create(analysisstatus_name='analysisstatus_3')
#        systemstatus_3 = Systemstatus.objects.create(systemstatus_name='systemstatus_3')
#        # create url
#        destination = urllib.parse.quote('/api/system/' + str(system_api_1.system_id) + '/', safe='/')
#        # create PUT string
#        putstring = {
#            "note_title": "new_system_api_1",
#            "analysisstatus": analysisstatus_3.analysisstatus_id,
#            "case": [
#                case_1.case_id,
#            ],
#            "company": [
#                company_1.company_id,
#            ],
#            "contact": contact_1.contact_id,
#            "dnsname": dnsname_1.dnsname_id,
#            "domain": domain_1.domain_id,
#            "host_system": host_system_1.system_id,
#            "ip": [
#                ip_1.ip_id,
#            ],
#            "location": location_1.location_id,
#            "os": os_1.os_id,
#            "osarch": osarch_1.osarch_id,
#            "reason": reason_1.reason_id,
#            "recommendation": recommendation_1.recommendation_id,
#            "serviceprovider": serviceprovider_1.serviceprovider_id,
#            "systemstatus": systemstatus_3.systemstatus_id,
#            "systemtype": systemtype_1.systemtype_id,
#            "tag": [
#                tag_1.tag_id,
#            ],
#            "system_lastbooted_time": '2021-05-10T21:35',
#            "system_deprecated_time": '2021-05-10T21:45',
#            "system_is_vm": True,
#            "system_created_by_user_id": test_user_id,
#            "system_modified_by_user_id": test_user_id,
#            "system_export_markdown": False,
#            "system_export_spreadsheet": False,
#        }
#        # get response
#        response = self.client.put(destination, data=putstring, content_type='application/json')
#        # compare
#        self.assertEqual(response.status_code, 200)
#        # get object
#        new_system_api_1 = System.objects.get(note_title='new_system_api_1')
#        # compare
#        self.assertEqual(new_system_api_1.analysisstatus, analysisstatus_3)
#        self.assertEqual(new_system_api_1.contact, contact_1)
#        self.assertEqual(new_system_api_1.dnsname, dnsname_1)
#        self.assertEqual(new_system_api_1.domain, domain_1)
#        self.assertEqual(new_system_api_1.host_system, host_system_1)
#        self.assertEqual(new_system_api_1.location, location_1)
#        self.assertEqual(new_system_api_1.os, os_1)
#        self.assertEqual(new_system_api_1.osarch, osarch_1)
#        self.assertEqual(new_system_api_1.reason, reason_1)
#        self.assertEqual(new_system_api_1.recommendation, recommendation_1)
#        self.assertEqual(new_system_api_1.serviceprovider, serviceprovider_1)
#        self.assertEqual(new_system_api_1.systemstatus, systemstatus_3)
#        self.assertEqual(new_system_api_1.systemtype, systemtype_1)
#        self.assertTrue(new_system_api_1.case.filter(case_name='case_1').exists())
#        self.assertTrue(new_system_api_1.company.filter(company_name='company_1').exists())
#        self.assertTrue(new_system_api_1.ip.filter(ip_ip='127.0.0.1').exists())
#        self.assertTrue(new_system_api_1.tag.filter(tag_name='tag_1').exists())
#        self.assertEqual(new_system_api_1.system_lastbooted_time, datetime(2021, 5, 10, 21, 35, tzinfo=timezone.utc))
#        self.assertEqual(new_system_api_1.system_deprecated_time, datetime(2021, 5, 10, 21, 45, tzinfo=timezone.utc))
#        self.assertTrue(new_system_api_1.system_is_vm)
#        self.assertFalse(new_system_api_1.system_export_markdown)
#        self.assertFalse(new_system_api_1.system_export_spreadsheet)

    def test_note_detail_api_redirect(self):
        """ test redirect with appending slash """

        # get object
        note_api_1 = Note.objects.get(note_title='note_api_1')
        # login testuser
        self.client.login(username='testuser_note_api', password='2to8VdHRHNUcNS7CXmDd')
        # create url
        destination = urllib.parse.quote('/api/note/' + str(note_api_1.note_id) + '/', safe='/')
        # get response
        response = self.client.get('/api/note/' + str(note_api_1.note_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)
