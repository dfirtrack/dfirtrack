from django import forms
from django.utils.translation import gettext_lazy
from dfirtrack_main.models import Analysisstatus, Case, Company, Domain, Dnsname, Location, Os, Reason, Serviceprovider, System, Systemstatus, Systemtype, Tag

class SystemImporterFileCsvConfigbasedForm(forms.Form):

    # file upload field (variable is used in request object)
    systemcsv = forms.FileField(
        label = 'CSV with systems (*)',
    )

class SystemImporterFileCsvFormbasedForm(forms.ModelForm, SystemImporterFileCsvConfigbasedForm):

    # reorder field choices
    systemstatus = forms.ModelChoiceField(
        queryset = Systemstatus.objects.order_by('systemstatus_name'),
        label = 'Systemstatus (*)',
        required = True,
        widget = forms.RadioSelect(),
    )

    # reorder field choices
    analysisstatus = forms.ModelChoiceField(
        queryset = Analysisstatus.objects.order_by('analysisstatus_name'),
        label = 'Analysisstatus',
        required = False,
        widget = forms.RadioSelect(),
    )

    # reorder field choices
    reason = forms.ModelChoiceField(
        label = gettext_lazy('Reason for investigation'),
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
        label = gettext_lazy('DNS name'),
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

    # case
    case = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        queryset = Case.objects.order_by('case_name'),
        label = 'Cases',
    )

    # company
    company = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        queryset = Company.objects.order_by('company_name'),
        label = 'Companies',
    )

    # tag
    tag = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        queryset = Tag.objects.order_by('tag_name'),
        label = 'Tags',
    )

    class Meta:
        model = System

        # this HTML forms are shown
        fields = (
            'systemstatus',
            'analysisstatus',
            'reason',
            'domain',
            'dnsname',
            'systemtype',
            'os',
            'location',
            'serviceprovider',
        )
