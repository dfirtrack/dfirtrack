import filecmp
import os
import shutil
import urllib.parse

from dateutil.parser import parse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from dfirtrack.settings import BASE_DIR
from dfirtrack_config.models import SystemExporterMarkdownConfigModel
from dfirtrack_main.exporter.markdown.markdown import system_cron
from dfirtrack_main.models import (
    Dnsname,
    Domain,
    Entry,
    Headline,
    Ip,
    Os,
    Reason,
    Recommendation,
    Reportitem,
    System,
    Systemstatus,
    Systemtype,
    Systemuser,
)


def set_markdown_path(markdown_path):
    """ helper function """

    # change config
    system_exporter_markdown_config_model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')
    system_exporter_markdown_config_model.markdown_path = markdown_path
    system_exporter_markdown_config_model.save()

    return

def set_markdown_sorting_dom():
    """ helper function """

    # change config
    system_exporter_markdown_config_model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')
    system_exporter_markdown_config_model.markdown_sorting = 'dom'
    system_exporter_markdown_config_model.save()

    return

class SystemExporterMarkdownViewTestCase(TestCase):
    """ system exporter markdown view tests """

    @classmethod
    def setUpTestData(cls):
        """ one-time setup """

        # create user
        test_user = User.objects.create_user(
            username='testuser_system_exporter_markdown',
            is_staff = True,
            is_superuser = True,
            password='2anJuuSjzjLmb2pOYuLf',
        )
        User.objects.create_user(username='message_user', password='eYZTI1hin7sW5iMARxcd')

        # set default config
        system_exporter_markdown_config_model = SystemExporterMarkdownConfigModel.objects.get(system_exporter_markdown_config_name = 'SystemExporterMarkdownConfig')
        system_exporter_markdown_config_model.markdown_path = '/tmp/dfirtrack_test'
        system_exporter_markdown_config_model.markdown_sorting = 'sys'
        system_exporter_markdown_config_model.save()

        # create object
        dnsname_1 = Dnsname.objects.create(dnsname_name = 'dnsname_1')

        # create objects
        domain_1 = Domain.objects.create(domain_name = 'domain_1')
        domain_2 = Domain.objects.create(domain_name = 'domain_2')

        # create object
        ip_1 = Ip.objects.create(ip_ip = '127.0.0.1')

        # create object
        os_1 = Os.objects.create(os_name = 'os_1')

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name = 'systemstatus_1')

        # get objects
        systemstatus_compromised = Systemstatus.objects.get(systemstatus_name = '30_compromised')
        systemstatus_unknown = Systemstatus.objects.get(systemstatus_name = '10_unknown')
        systemstatus_analysis_ongoing = Systemstatus.objects.get(systemstatus_name = '20_analysis_ongoing')
        systemstatus_not_analyzed = Systemstatus.objects.get(systemstatus_name = '90_not_analyzed')
        systemstatus_clean = Systemstatus.objects.get(systemstatus_name = '40_clean')

        # update object (used with 'admonition' extension of mkdocs)
        systemstatus_clean.systemstatus_note = 'This system is clean.'
        systemstatus_clean.save()

        # create object
        reason_1 = Reason.objects.create(reason_name = 'reason_1', reason_note = 'reason_1_note')

        # create object
        recommendation_1 = Recommendation.objects.create(recommendation_name = 'recommendation_1', recommendation_note = 'recommendation_1_note')

        # create object
        systemtype_1 = Systemtype.objects.create(systemtype_name = 'systemtype_1')

        # set system_install_time
        system_install_time = parse('2020-01-02 12:34:56-00')

        # create system objects

        # standard system covering all used attributes
        system_1 = System.objects.create(
            system_name = 'system_1',
            systemstatus = systemstatus_compromised,
            dnsname = dnsname_1,
            domain = domain_1,
            os = os_1,
            reason = reason_1,
            recommendation = recommendation_1,
            systemtype = systemtype_1,
            system_install_time = system_install_time,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        system_1.ip.add(ip_1)
        # system with different domain
        System.objects.create(
            system_name = 'system_2',
            systemstatus = systemstatus_unknown,
            domain = domain_2,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        # system without domain
        System.objects.create(
            system_name = 'system_3',
            systemstatus = systemstatus_analysis_ongoing,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        # system that will not be exported
        System.objects.create(
            system_name = 'system_4',
            systemstatus = systemstatus_1,
            system_export_markdown = False,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        # system with same domain (needed during creation of `mkdocs.yml`)
        System.objects.create(
            system_name = 'system_5',
            systemstatus = systemstatus_clean,
            domain = domain_2,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )
        # system covering last special status that is used with 'admonition' extension of mkdocs
        System.objects.create(
            system_name = 'system_6',
            systemstatus = systemstatus_not_analyzed,
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        headline_1 = Headline.objects.create(headline_name='headline_1')

        # create object
        Reportitem.objects.create(
            reportitem_note = 'lorem ipsum',
            system = system_1,
            headline = headline_1,
            reportitem_subheadline = 'subheadline_1',
            reportitem_created_by_user_id = test_user,
            reportitem_modified_by_user_id = test_user,
        )

        # create object
        Systemuser.objects.create(systemuser_name='systemuser_1', system = system_1)

        # create objects
        Entry.objects.create(
            system = system_1,
            entry_type = 'type_1',
            entry_content = 'lorem ipsum',
            entry_time = "2020-02-03T01:23:45+00:00",
            entry_created_by_user_id = test_user,
            entry_modified_by_user_id = test_user,
        )

        Entry.objects.create(
            system = system_1,           
            entry_time = "2020-02-04T01:23:45+00:00",
            entry_created_by_user_id = test_user,
            entry_modified_by_user_id = test_user,
        )

    @classmethod
    def setUp(cls):
        """ setup in advance of every test """

        # set markdown directory for file system
        markdown_path_filesystem = '/tmp/dfirtrack_test'

        # remove existing and re-create empty markdown directory
        if os.path.exists(markdown_path_filesystem):
            # remove existing markdown directory (recursively)
            shutil.rmtree(markdown_path_filesystem)
            # re-create empty markdown directory
            os.makedirs(markdown_path_filesystem)
        # create empty markdown directory
        else:
            # create empty markdown directory
            os.makedirs(markdown_path_filesystem)

    def test_system_exporter_markdown_not_logged_in(self):
        """ test instant markdown export via button to server file system """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/markdown/system/', safe='')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_logged_in(self):
        """ test instant markdown export via button to server file system """

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_redirect(self):
        """ test instant markdown export via button to server file system """

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_exporter_markdown_markdown_path_empty(self):
        """ test instant markdown export via button to server file system """

        # change config
        set_markdown_path('')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'Markdown path contains an empty string. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_markdown_path_not_existent(self):
        """ test instant markdown export via button to server file system """

        # change config
        set_markdown_path('/foobar')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'Markdown path does not exist. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_markdown_path_no_write_permission(self):
        """ test instant markdown export via button to server file system """

        # change config
        set_markdown_path('/root')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'No write permission for markdown path. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_systemsorted(self):
        """ test instant markdown export via button to server file system """

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare - file system
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test//mkdocs.yml'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_1_domain_1_20200102_123456.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_2_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_3.md'))
        self.assertFalse(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_4.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_5_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_6.md'))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_1_domain_1_20200102_123456.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_1.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_2_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_2.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_3.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_3.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_5_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_5.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_6.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_6.md'), shallow = False))
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - messages
        self.assertEqual(str(messages[0]), 'System exporter markdown (sorted by system) started')
        self.assertEqual(messages[0].level_tag, 'success')
        self.assertEqual(str(messages[1]), 'System exporter markdown (sorted by system) finished')
        self.assertEqual(messages[1].level_tag, 'success')

    def test_system_exporter_markdown_domainsorted(self):
        """ test instant markdown export via button to server file system """

        # change config
        set_markdown_sorting_dom()

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        response = self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/'))
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/domain_1/'))
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/domain_2/'))
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/other_domains/'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test//mkdocs.yml'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/domain_1/system_1_domain_1_20200102_123456.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/domain_2/system_2_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/other_domains/system_3.md'))
        self.assertFalse(os.path.isfile('/tmp/dfirtrack_test/docs/systems/other_domains/system_4.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/domain_2/system_5_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/other_domains/system_6.md'))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/domain_1/system_1_domain_1_20200102_123456.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_1.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/domain_2/system_2_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_2.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/other_domains/system_3.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_3.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/domain_2/system_5_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_5.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/other_domains/system_6.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_6.md'), shallow = False))
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare - messages
        self.assertEqual(str(messages[0]), 'System exporter markdown (sorted by domain) started')
        self.assertEqual(messages[0].level_tag, 'success')
        self.assertEqual(str(messages[1]), 'System exporter markdown (sorted by domain) finished')
        self.assertEqual(messages[1].level_tag, 'success')

    def test_system_exporter_markdown_clean_directory(self):
        """ test instant markdown export via button to server file system """

        # create systems subfolder to test removal and re-creation
        os.makedirs('/tmp/dfirtrack_test/docs/systems/')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/'))

    def test_system_exporter_markdown_read_mkdocs_yml(self):
        """ test instant markdown export via button to server file system """

        # cope dummy mkdocs.yml to test file reading
        shutil.copy(f'{os.getcwd()}/dfirtrack_main/tests/system/files/mkdocs.yml', '/tmp/dfirtrack_test/mkdocs.yml')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        self.client.get('/system/exporter/markdown/system/', follow=True)
        # compare
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/'))

    def test_system_exporter_markdown_cron_markdown_path_empty(self):
        """ test markdown export via scheduled task to server file system """

        # change config
        set_markdown_path('')

        # export markdown without GET by directly calling the function
        system_cron()

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_markdown')
        self.assertEqual(messages[0].message, '[Scheduled task markdown exporter] Markdown path contains an empty string. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='eYZTI1hin7sW5iMARxcd')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, '[Scheduled task markdown exporter] Markdown path contains an empty string. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_cron_markdown_path_not_existent(self):
        """ test markdown export via scheduled task to server file system """

        # change config
        set_markdown_path('/foobar')

        # export markdown without GET by directly calling the function
        system_cron()

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_markdown')
        self.assertEqual(messages[0].message, '[Scheduled task markdown exporter] Markdown path does not exist. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='eYZTI1hin7sW5iMARxcd')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, '[Scheduled task markdown exporter] Markdown path does not exist. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_cron_markdown_path_no_write_permission(self):
        """ test markdown export via scheduled task to server file system """

        # change config
        set_markdown_path('/root')

        # export markdown without GET by directly calling the function
        system_cron()

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_system_exporter_markdown')
        self.assertEqual(messages[0].message, '[Scheduled task markdown exporter] No write permission for markdown path. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')
        # switch user context
        self.client.logout()
        self.client.login(username='message_user', password='eYZTI1hin7sW5iMARxcd')
        # get response
        response = self.client.get('/system/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(str(response.context['user']), 'message_user')
        self.assertEqual(messages[0].message, '[Scheduled task markdown exporter] No write permission for markdown path. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_cron_systemsorted(self):
        """ test markdown export via scheduled task to server file system """

        # export markdown without GET by directly calling the function
        system_cron()

        # compare - file system
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test//mkdocs.yml'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_1_domain_1_20200102_123456.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_2_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_3.md'))
        self.assertFalse(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_4.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_5_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/system_6.md'))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_1_domain_1_20200102_123456.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_1.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_2_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_2.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_3.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_3.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_5_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_5.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/system_6.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_6.md'), shallow = False))

    def test_system_exporter_markdown_cron_domainsorted(self):
        """ test markdown export via scheduled task to server file system """

        # change config
        set_markdown_sorting_dom()

        # export markdown without GET by directly calling the function
        system_cron()

        # compare
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/'))
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/domain_1/'))
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/domain_2/'))
        self.assertTrue(os.path.exists('/tmp/dfirtrack_test/docs/systems/other_domains/'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test//mkdocs.yml'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/domain_1/system_1_domain_1_20200102_123456.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/domain_2/system_2_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/other_domains/system_3.md'))
        self.assertFalse(os.path.isfile('/tmp/dfirtrack_test/docs/systems/other_domains/system_4.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/domain_2/system_5_domain_2.md'))
        self.assertTrue(os.path.isfile('/tmp/dfirtrack_test/docs/systems/other_domains/system_6.md'))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/domain_1/system_1_domain_1_20200102_123456.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_1.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/domain_2/system_2_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_2.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/other_domains/system_3.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_3.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/domain_2/system_5_domain_2.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_5.md'), shallow = False))
        self.assertTrue(filecmp.cmp('/tmp/dfirtrack_test/docs/systems/other_domains/system_6.md', os.path.join(BASE_DIR, 'dfirtrack_main/tests/system/files/system_exporter_markdown_testfile_system_6.md'), shallow = False))

    def test_system_exporter_markdown_create_cron_not_logged_in(self):
        """ test helper function to check config before creating scheduled task """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/system/exporter/markdown/system/cron/', safe='')
        # get response
        response = self.client.get('/system/exporter/markdown/system/cron/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_create_cron_logged_in(self):
        """ test helper function to check config before creating scheduled task """

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/admin/django_q/schedule/add/?name=system_markdown_exporter&func=dfirtrack_main.exporter.markdown.markdown.system_cron', safe='/?=&')
        # get response
        response = self.client.get('/system/exporter/markdown/system/cron/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_system_exporter_markdown_create_cron_redirect(self):
        """ test helper function to check config before creating scheduled task """

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/admin/django_q/schedule/add/?name=system_markdown_exporter&func=dfirtrack_main.exporter.markdown.markdown.system_cron', safe='/?=&')
        # get response
        response = self.client.get('/system/exporter/markdown/system/cron', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=301, target_status_code=200)

    def test_system_exporter_markdown_create_cron_markdown_path_empty(self):
        """ test helper function to check config before creating scheduled task """

        # change config
        set_markdown_path('')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/cron/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'Markdown path contains an empty string. Check config!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_create_cron_markdown_path_not_existent(self):
        """ test helper function to check config before creating scheduled task """

        # change config
        set_markdown_path('/foobar')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/cron/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'Markdown path does not exist. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')

    def test_system_exporter_markdown_create_cron_markdown_path_no_write_permission(self):
        """ test helper function to check config before creating scheduled task """

        # change config
        set_markdown_path('/root')

        # login testuser
        self.client.login(username='testuser_system_exporter_markdown', password='2anJuuSjzjLmb2pOYuLf')
        # create url
        destination = urllib.parse.quote('/system/', safe='/')
        # get response
        response = self.client.get('/system/exporter/markdown/system/cron/', follow=True)
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)
        self.assertEqual(str(messages[0]), 'No write permission for markdown path. Check config or file system!')
        self.assertEqual(messages[0].level_tag, 'error')
