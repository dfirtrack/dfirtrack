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
    if not dfirtrack_config.CSV_CHOICE_REASON:
        reason = forms.ModelChoiceField(
            label = gettext_lazy('Reason'),
            queryset = Reason.objects.order_by('reason_name'),
            required = False,
            widget = forms.RadioSelect(),
        )
    if not dfirtrack_config.CSV_CHOICE_DOMAIN:
        domain = forms.ModelChoiceField(
            label = gettext_lazy('Domain'),
            queryset = Domain.objects.order_by('domain_name'),
            required = False,
            widget = forms.RadioSelect(),
        )
    if not dfirtrack_config.CSV_CHOICE_DNSNAME:
        dnsname = forms.ModelChoiceField(
            label = gettext_lazy('Dnsname'),
            queryset = Dnsname.objects.order_by('dnsname_name'),
            required = False,
            widget = forms.RadioSelect(),
        )
    if not dfirtrack_config.CSV_CHOICE_SYSTEMTYPE:
        systemtype = forms.ModelChoiceField(
            label = gettext_lazy('Systemtype'),
            queryset = Systemtype.objects.order_by('systemtype_name'),
            required = False,
            widget = forms.RadioSelect(),
        )
    if not dfirtrack_config.CSV_CHOICE_OS:
        os = forms.ModelChoiceField(
            label = gettext_lazy('Os'),
            queryset = Os.objects.order_by('os_name'),
            required = False,
            widget = forms.RadioSelect(),
        )
    if not dfirtrack_config.CSV_CHOICE_LOCATION:
        location = forms.ModelChoiceField(
            label = gettext_lazy('Location'),
            queryset = Location.objects.order_by('location_name'),
            required = False,
            widget = forms.RadioSelect(),
        )
    if not dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER:
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

        """
        The following attributes are only shown if they are not selected for filling via CSV or dfirtrack.config.
        That means the corresponding variable CSV_CHOICE_... in dfirtrack.config is set to False.
        """

        # this HTML forms are shown
        fields = ()

        # add attributes as fields for manual editing if not automatically filled
        if not constance_config.CSV_CHOICE_SYSTEMSTATUS:
            fields += ('systemstatus',)
        if not constance_config.CSV_CHOICE_ANALYSISSTATUS:
            fields += ('analysisstatus',)
        if not dfirtrack_config.CSV_CHOICE_REASON:
            fields += ('reason',)
        if not dfirtrack_config.CSV_CHOICE_DOMAIN:
            fields += ('domain',)
        if not dfirtrack_config.CSV_CHOICE_DNSNAME:
            fields += ('dnsname',)
        if not dfirtrack_config.CSV_CHOICE_SYSTEMTYPE:
            fields += ('systemtype',)
        if not dfirtrack_config.CSV_CHOICE_OS:
            fields += ('os',)
        if not dfirtrack_config.CSV_CHOICE_LOCATION:
            fields += ('location',)
        if not dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER:
            fields += ('serviceprovider',)
        if not dfirtrack_config.CSV_CHOICE_CASE:
            fields += ('case',)
        if not dfirtrack_config.CSV_CHOICE_COMPANY:
            fields += ('company',)
        if not dfirtrack_config.CSV_CHOICE_TAG:
            fields += ('tag',)

        # special form type or option
        widgets = {}

        # define widgets for choosen fields
        if not constance_config.CSV_CHOICE_SYSTEMSTATUS:
            widgets['systemstatus'] = forms.RadioSelect()
        if not constance_config.CSV_CHOICE_ANALYSISSTATUS:
            widgets['analysisstatus'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_CASE:
            widgets['case'] = forms.CheckboxSelectMultiple()
        if not dfirtrack_config.CSV_CHOICE_COMPANY:
            widgets['company'] = forms.CheckboxSelectMultiple()
        if not dfirtrack_config.CSV_CHOICE_TAG:
            widgets['tag'] = forms.CheckboxSelectMultiple()
