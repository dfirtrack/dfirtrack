import urllib.parse
from datetime import datetime
from datetime import timezone as dttimezone

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from dfirtrack_main.models import (
    Analysisstatus,
    Case,
    Company,
    Contact,
    Dnsname,
    Domain,
    Ip,
    Location,
    Os,
    Osarch,
    Reason,
    Recommendation,
    Serviceprovider,
    System,
    Systemstatus,
    Systemtype,
    Tag,
    Tagcolor,
)


class SystemAPIViewTestCase(TestCase):
    """system API view tests"""

    @classmethod
    def setUpTestData(cls):
        # create user
        test_user = User.objects.create_user(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )

        # create object
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Company.objects.create(company_name='company_1')
        Contact.objects.create(
            contact_name='contact_1',
            contact_email='contact_email_1',
        )
        Dnsname.objects.create(dnsname_name='dnsname_1')
        Domain.objects.create(domain_name='domain_1')
        Ip.objects.create(ip_ip='127.0.0.1')
        Location.objects.create(location_name='location_1')
        Os.objects.create(os_name='os_1')
        Osarch.objects.create(osarch_name='osarch_1')
        Reason.objects.create(reason_name='reason_1')
        Recommendation.objects.create(recommendation_name='recommendation_1')
        Serviceprovider.objects.create(serviceprovider_name='serviceprovider_1')
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        Systemtype.objects.create(systemtype_name='systemtype_1')

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

        """ system """

        # create object - main testing system
        System.objects.create(
            system_name='system_api_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # create object - host system
        System.objects.create(
            system_name='host_system_api_1',
            systemstatus=systemstatus_1,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

    def test_system_list_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get response
        response = self.client.get('/api/system/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_system_list_api_method_get(self):
        """GET is allowed"""

        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # get response
        response = self.client.get('/api/system/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_list_api_method_post(self):
        """POST is allowed"""

        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_system_api').id
        # get object
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        # create POST string
        poststring = {
            "system_name": "system_api_2",
            "systemstatus": systemstatus_1.systemstatus_id,
            "system_created_by_user_id": test_user_id,
            "system_modified_by_user_id": test_user_id,
        }
        # check for existence of object
        system_api_2_none = System.objects.filter(system_name='system_api_2')
        # compare
        self.assertEqual(len(system_api_2_none), 0)
        # get response
        response = self.client.post(
            '/api/system/', data=poststring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        system_api_2 = System.objects.get(system_name='system_api_2')
        # compare
        self.assertEqual(system_api_2.systemstatus, systemstatus_1)

    def test_system_list_api_method_post_all_id(self):
        """POST is allowed"""

        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_system_api').id
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_1'
        )
        case_1 = Case.objects.get(case_name='case_1')
        company_1 = Company.objects.get(company_name='company_1')
        contact_1 = Contact.objects.get(contact_name='contact_1')
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        domain_1 = Domain.objects.get(domain_name='domain_1')
        host_system_1 = System.objects.get(system_name='host_system_api_1')
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        location_1 = Location.objects.get(location_name='location_1')
        os_1 = Os.objects.get(os_name='os_1')
        osarch_1 = Osarch.objects.get(osarch_name='osarch_1')
        reason_1 = Reason.objects.get(reason_name='reason_1')
        recommendation_1 = Recommendation.objects.get(
            recommendation_name='recommendation_1'
        )
        serviceprovider_1 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_1'
        )
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create POST string
        poststring = {
            "system_name": "system_api_3",
            "analysisstatus": analysisstatus_1.analysisstatus_id,
            "case": [
                case_1.case_id,
            ],
            "company": [
                company_1.company_id,
            ],
            "contact": contact_1.contact_id,
            "dnsname": dnsname_1.dnsname_id,
            "domain": domain_1.domain_id,
            "host_system": host_system_1.system_id,
            "ip": [
                ip_1.ip_id,
            ],
            "location": location_1.location_id,
            "os": os_1.os_id,
            "osarch": osarch_1.osarch_id,
            "reason": reason_1.reason_id,
            "recommendation": recommendation_1.recommendation_id,
            "serviceprovider": serviceprovider_1.serviceprovider_id,
            "systemstatus": systemstatus_1.systemstatus_id,
            "systemtype": systemtype_1.systemtype_id,
            "tag": [
                tag_1.tag_id,
            ],
            "system_lastbooted_time": '2021-05-10T21:15',
            "system_deprecated_time": '2021-05-10T21:25',
            "system_is_vm": True,
            "system_created_by_user_id": test_user_id,
            "system_modified_by_user_id": test_user_id,
            "system_assigned_to_user_id": test_user_id,
            "system_export_markdown": False,
            "system_export_spreadsheet": False,
        }
        # check for existence of object
        system_api_3_none = System.objects.filter(system_name='system_api_3')
        # compare
        self.assertEqual(len(system_api_3_none), 0)
        # get response
        response = self.client.post(
            '/api/system/', data=poststring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 201)
        # get object
        system_api_3 = System.objects.get(system_name='system_api_3')
        # compare
        self.assertEqual(system_api_3.analysisstatus, analysisstatus_1)
        self.assertEqual(system_api_3.contact, contact_1)
        self.assertEqual(system_api_3.dnsname, dnsname_1)
        self.assertEqual(system_api_3.domain, domain_1)
        self.assertEqual(system_api_3.host_system, host_system_1)
        self.assertEqual(system_api_3.location, location_1)
        self.assertEqual(system_api_3.os, os_1)
        self.assertEqual(system_api_3.osarch, osarch_1)
        self.assertEqual(system_api_3.reason, reason_1)
        self.assertEqual(system_api_3.recommendation, recommendation_1)
        self.assertEqual(system_api_3.serviceprovider, serviceprovider_1)
        self.assertEqual(system_api_3.systemstatus, systemstatus_1)
        self.assertEqual(system_api_3.systemtype, systemtype_1)
        self.assertTrue(system_api_3.case.filter(case_name='case_1').exists())
        self.assertTrue(system_api_3.company.filter(company_name='company_1').exists())
        self.assertTrue(system_api_3.ip.filter(ip_ip='127.0.0.1').exists())
        self.assertTrue(system_api_3.tag.filter(tag_name='tag_1').exists())
        self.assertEqual(
            system_api_3.system_lastbooted_time,
            datetime(2021, 5, 10, 21, 15, tzinfo=dttimezone.utc),
        )
        self.assertEqual(
            system_api_3.system_deprecated_time,
            datetime(2021, 5, 10, 21, 25, tzinfo=dttimezone.utc),
        )
        self.assertTrue(system_api_3.system_is_vm)
        self.assertFalse(system_api_3.system_export_markdown)
        self.assertFalse(system_api_3.system_export_spreadsheet)

    # TODO: is it possible to declare (and therefore test) nested serializers this way (like with analysisstatus in this example)?
    #    def test_system_list_api_method_post_all_fk(self):
    #        """ POST is allowed """
    #
    #        # get user
    #        test_user_id = User.objects.get(username='testuser_system_api').id
    #        # get object
    #        analysisstatus_name = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1').analysisstatus_name
    #        # get object
    #        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
    #        # login testuser
    #        self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
    #        # create POST string
    #        poststring = {
    #            "system_name": "system_api_2",
    #            "analysisstatus": {
    #                "analysisstatus_name": analysisstatus_name,
    #            },
    #            "systemstatus": systemstatus_id,
    #            "system_created_by_user_id": test_user_id,
    #            "system_modified_by_user_id": test_user_id,
    #        }
    #        # get response
    #        response = self.client.post('/api/system/', data=poststring, content_type='application/json')
    #        # compare
    #        self.assertEqual(response.status_code, 201)

    def test_system_list_api_redirect(self):
        """test redirect with appending slash"""

        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # create url
        destination = urllib.parse.quote('/api/system/', safe='/')
        # get response
        response = self.client.get('/api/system', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_detail_api_unauthorized(self):
        """unauthorized access is forbidden"""

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # get response
        response = self.client.get('/api/system/' + str(system_api_1.system_id) + '/')
        # compare
        self.assertEqual(response.status_code, 401)

    def test_system_detail_api_method_get(self):
        """GET is allowed"""

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # get response
        response = self.client.get('/api/system/' + str(system_api_1.system_id) + '/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_detail_api_method_delete(self):
        """DELETE is forbidden"""

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # get response
        response = self.client.delete(
            '/api/system/' + str(system_api_1.system_id) + '/'
        )
        # compare
        self.assertEqual(response.status_code, 405)

    def test_system_detail_api_method_put(self):
        """PUT is allowed"""

        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_system_api').id
        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # create objects
        analysisstatus_2 = Analysisstatus.objects.create(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.create(systemstatus_name='systemstatus_2')
        # create url
        destination = urllib.parse.quote(
            '/api/system/' + str(system_api_1.system_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "system_name": "new_system_api_1",
            "analysisstatus": analysisstatus_2.analysisstatus_id,
            "systemstatus": systemstatus_2.systemstatus_id,
            "system_created_by_user_id": test_user_id,
            "system_modified_by_user_id": test_user_id,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        new_system_api_1 = System.objects.get(system_name='new_system_api_1')
        # compare
        self.assertEqual(new_system_api_1.analysisstatus, analysisstatus_2)
        self.assertEqual(new_system_api_1.systemstatus, systemstatus_2)

    def test_system_detail_api_method_put_all_id(self):
        """PUT is allowed"""

        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # get user
        test_user_id = User.objects.get(username='testuser_system_api').id
        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        company_1 = Company.objects.get(company_name='company_1')
        contact_1 = Contact.objects.get(contact_name='contact_1')
        dnsname_1 = Dnsname.objects.get(dnsname_name='dnsname_1')
        domain_1 = Domain.objects.get(domain_name='domain_1')
        host_system_1 = System.objects.get(system_name='host_system_api_1')
        ip_1 = Ip.objects.get(ip_ip='127.0.0.1')
        location_1 = Location.objects.get(location_name='location_1')
        os_1 = Os.objects.get(os_name='os_1')
        osarch_1 = Osarch.objects.get(osarch_name='osarch_1')
        reason_1 = Reason.objects.get(reason_name='reason_1')
        recommendation_1 = Recommendation.objects.get(
            recommendation_name='recommendation_1'
        )
        serviceprovider_1 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_1'
        )
        systemtype_1 = Systemtype.objects.get(systemtype_name='systemtype_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        # create objects
        analysisstatus_3 = Analysisstatus.objects.create(
            analysisstatus_name='analysisstatus_3'
        )
        systemstatus_3 = Systemstatus.objects.create(systemstatus_name='systemstatus_3')
        # create url
        destination = urllib.parse.quote(
            '/api/system/' + str(system_api_1.system_id) + '/', safe='/'
        )
        # create PUT string
        putstring = {
            "system_name": "new_system_api_1",
            "analysisstatus": analysisstatus_3.analysisstatus_id,
            "case": [
                case_1.case_id,
            ],
            "company": [
                company_1.company_id,
            ],
            "contact": contact_1.contact_id,
            "dnsname": dnsname_1.dnsname_id,
            "domain": domain_1.domain_id,
            "host_system": host_system_1.system_id,
            "ip": [
                ip_1.ip_id,
            ],
            "location": location_1.location_id,
            "os": os_1.os_id,
            "osarch": osarch_1.osarch_id,
            "reason": reason_1.reason_id,
            "recommendation": recommendation_1.recommendation_id,
            "serviceprovider": serviceprovider_1.serviceprovider_id,
            "systemstatus": systemstatus_3.systemstatus_id,
            "systemtype": systemtype_1.systemtype_id,
            "tag": [
                tag_1.tag_id,
            ],
            "system_lastbooted_time": '2021-05-10T21:35',
            "system_deprecated_time": '2021-05-10T21:45',
            "system_is_vm": True,
            "system_created_by_user_id": test_user_id,
            "system_modified_by_user_id": test_user_id,
            "system_assigned_to_user_id": test_user_id,
            "system_export_markdown": False,
            "system_export_spreadsheet": False,
        }
        # get response
        response = self.client.put(
            destination, data=putstring, content_type='application/json'
        )
        # compare
        self.assertEqual(response.status_code, 200)
        # get object
        new_system_api_1 = System.objects.get(system_name='new_system_api_1')
        # compare
        self.assertEqual(new_system_api_1.analysisstatus, analysisstatus_3)
        self.assertEqual(new_system_api_1.contact, contact_1)
        self.assertEqual(new_system_api_1.dnsname, dnsname_1)
        self.assertEqual(new_system_api_1.domain, domain_1)
        self.assertEqual(new_system_api_1.host_system, host_system_1)
        self.assertEqual(new_system_api_1.location, location_1)
        self.assertEqual(new_system_api_1.os, os_1)
        self.assertEqual(new_system_api_1.osarch, osarch_1)
        self.assertEqual(new_system_api_1.reason, reason_1)
        self.assertEqual(new_system_api_1.recommendation, recommendation_1)
        self.assertEqual(new_system_api_1.serviceprovider, serviceprovider_1)
        self.assertEqual(new_system_api_1.systemstatus, systemstatus_3)
        self.assertEqual(new_system_api_1.systemtype, systemtype_1)
        self.assertTrue(new_system_api_1.case.filter(case_name='case_1').exists())
        self.assertTrue(
            new_system_api_1.company.filter(company_name='company_1').exists()
        )
        self.assertTrue(new_system_api_1.ip.filter(ip_ip='127.0.0.1').exists())
        self.assertTrue(new_system_api_1.tag.filter(tag_name='tag_1').exists())
        self.assertEqual(
            new_system_api_1.system_lastbooted_time,
            datetime(2021, 5, 10, 21, 35, tzinfo=dttimezone.utc),
        )
        self.assertEqual(
            new_system_api_1.system_deprecated_time,
            datetime(2021, 5, 10, 21, 45, tzinfo=dttimezone.utc),
        )
        self.assertTrue(new_system_api_1.system_is_vm)
        self.assertFalse(new_system_api_1.system_export_markdown)
        self.assertFalse(new_system_api_1.system_export_spreadsheet)

    # TODO: is it possible to declare (and therefore test) nested serializers this way (like with analysisstatus in this example)?
    #    def test_system_detail_api_method_put_all_fk(self):
    #        """ PUT is allowed """
    #
    #        # get user
    #        test_user_id = User.objects.get(username='testuser_system_api').id
    #        # get object
    #        system_api_1 = System.objects.get(system_name='system_api_1')
    #        # get object
    #        analysisstatus_name = Analysisstatus.objects.get(analysisstatus_name='analysisstatus_1').analysisstatus_name
    #        # get object
    #        systemstatus_id = Systemstatus.objects.get(systemstatus_name='systemstatus_1').systemstatus_id
    #        # login testuser
    #        self.client.login(username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc')
    #        # create url
    #        destination = urllib.parse.quote('/api/system/' + str(system_api_1.system_id) + '/', safe='/')
    #        # create PUT string
    #        putstring = {
    #            "system_name": "new_system_api_1",
    #            "analysisstatus": {
    #                "analysisstatus_name": analysisstatus_name,
    #            },
    #            "systemstatus": systemstatus_id,
    #            "system_created_by_user_id": test_user_id,
    #            "system_modified_by_user_id": test_user_id,
    #        }
    #        # get response
    #        response = self.client.put(destination, data=putstring, content_type='application/json')
    #        # compare
    #        self.assertEqual(response.status_code, 200)

    def test_system_detail_api_redirect(self):
        """test redirect with appending slash"""

        # get object
        system_api_1 = System.objects.get(system_name='system_api_1')
        # login testuser
        self.client.login(
            username='testuser_system_api', password='Pqtg7fic7FfB2ESEwaPc'
        )
        # create url
        destination = urllib.parse.quote(
            '/api/system/' + str(system_api_1.system_id) + '/', safe='/'
        )
        # get response
        response = self.client.get(
            '/api/system/' + str(system_api_1.system_id), follow=True
        )
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )
