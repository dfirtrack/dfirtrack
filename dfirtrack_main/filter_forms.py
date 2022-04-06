from django import forms
from django.contrib.auth.models import User

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import Case, Notestatus, Tag


class GeneralFilterForm(forms.ModelForm):
    """general filter form"""

    # show all existing case objects
    filter_list_case = forms.ModelChoiceField(
        queryset=Case.objects.order_by('case_name'),
        empty_label='Filter for case',
        label='Filter for case',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # show all existing tag objects
    filter_list_tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.order_by('tag_name'),
        label='Filter for tag',
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    # show all existing user objects
    filter_list_assigned_to_user_id = forms.ModelChoiceField(
        queryset=User.objects.order_by('username'),
        empty_label='No user assigned',
        label='Filter for user',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # config model pk
    user_config_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:

        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = (
            'filter_list_case',
            'filter_list_tag',
            'filter_list_assigned_to_user_id',
            'user_config_id'
        )

class DocumentationFilterForm(GeneralFilterForm):
    """documentation filter form"""

    # show all existing notestatus objects
    filter_list_status = forms.ModelChoiceField(
        queryset=Notestatus.objects.order_by('notestatus_name'),
        empty_label='Filter for notestatus',
        label='Filter for notestatus',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # set initial status value to be selected during rendering
    def __init__(self, *args, **kwargs):
        user_config = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if user_config and user_config.filter_list_status:
            self.initial['filter_list_status'] = user_config.filter_list_status.notestatus_id

    # save status value from cleaned data
    def save(self, *args, **kwargs):   
        if 'filter_list_status' in self.changed_data:
            self.instance.filter_list_status = self.cleaned_data['filter_list_status']
        return super().save(*args, **kwargs)

    class Meta:

        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = (
            'filter_list_case',
            'filter_list_tag',
            'filter_list_assigned_to_user_id',
            'user_config_id',
            'filter_list_status'
        )