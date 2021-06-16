from django import forms
from django.template.loader import render_to_string

class TagWidget(forms.SelectMultiple):

    template_name = 'dfirtrack_main/tag/tag_widget.html'

    def __init__(self, *args, **kwargs):
         super(TagWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        context = {
            "test": "Tag"
        }
        return render_to_string(self.template_name, context)