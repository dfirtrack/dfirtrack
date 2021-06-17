from django import forms
from django.template.loader import render_to_string
from dfirtrack_main.models import Tag

class TagWidget(forms.CheckboxSelectMultiple):

    template_name = 'dfirtrack_main/widgets/tag_widget.html'

    def __init__(self, *args, **kwargs):
         super(TagWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        context = self.get_context(name, value, attrs)
        context['tags'] = Tag.objects.all()
        return render_to_string(self.template_name, context)