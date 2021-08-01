import urllib.parse

from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from dfirtrack_config.models import Workflow
from dfirtrack_main.models import (
    Analysisstatus,
    Company,
    Contact,
    Location,
    Serviceprovider,
    System,
    Systemstatus,
    Tag,
    Tagcolor,
)


def create_system(system_name):
    """helper function"""

    # get user
    test_user = User.objects.get(username='testuser_system_modificator')

    # get objects
    analysisstatus_1 = Analysisstatus.objects.get(
        analysisstatus_name='analysisstatus_1'
    )
    systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')

    company_1 = Company.objects.get(company_name='company_1')
    contact_1 = Contact.objects.get(contact_name='contact_1')
    location_1 = Location.objects.get(location_name='location_1')
    serviceprovider_1 = Serviceprovider.objects.get(
        serviceprovider_name='serviceprovider_1'
    )
    tag_1 = Tag.objects.get(tag_name='tag_1')

    # create system
    system = System.objects.create(
        system_name=system_name,
        analysisstatus=analysisstatus_1,
        systemstatus=systemstatus_1,
        contact=contact_1,
        location=location_1,
        serviceprovider=serviceprovider_1,
        system_created_by_user_id=test_user,
        system_modified_by_user_id=test_user,
    )

    # add many2many
    system.company.add(company_1)
    system.tag.add(tag_1)

    # return to setup function
    return


class SystemModificatorViewTestCase(TestCase):
    """system modificator view tests"""

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )

        # create objects
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_1')
        Analysisstatus.objects.create(analysisstatus_name='analysisstatus_2')
        Company.objects.create(company_name='company_1')
        Company.objects.create(company_name='company_2')
        Company.objects.create(company_name='company_3')
        Contact.objects.create(
            contact_name='contact_1', contact_email='con1@example.com'
        )
        Contact.objects.create(
            contact_name='contact_2', contact_email='con2@example.com'
        )
        Location.objects.create(location_name='location_1')
        Location.objects.create(location_name='location_2')
        Serviceprovider.objects.create(serviceprovider_name='serviceprovider_1')
        Serviceprovider.objects.create(serviceprovider_name='serviceprovider_2')
        Systemstatus.objects.create(systemstatus_name='systemstatus_1')
        Systemstatus.objects.create(systemstatus_name='systemstatus_2')
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        Tag.objects.create(
            tag_name='tag_1',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_2',
            tagcolor=tagcolor_1,
        )
        Tag.objects.create(
            tag_name='tag_3',
            tagcolor=tagcolor_1,
        )
        # create systems
        create_system('system_modificator_system_1')
        create_system('system_modificator_system_2')
        create_system('system_modificator_system_3')
        create_system('system_modificator_redirect')
        create_system('system_modificator_char_field_1')
        create_system('system_modificator_char_field_2')
        create_system('system_modificator_messages_1')
        create_system('system_modificator_messages_2')
        create_system('system_modificator_double')
        create_system('system_modificator_double')

        # create objscts
        Workflow.objects.create(
            workflow_name='workflow_1',
            workflow_created_by_user_id=test_user,
            workflow_modified_by_user_id=test_user,
        )

    def test_system_modificator_not_logged_in(self):
        """test modificator view"""

        # create url
        destination = '/login/?next=' + urllib.parse.quote(
            '/system/modificator/', safe=''
        )
        # get response
        response = self.client.get('/system/modificator/', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_modificator_logged_in(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get response
        response = self.client.get('/system/modificator/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_system_modificator_template(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get response
        response = self.client.get('/system/modificator/')
        # compare
        self.assertTemplateUsed(
            response, 'dfirtrack_main/system/system_modificator.html'
        )

    def test_system_modificator_get_user_context(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get response
        response = self.client.get('/system/modificator/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_modificator')

    def test_system_modificator_context_workflows(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get response
        response = self.client.get('/system/modificator/')
        # compare
        self.assertEquals(str(response.context['workflows'][0]), 'workflow_1')

    def test_system_modificator_redirect(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # create url
        destination = urllib.parse.quote('/system/modificator/', safe='/')
        # get response
        response = self.client.get('/system/modificator', follow=True)
        # compare
        self.assertRedirects(
            response, destination, status_code=301, target_status_code=200
        )

    def test_system_modificator_post_redirect(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_redirect',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
        }
        # create url
        destination = '/system/'
        # get response
        response = self.client.post('/system/modificator/', data_dict)
        # compare
        self.assertRedirects(
            response, destination, status_code=302, target_status_code=200
        )

    def test_system_modificator_post_systems_status(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_1'
        )
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_1 = Systemstatus.objects.get(systemstatus_name='systemstatus_1')
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1\nsystem_modificator_system_2',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company_delete': 'keep_not_add',
            'tag_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
        }
        # get response
        self.client.post('/system/modificator/', data_dict)
        # compare
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_1'
            ).analysisstatus,
            analysisstatus_2,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_2'
            ).analysisstatus,
            analysisstatus_2,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_3'
            ).analysisstatus,
            analysisstatus_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').systemstatus,
            systemstatus_2,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').systemstatus,
            systemstatus_2,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').systemstatus,
            systemstatus_1,
        )

    def test_system_modificator_post_systems_keep_all_no_attributes_provided(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        contact_1 = Contact.objects.get(contact_name='contact_1')
        location_1 = Location.objects.get(location_name='location_1')
        serviceprovider_1 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_1'
        )
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1\nsystem_modificator_system_2',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
            'tag_delete': 'keep_not_add',
        }
        # get response
        self.client.post('/system/modificator/', data_dict)
        # compare - company (m2m)
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_3')
            .exists()
        )
        # compare - contact (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').contact,
            contact_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').contact,
            contact_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').contact,
            contact_1,
        )
        # compare - location (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').location,
            location_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').location,
            location_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').location,
            location_1,
        )
        # compare - serviceprovider (fk)
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_1'
            ).serviceprovider,
            serviceprovider_1,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_2'
            ).serviceprovider,
            serviceprovider_1,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_3'
            ).serviceprovider,
            serviceprovider_1,
        )
        # compare - tag (m2m)
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_3')
            .exists()
        )

    def test_system_modificator_post_systems_keep_all_attributes_provided(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        company_2 = Company.objects.get(company_name='company_2')
        company_3 = Company.objects.get(company_name='company_3')
        contact_1 = Contact.objects.get(contact_name='contact_1')
        contact_2 = Contact.objects.get(contact_name='contact_2')
        location_1 = Location.objects.get(location_name='location_1')
        location_2 = Location.objects.get(location_name='location_2')
        serviceprovider_1 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_1'
        )
        serviceprovider_2 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_2'
        )
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1\nsystem_modificator_system_2',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company': [str(company_2.company_id), str(company_3.company_id)],
            'contact': contact_2.contact_id,
            'location': location_2.location_id,
            'serviceprovider': serviceprovider_2.serviceprovider_id,
            'tag': [str(tag_2.tag_id), str(tag_3.tag_id)],
            'company_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
            'tag_delete': 'keep_not_add',
        }
        # get response
        self.client.post('/system/modificator/', data_dict)
        # compare - company (m2m)
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_3')
            .exists()
        )
        # compare - contact (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').contact,
            contact_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').contact,
            contact_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').contact,
            contact_1,
        )
        # compare - location (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').location,
            location_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').location,
            location_1,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').location,
            location_1,
        )
        # compare - serviceprovider (fk)
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_1'
            ).serviceprovider,
            serviceprovider_1,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_2'
            ).serviceprovider,
            serviceprovider_1,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_3'
            ).serviceprovider,
            serviceprovider_1,
        )
        # compare - tag (m2m)
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_3')
            .exists()
        )

    def test_system_modificator_post_systems_add_m2m_attributes_provided(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        company_2 = Company.objects.get(company_name='company_2')
        company_3 = Company.objects.get(company_name='company_3')
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1\nsystem_modificator_system_2',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company': [str(company_2.company_id), str(company_3.company_id)],
            'tag': [str(tag_2.tag_id), str(tag_3.tag_id)],
            'company_delete': 'keep_and_add',
            'contact_delete': 'switch_new',
            'location_delete': 'switch_new',
            'serviceprovider_delete': 'switch_new',
            'tag_delete': 'keep_and_add',
        }
        # get response
        self.client.post('/system/modificator/', data_dict)
        # compare - company (m2m)
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_3')
            .exists()
        )
        # compare - tag (m2m)
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_3')
            .exists()
        )

    def test_system_modificator_post_systems_remove_all_no_attributes_provided(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        contact_1 = Contact.objects.get(contact_name='contact_1')
        location_1 = Location.objects.get(location_name='location_1')
        serviceprovider_1 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_1'
        )
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1\nsystem_modificator_system_2',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company_delete': 'remove_and_add',
            'contact_delete': 'switch_new',
            'location_delete': 'switch_new',
            'serviceprovider_delete': 'switch_new',
            'tag_delete': 'remove_and_add',
        }
        # get response
        self.client.post('/system/modificator/', data_dict)
        # compare - company (m2m)
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_3')
            .exists()
        )
        # compare - contact (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').contact, None
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').contact, None
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').contact,
            contact_1,
        )
        # compare - location (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').location, None
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').location, None
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').location,
            location_1,
        )
        # compare - serviceprovider (fk)
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_1'
            ).serviceprovider,
            None,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_2'
            ).serviceprovider,
            None,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_3'
            ).serviceprovider,
            serviceprovider_1,
        )
        # compare - tag (m2m)
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_3')
            .exists()
        )

    def test_system_modificator_post_systems_remove_all_attributes_provided(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        company_2 = Company.objects.get(company_name='company_2')
        company_3 = Company.objects.get(company_name='company_3')
        contact_1 = Contact.objects.get(contact_name='contact_1')
        contact_2 = Contact.objects.get(contact_name='contact_2')
        location_1 = Location.objects.get(location_name='location_1')
        location_2 = Location.objects.get(location_name='location_2')
        serviceprovider_1 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_1'
        )
        serviceprovider_2 = Serviceprovider.objects.get(
            serviceprovider_name='serviceprovider_2'
        )
        tag_2 = Tag.objects.get(tag_name='tag_2')
        tag_3 = Tag.objects.get(tag_name='tag_3')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1\nsystem_modificator_system_2',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company': [str(company_2.company_id), str(company_3.company_id)],
            'contact': contact_2.contact_id,
            'location': location_2.location_id,
            'serviceprovider': serviceprovider_2.serviceprovider_id,
            'tag': [str(tag_2.tag_id), str(tag_3.tag_id)],
            'company_delete': 'remove_and_add',
            'contact_delete': 'switch_new',
            'location_delete': 'switch_new',
            'serviceprovider_delete': 'switch_new',
            'tag_delete': 'remove_and_add',
        }
        # get response
        self.client.post('/system/modificator/', data_dict)
        # compare - company (m2m)
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .company.filter(company_name='company_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .company.filter(company_name='company_3')
            .exists()
        )
        # compare - contact (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').contact,
            contact_2,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').contact,
            contact_2,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').contact,
            contact_1,
        )
        # compare - location (fk)
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_1').location,
            location_2,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_2').location,
            location_2,
        )
        self.assertEqual(
            System.objects.get(system_name='system_modificator_system_3').location,
            location_1,
        )
        # compare - serviceprovider (fk)
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_1'
            ).serviceprovider,
            serviceprovider_2,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_2'
            ).serviceprovider,
            serviceprovider_2,
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_system_3'
            ).serviceprovider,
            serviceprovider_1,
        )
        # compare - tag (m2m)
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_1')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_2')
            .tag.filter(tag_name='tag_3')
            .exists()
        )
        self.assertTrue(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_1')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_2')
            .exists()
        )
        self.assertFalse(
            System.objects.get(system_name='system_modificator_system_3')
            .tag.filter(tag_name='tag_3')
            .exists()
        )

    def test_system_modificator_post_char_field(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        system_modificator_char_field_1 = System.objects.get(
            system_name='system_modificator_char_field_1'
        )
        system_modificator_char_field_2 = System.objects.get(
            system_name='system_modificator_char_field_2'
        )
        # create system list and append system IDs
        systemlist = []
        systemlist.append(str(system_modificator_char_field_1.system_id))
        systemlist.append(str(system_modificator_char_field_2.system_id))
        # create post data
        data_dict = {
            'systemlist': systemlist,
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
            'tag_delete': 'keep_not_add',
        }
        # get response
        self.client.post('/system/modificator/', data_dict)
        # compare
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_char_field_1'
            ).analysisstatus.analysisstatus_name,
            'analysisstatus_2',
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_char_field_2'
            ).analysisstatus.analysisstatus_name,
            'analysisstatus_2',
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_char_field_1'
            ).systemstatus.systemstatus_name,
            'systemstatus_2',
        )
        self.assertEqual(
            System.objects.get(
                system_name='system_modificator_char_field_2'
            ).systemstatus.systemstatus_name,
            'systemstatus_2',
        )

    def test_system_modificator_post_messages(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_messages_1\n\nsystem_modificator_double',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
            'tag_delete': 'keep_not_add',
        }
        # get response
        response = self.client.post('/system/modificator/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[0]), 'System modificator started')
        self.assertEqual(str(messages[1]), '1 system was created / modified.')
        self.assertEqual(
            str(messages[2]), "1 system was skipped. ['system_modificator_double']"
        )
        self.assertEqual(
            str(messages[3]),
            '1 line out of 3 lines was faulty (see log file for details).',
        )

    def test_system_modificator_post_other_messages(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # get objects
        analysisstatus_2 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_2'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_messages_1\n\nsystem_modificator_not_existent\nsystem_modificator_double\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nsystem_modificator_messages_2',
            'analysisstatus': analysisstatus_2.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'company_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
            'tag_delete': 'keep_not_add',
        }
        # get response
        response = self.client.post('/system/modificator/', data_dict)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(messages[1]), '2 systems were created / modified.')
        self.assertEqual(
            str(messages[2]),
            "2 systems were skipped. ['system_modificator_not_existent', 'system_modificator_double']",
        )
        self.assertEqual(
            str(messages[3]),
            '2 lines out of 6 lines were faulty (see log file for details).',
        )

    # TODO
    def test_system_modificator_post_workflow_messages(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # create objects
        analysisstatus_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_1'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1',
            'analysisstatus': analysisstatus_1.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'workflow': workflow_1.workflow_id,
            'company_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
            'tag_delete': 'keep_not_add',
        }
        # get response
        response = self.client.post('/system/modificator/', data_dict, follow=True)
        # compare
        self.assertContains(response, 'System creator/modificator workflows applied.')

    def test_system_modificator_post_nonexistent_workflow_messages(self):
        """test modificator view"""

        # login testuser
        self.client.login(
            username='testuser_system_modificator', password='QDX5Xp9yhnejSIuYaE1G'
        )
        # create objects
        analysisstatus_1 = Analysisstatus.objects.get(
            analysisstatus_name='analysisstatus_1'
        )
        systemstatus_2 = Systemstatus.objects.get(systemstatus_name='systemstatus_2')
        workflow_1 = Workflow.objects.get(workflow_name='workflow_1')
        # create post data
        data_dict = {
            'systemlist': 'system_modificator_system_1',
            'analysisstatus': analysisstatus_1.analysisstatus_id,
            'systemstatus': systemstatus_2.systemstatus_id,
            'workflow': [workflow_1.workflow_id, 99],
            'company_delete': 'keep_not_add',
            'contact_delete': 'keep_existing',
            'location_delete': 'keep_existing',
            'serviceprovider_delete': 'keep_existing',
            'tag_delete': 'keep_not_add',
        }
        # get response
        response = self.client.post('/system/modificator/', data_dict, follow=True)
        # compare
        self.assertContains(response, 'Could not apply all workflows.')
