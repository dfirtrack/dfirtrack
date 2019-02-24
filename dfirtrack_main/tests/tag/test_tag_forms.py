from django.test import TestCase
from dfirtrack_main.forms import TagForm
from dfirtrack_main.models import Tagcolor

class TagFormTestCase(TestCase):
    """ tag form tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Tagcolor.objects.create(tagcolor_name='tagcolor_1')

    def test_tag_tagcolor_label(self):

        # get object
        form = TagForm()
        # compare
        self.assertEquals(form.fields['tagcolor'].label, 'Tag color (*)')

    def test_tag_name_label(self):

        # get object
        form = TagForm()
        # compare
        self.assertEquals(form.fields['tag_name'].label, 'Tag name (*)')

    def test_tag_note_label(self):

        # get object
        form = TagForm()
        # compare
        self.assertEquals(form.fields['tag_note'].label, 'Tag note')

    def test_tag_name_empty_with_tagcolor(self):

        # get foreign key object id
        tagcolor_id = Tagcolor.objects.get(tagcolor_name='tagcolor_1').tagcolor_id
        # get object
        form = TagForm(data = {'tag_name': '', 'tagcolor': tagcolor_id})
        # compare
        self.assertFalse(form.is_valid())

    def test_tag_name_filled_without_tagcolor(self):

        # get object
        form = TagForm(data = {'tag_name': 'tag_1'})
        # compare
        self.assertFalse(form.is_valid())

    def test_tag_name_filled_with_tagcolor(self):

        # get foreign key object id
        tagcolor_id = Tagcolor.objects.get(tagcolor_name='tagcolor_1').tagcolor_id
        # get object
        form = TagForm(data = {'tag_name': 'tag_1', 'tagcolor': tagcolor_id})
        # compare
        self.assertTrue(form.is_valid())

    def test_tag_name_proper_chars(self):

        # get foreign key object id
        tagcolor_id = Tagcolor.objects.get(tagcolor_name='tagcolor_1').tagcolor_id
        # get object
        form = TagForm(data = {'tag_name': 'tttttttttttttttttttttttttttttttttttttttttttttttttt', 'tagcolor': tagcolor_id})
        # compare
        self.assertTrue(form.is_valid())

    def test_tag_name_too_many_chars(self):

        # get foreign key object id
        tagcolor_id = Tagcolor.objects.get(tagcolor_name='tagcolor_1').tagcolor_id
        # get object
        form = TagForm(data = {'tag_name': 'ttttttttttttttttttttttttttttttttttttttttttttttttttt', 'tagcolor': tagcolor_id})
        # compare
        self.assertFalse(form.is_valid())
