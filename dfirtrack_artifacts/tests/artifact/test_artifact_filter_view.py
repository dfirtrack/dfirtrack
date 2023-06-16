from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from dfirtrack_artifacts.models import Artifact, Artifactstatus, Artifacttype
from dfirtrack_config.models import MainConfigModel, UserConfigModel
from dfirtrack_main.models import Case, System, Systemstatus, Tag, Tagcolor


def set_user_config(test_user, filter_list_case, filter_list_tag):
    """ " set user config"""

    # get config
    user_config = UserConfigModel.objects.get(
        user_config_username=test_user, filter_view='artifact_list'
    )
    # set values
    user_config.filter_list_case = filter_list_case
    if filter_list_tag:
        user_config.filter_list_tag.set(
            [
                filter_list_tag,
            ]
        )
    else:
        user_config.filter_list_tag.clear()
    # save config
    user_config.save()

    # return to test
    return


class ArtifactFilterViewTestCase(TestCase):
    """artifact filter view tests"""

    @classmethod
    def setUpTestData(cls):
        """one time setup"""

        # create user
        test_user = User.objects.create_user(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )

        # create config
        UserConfigModel.objects.create(
            user_config_username=test_user, filter_view='artifact_list'
        )

        # case
        case = Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

        # tagcolor
        tagcolor_1 = Tagcolor.objects.create(tagcolor_name='tagcolor_1')
        # tag
        tag = Tag.objects.create(tag_name='tag_1', tagcolor=tagcolor_1)

        # systemstatus
        systemstatus = Systemstatus.objects.create(systemstatus_name='systemstatus_1')

        # system
        system = System.objects.create(
            system_name='system_plain',
            systemstatus=systemstatus,
            system_created_by_user_id=test_user,
            system_modified_by_user_id=test_user,
        )

        # artifacttype
        artifacttype = Artifacttype.objects.create(artifacttype_name='Artifacttype')

        # no case / no tag
        Artifact.objects.create(
            artifact_name="artifact_plain",
            artifacttype=artifacttype,
            system=system,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )

        # 1 case / no tag
        Artifact.objects.create(
            artifact_name="artifact_case",
            artifacttype=artifacttype,
            case=case,
            system=system,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )

        # no case / 1 tag
        artifact = Artifact.objects.create(
            artifact_name="artifact_tag",
            artifacttype=artifacttype,
            system=system,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )
        artifact.tag.add(tag)

        # 1 case / 1 tag
        artifact = Artifact.objects.create(
            artifact_name="artifact_both",
            artifacttype=artifacttype,
            case=case,
            system=system,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
        )
        artifact.tag.add(tag)

        # closed artifact
        main_config_model = MainConfigModel.objects.get(main_config_name='MainConfig')
        artifacstatus_open = Artifactstatus.objects.all().first()
        main_config_model.artifactstatus_open.add(artifacstatus_open)
        artifactstatus_closed = Artifactstatus.objects.all().last()

        Artifact.objects.create(
            artifact_name="artifact_closed",
            artifacttype=artifacttype,
            system=system,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
            artifactstatus=artifactstatus_closed,
        )

        Artifact.objects.create(
            artifact_name="artifact_open",
            artifacttype=artifacttype,
            system=system,
            artifact_created_by_user_id=test_user,
            artifact_modified_by_user_id=test_user,
            artifactstatus=artifacstatus_open,
        )

    def test_artifact_list_no_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')
        # get objects
        plain = Artifact.objects.get(artifact_name='artifact_plain')
        case = Artifact.objects.get(artifact_name='artifact_case')
        tag = Artifact.objects.get(artifact_name='artifact_tag')
        both = Artifact.objects.get(artifact_name='artifact_both')

        # change config
        set_user_config(test_user, None, None)

        # get response with default JSON request
        response = self.client.post(
            '/filter/artifact/?artifact&status=all',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'artifact_name',
                'draw': '1',
            },
        )
        # compare
        self.assertContains(response, plain.artifact_name)
        self.assertContains(response, case.artifact_name)
        self.assertContains(response, tag.artifact_name)
        self.assertContains(response, both.artifact_name)

    def test_artifact_list_case_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')
        # get objects
        plain = Artifact.objects.get(artifact_name='artifact_plain')
        case = Artifact.objects.get(artifact_name='artifact_case')
        tag = Artifact.objects.get(artifact_name='artifact_tag')
        both = Artifact.objects.get(artifact_name='artifact_both')

        # change config
        set_user_config(test_user, None, None)

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        set_user_config(test_user, case_1, None)

        # get response with default JSON request
        response = self.client.post(
            '/filter/artifact/?artifact&status=all',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'artifact_name',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, plain.artifact_name)
        self.assertContains(response, case.artifact_name)
        self.assertNotContains(response, tag.artifact_name)
        self.assertContains(response, both.artifact_name)

    def test_artifact_list_tag_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')
        # get objects
        plain = Artifact.objects.get(artifact_name='artifact_plain')
        case = Artifact.objects.get(artifact_name='artifact_case')
        tag = Artifact.objects.get(artifact_name='artifact_tag')
        both = Artifact.objects.get(artifact_name='artifact_both')

        # change config
        set_user_config(test_user, None, None)

        # change config
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, None, tag_1)

        # get response with default JSON request
        response = self.client.post(
            '/filter/artifact/?artifact&status=all',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'artifact_name',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, plain.artifact_name)
        self.assertNotContains(response, case.artifact_name)
        self.assertContains(response, tag.artifact_name)
        self.assertContains(response, both.artifact_name)

    def test_artifact_list_both_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')
        # get objects
        plain = Artifact.objects.get(artifact_name='artifact_plain')
        case = Artifact.objects.get(artifact_name='artifact_case')
        tag = Artifact.objects.get(artifact_name='artifact_tag')
        both = Artifact.objects.get(artifact_name='artifact_both')

        # change config
        set_user_config(test_user, None, None)

        # change config
        tag_1 = Tag.objects.get(tag_name='tag_1')
        case_1 = Case.objects.get(case_name='case_1')
        set_user_config(test_user, case_1, tag_1)

        # get response with default JSON request
        response = self.client.post(
            '/filter/artifact/?artifact&status=all',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'artifact_name',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, plain.artifact_name)
        self.assertNotContains(response, case.artifact_name)
        self.assertNotContains(response, tag.artifact_name)
        self.assertContains(response, both.artifact_name)

    def test_artifact_list_open_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')
        # get objects
        closed = Artifact.objects.get(artifact_name='artifact_closed')
        open = Artifact.objects.get(artifact_name='artifact_open')

        # change config
        set_user_config(test_user, None, None)

        # get response with default JSON request
        response = self.client.post(
            '/filter/artifact/?artifact&status=open',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'artifact_name',
                'draw': '1',
            },
        )
        # compare
        self.assertContains(response, open.artifact_name)
        self.assertNotContains(response, closed.artifact_name)

    def test_artifact_list_closed_filter_context(self):
        """no filter applied"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')
        # get objects
        closed = Artifact.objects.get(artifact_name='artifact_closed')
        open = Artifact.objects.get(artifact_name='artifact_open')

        # change config
        set_user_config(test_user, None, None)

        # get response with default JSON request
        response = self.client.post(
            '/filter/artifact/?artifact&status=closed',
            {
                'order[0][column]': '1',
                'order[0][dir]': 'asc',
                'start': '0',
                'length': '25',
                'search[value]': '',
                'columns[1][data]': 'artifact_name',
                'draw': '1',
            },
        )
        # compare
        self.assertNotContains(response, open.artifact_name)
        self.assertContains(response, closed.artifact_name)

    def test_artifact_post_filter_config(self):
        """reset filter settings via URL"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')

        # get objects
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')

        # clear config
        set_user_config(test_user, None, None)

        # get config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='artifact_list'
        )

        # compare - settings after request
        self.assertEqual(user_config.filter_list_case, None)
        self.assertEqual(user_config.filter_list_tag.first(), None)
        self.assertEqual(user_config.filter_list_assigned_to_user_id, None)

        # post filter settings
        data = {
            'filter_list_case': case_1.case_id,
            'user_config_id': user_config.user_config_id,
        }
        self.client.post('/artifacts/artifact/', data)

        # refresh config
        user_config.refresh_from_db()
        # compare - settings before request
        self.assertEqual(user_config.filter_list_case, case_1)
        self.assertEqual(user_config.filter_list_tag.first(), None)
        self.assertEqual(user_config.filter_list_assigned_to_user_id, None)

        # post filter settings
        data = {
            'filter_list_tag': tag_1.tag_id,
            'user_config_id': user_config.user_config_id,
        }
        self.client.post('/artifacts/artifact/', data)

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_list_case, None)
        self.assertEqual(user_config.filter_list_tag.first(), tag_1)
        self.assertEqual(user_config.filter_list_assigned_to_user_id, None)

        # post filter settings
        data = {
            'filter_list_assigned_to_user_id': test_user.id,
            'user_config_id': user_config.user_config_id,
        }
        self.client.post('/artifacts/artifact/', data)

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_list_assigned_to_user_id, test_user)
        self.assertEqual(user_config.filter_list_tag.first(), None)
        self.assertEqual(user_config.filter_list_case, None)

    def test_artifact_clear_filter_config(self):
        """reset filter settings via URL"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )
        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # get config
        user_config = UserConfigModel.objects.get(
            user_config_username=test_user, filter_view='artifact_list'
        )

        # compare - settings before request
        self.assertEqual(user_config.filter_list_case, case_1)
        self.assertEqual(user_config.filter_list_tag.first(), tag_1)

        # get response, should reset filter config
        self.client.get('/artifacts/artifact/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_list_case, None)
        self.assertEqual(user_config.filter_list_tag.first(), None)

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        tag_1 = Tag.objects.get(tag_name='tag_1')
        set_user_config(test_user, case_1, tag_1)

        # refresh config
        user_config.refresh_from_db()
        # compare - settings before request
        self.assertEqual(user_config.filter_list_case, case_1)
        self.assertEqual(user_config.filter_list_tag.first(), tag_1)

        # get response, should reset filter config
        self.client.get('/artifacts/artifact/clear_filter/')

        # refresh config
        user_config.refresh_from_db()
        # compare - settings after request
        self.assertEqual(user_config.filter_list_case, None)
        self.assertEqual(user_config.filter_list_tag.first(), None)

    def test_artifact_list_filter_message(self):
        """test filter warning message"""

        # login testuser
        self.client.login(
            username='testuser_artifact_filter', password='9PUdBjlawv5WCdFXEYf6'
        )

        # get user
        test_user = User.objects.get(username='testuser_artifact_filter')

        # change config
        case_1 = Case.objects.get(case_name='case_1')
        set_user_config(test_user, case_1, None)

        # get response
        response = self.client.get('/artifacts/artifact/')
        # get messages
        messages = list(get_messages(response.wsgi_request))
        # compare
        self.assertEqual(
            str(messages[0]), 'Filter is active. Artifacts might be incomplete.'
        )
