from django import forms
from dfirtrack_main.models import Case
from dfirtrack_main.models import Notestatus
from dfirtrack_main.models import Tag


class DocumentationChoiceForm(forms.Form):
    """ documentation choice form """

    # show all existing case objects
    case = forms.ModelChoiceField(
        queryset = Case.objects.order_by('case_name'),
        empty_label = 'Filter for case',
        label = 'Filter for case',
        required = False,
    )

    # show all existing notestatus objects
    notestatus = forms.ModelChoiceField(
        queryset = Notestatus.objects.order_by('notestatus_name'),
        empty_label = 'Filter for notestatus',
        label = 'Filter for notestatus',
        required = False,
    )

    # show all existing tag objects
    tag = forms.ModelChoiceField(
        queryset = Tag.objects.order_by('tag_name'),
        empty_label = 'Filter for tag',
        label = 'Filter for tag',
        required = False,
    )
