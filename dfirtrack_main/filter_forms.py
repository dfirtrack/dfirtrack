from django import forms

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import Case, Notestatus, Tag


class BaseFilterForm(forms.Form):
    """ base filter form with shared fields """

    # show all existing case objects
    case = forms.ModelChoiceField(
        queryset = Case.objects.order_by('case_name'),
        empty_label = 'Filter for case',
        label = 'Filter for case',
        required = False,
    )

    # show all existing tag objects
    tag = forms.ModelChoiceField(
        queryset = Tag.objects.order_by('tag_name'),
        empty_label = 'Filter for tag',
        label = 'Filter for tag',
        required = False,
    )

class DocumentationFilterForm(forms.ModelForm, BaseFilterForm):
    """ documentation filter form """

    # show all existing notestatus objects
    notestatus = forms.ModelChoiceField(
        queryset = Notestatus.objects.order_by('notestatus_name'),
        empty_label = 'Filter for notestatus',
        label = 'Filter for notestatus',
        required = False,
    )

    class Meta:

        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = (
            'filter_documentation_list_keep',
        )

        # non default form labeling
        labels = {
            'filter_documentation_list_keep': 'Remember filter settings (confirm by applying)',
        }

class SystemFilterForm(forms.ModelForm, BaseFilterForm):
    """ system filter form """

    class Meta:

        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = (
            'filter_system_list_keep',
        )

        # non default form labeling
        labels = {
            'filter_system_list_keep': 'Remember filter settings (confirm by applying)',
        }
