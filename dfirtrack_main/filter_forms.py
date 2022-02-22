from django import forms
from django.contrib.auth.models import User

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import Case, Notestatus, Tag


class DocumentationFilterForm(forms.ModelForm):
    """documentation filter form"""

    # show all existing case objects
    filter_documentation_list_case = forms.ModelChoiceField(
        queryset=Case.objects.order_by('case_name'),
        empty_label='Filter for case',
        label='Filter for case',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # show all existing tag objects
    filter_documentation_list_tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.order_by('tag_name'),
        label='Filter for tag',
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    # show all existing user objects
    filter_documentation_list_user = forms.ModelChoiceField(
        queryset=User.objects.order_by('username'),
        empty_label='No user assigned',
        label='Filter for user',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # show all existing notestatus objects
    filter_documentation_list_notestatus = forms.ModelChoiceField(
        queryset=Notestatus.objects.order_by('notestatus_name'),
        empty_label='Filter for notestatus',
        label='Filter for notestatus',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    user_config_username = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
    )

    class Meta:

        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = (
            'filter_documentation_list_notestatus',
            'filter_documentation_list_case',
            'filter_documentation_list_user',
            'filter_documentation_list_tag',
            'user_config_username'
        )

        # non default form labeling
        labels = {
            'filter_documentation_list_keep': 'Remember filter settings (confirm by applying)',
        }


class SystemFilterForm(forms.ModelForm):
    """system filter form"""

        # show all existing case objects
    filter_system_list_case = forms.ModelChoiceField(
        queryset=Case.objects.order_by('case_name'),
        empty_label='Filter for case',
        label='Filter for case',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # show all existing tag objects
    filter_system_list_tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.order_by('tag_name'),
        label='Filter for tag',
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    # show all existing user objects
    filter_system_list_user = forms.ModelChoiceField(
        queryset=User.objects.order_by('username'),
        empty_label='No user assigned',
        label='Filter for user',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    user_config_username = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
    )

    class Meta:

        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = (
            'filter_system_list_case',
            'filter_system_list_tag',
            'filter_system_list_user',
            'user_config_username'
        )

        # non default form labeling
        labels = {
            'filter_system_list_keep': 'Remember filter settings (confirm by applying)',
        }
