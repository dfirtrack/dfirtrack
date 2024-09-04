from django import forms
from django.core.exceptions import ValidationError
from djangoql.exceptions import DjangoQLLexerError
from djangoql.parser import DjangoQLParser, DjangoQLParserError

from dfirtrack_config.models import UserConfigModel
from dfirtrack_main.models import Notestatus


def validate_filter_query(value):
    djangoqlParser = DjangoQLParser()
    try:
        djangoqlParser.parse(input=value)
    except (DjangoQLParserError, DjangoQLLexerError):
        raise ValidationError("Syntax error")


class GeneralFilterForm(forms.ModelForm):
    """general filter form"""

    filter_query = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        validators=[validate_filter_query],
        label="Filter query",
    )

    # config model pk
    user_config_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        # model
        model = UserConfigModel

        # this HTML forms are shown
        fields = (
            'filter_query',
            'user_config_id',
        )
