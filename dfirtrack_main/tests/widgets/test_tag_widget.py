from django.test import TestCase

from dfirtrack_main.models import Tag, Tagcolor
from dfirtrack_main.widgets import TagWidget


class TagWidgetTestCase(TestCase):
    @classmethod
    def setUpTestData(self):

        # create object
        tag_color_1 = Tagcolor.objects.create(tagcolor_name="tag_color_1")
        Tag.objects.create(tag_name='tag_1', tagcolor=tag_color_1)

    def test_tag_widget_template_name(self):
        """test tag widget template name"""
        # create widget
        tagWidget = TagWidget()

        # check
        self.assertEqual(
            tagWidget.template_name, 'dfirtrack_main/widgets/tag_widget.html'
        )

    def test_tag_widget_context(self):
        """test tag wideget context"""
        # create widget
        tagWidget = TagWidget()
        value = ['1']
        context = tagWidget.get_context('tag', value, None)

        # check
        self.assertEqual(context['widget']['name'], 'tag')
        self.assertEqual(context['widget']['value'], value)

    def test_tag_widget_render_output(self):
        """test tag widget render"""
        # create widget
        tagWidget = TagWidget()

        # get render output
        output_string = tagWidget.render('tag', list(), {'id': 'id_tag'})

        # check
        self.assertTrue('tag_1' in output_string)
        self.assertTrue('tag_color_1' in output_string)
