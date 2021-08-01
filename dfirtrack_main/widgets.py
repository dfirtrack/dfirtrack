from django import forms
from django.template.loader import render_to_string

from dfirtrack_main.models import Tag


class TagWidget(forms.CheckboxSelectMultiple):
    ''' Custom tag widget '''

    # widget template for dynamic tags (javascript based)
    template_name = 'dfirtrack_main/widgets/tag_widget.html'

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        # get all context information parent function
        context = self.get_context(name, value, attrs)
        # get all tags, import for tag colors
        context['tags'] = Tag.objects.all()
        # render custom template with context information
        return render_to_string(self.template_name, context)