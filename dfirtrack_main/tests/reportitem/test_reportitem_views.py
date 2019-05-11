from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from dfirtrack_main.models import Headline, Reportitem, System, Systemstatus
from dfirtrack_main.views import reportitems_views
import urllib.parse

class ReportitemViewTestCase(TestCase):
    """ reportitem view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        test_user.save()

        # create object
        systemstatus_1 = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # create object
        system_1 = System.objects.create(
            system_name='system_1',
            systemstatus = systemstatus_1,
            system_modify_time = timezone.now(),
            system_created_by_user_id = test_user,
            system_modified_by_user_id = test_user,
        )

        # create object
        headline_1 = Headline.objects.create(headline_name='headline_1')

        # create object
        Reportitem.objects.create(
            reportitem_note='lorem ipsum',
            system = system_1,
            headline = headline_1,
            reportitem_created_by_user_id = test_user,
            reportitem_modified_by_user_id = test_user,
        )

    def test_reportitems_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitems/', safe='')
        # get response
        response = self.client.get('/reportitems/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitems_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitems_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitems_list.html')

    def test_reportitems_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitems_detail_not_logged_in(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitems/' + str(reportitem_1.reportitem_id), safe='')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitems_detail_logged_in(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitems_detail_template(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitems_detail.html')

    def test_reportitems_detail_get_user_context(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitems_add_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitems/add/', safe='')
        # get response
        response = self.client.get('/reportitems/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitems_add_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitems_add_template(self):

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitems_add.html')

    def test_reportitems_add_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

    def test_reportitems_edit_not_logged_in(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/reportitems/' + str(reportitem_1.reportitem_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_reportitems_edit_logged_in(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_reportitems_edit_template(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/reportitem/reportitems_edit.html')

    def test_reportitems_edit_get_user_context(self):

        # get object
        reportitem_1 = Reportitem.objects.get(reportitem_note='lorem ipsum')
        # login testuser
        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
        # get response
        response = self.client.get('/reportitems/' + str(reportitem_1.reportitem_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_reportitem')

#    def test_reportitems_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_reportitem', password='R2vXUSF3SIB8hhKmnztS')
#        # get response
#        response = self.client.get('/reportitems/x')
#        # compare
#        self.assertEqual(response.status_code, 404)
