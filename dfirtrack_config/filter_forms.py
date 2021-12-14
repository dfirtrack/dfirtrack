from django import forms
from django.contrib.auth.models import User

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.filter_forms import BaseFilterForm


class AssignmentFilterForm(forms.ModelForm, BaseFilterForm):
    """assignment filter form"""

    # show all existing user objects
    user = forms.ModelChoiceField(
        queryset=User.objects.order_by('username'),
        empty_label='No user assigned',
        label='Filter for user',
        required=False,
    )

    class Meta:

        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = ('filter_assignment_view_keep',)

        # non default form labeling
        labels = {
            'filter_assignment_view_keep': 'Remember filter settings (confirm by applying)',
        }
