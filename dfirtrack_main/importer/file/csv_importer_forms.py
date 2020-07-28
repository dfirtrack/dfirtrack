from constance import config as constance_config
from django import forms
from django.utils.translation import gettext_lazy
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.models import Domain, Dnsname, Location, Os, Reason, Serviceprovider, System, Systemtype

class SystemImporterFileCsvConfigbasedForm(forms.Form):

    # file upload field (variable is used in request object)
    systemcsv = forms.FileField(
        label = 'CSV with systems (*)',
    )

class SystemImporterFileCsvFormbasedForm(forms.ModelForm, SystemImporterFileCsvConfigbasedForm):

    # reorder field choices
    reason = forms.ModelChoiceField(
        label = gettext_lazy('Reason'),
        queryset = Reason.objects.order_by('reason_name'),
        required = False,
        widget = forms.RadioSelect(),
    )
    domain = forms.ModelChoiceField(
        label = gettext_lazy('Domain'),
        queryset = Domain.objects.order_by('domain_name'),
        required = False,
        widget = forms.RadioSelect(),
    )
    dnsname = forms.ModelChoiceField(
        label = gettext_lazy('Dnsname'),
        queryset = Dnsname.objects.order_by('dnsname_name'),
        required = False,
        widget = forms.RadioSelect(),
    )
    systemtype = forms.ModelChoiceField(
        label = gettext_lazy('Systemtype'),
        queryset = Systemtype.objects.order_by('systemtype_name'),
        required = False,
        widget = forms.RadioSelect(),
    )
    os = forms.ModelChoiceField(
        label = gettext_lazy('Os'),
        queryset = Os.objects.order_by('os_name'),
        required = False,
        widget = forms.RadioSelect(),
    )
    location = forms.ModelChoiceField(
        label = gettext_lazy('Location'),
        queryset = Location.objects.order_by('location_name'),
        required = False,
        widget = forms.RadioSelect(),
    )
    serviceprovider = forms.ModelChoiceField(
        label = gettext_lazy('Serviceprovider'),
        queryset = Serviceprovider.objects.order_by('serviceprovider_name'),
        required = False,
        widget = forms.RadioSelect(),
    )

# TODO: CheckboxSelectMultiple does not work properly
#    # reorder field choices
#    case = forms.ModelChoiceField(
#        label = gettext_lazy('Case'),
#        queryset = Case.objects.order_by('case_name'),
#        required = False,
#        widget=forms.CheckboxSelectMultiple(),
#    )

# TODO: CheckboxSelectMultiple does not work properly
#    # reorder field choices
#    company = forms.ModelChoiceField(
#        label = gettext_lazy('Company'),
#        queryset = Company.objects.order_by('company_name'),
#        required = False,
#        widget=forms.CheckboxSelectMultiple(),
#    )

# TODO: CheckboxSelectMultiple does not work properly
#    # reorder field choices
#    tag = forms.ModelChoiceField(
#        label = gettext_lazy('Tag'),
#        queryset = Tag.objects.order_by('tag_name'),
#        required = False,
#        widget=forms.CheckboxSelectMultiple(),
#    )

    class Meta:
        model = System

        # this HTML forms are shown
        fields = ()

        # add attributes as fields for manual editing if not automatically filled
        if not constance_config.CSV_CHOICE_SYSTEMSTATUS:
            fields += ('systemstatus',)
        if not constance_config.CSV_CHOICE_ANALYSISSTATUS:
            fields += ('analysisstatus',)
        fields += (
            'reason',
            'domain',
            'dnsname',
            'systemtype',
            'os',
            'location',
            'serviceprovider',
            'case',
            'company',
            'tag',
        )


        # define widgets for choosen fields
        widgets = {
            'systemstatus': forms.RadioSelect(),
            'analysisstatus': forms.RadioSelect(),
            'case': forms.CheckboxSelectMultiple(),
            'company': forms.CheckboxSelectMultiple(),
            'tag': forms.CheckboxSelectMultiple(),
        }
