from django import forms
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.models import System

class SystemImporterFileCsv(forms.ModelForm):

    # file upload field (variable is used in request object)
    systemcsv = forms.FileField()

    class Meta:
        model = System
        # this HTML forms are shown
        fields = ()

        """
        The following attributes are shown only if they are not selected for filling via CSV.
        That means the corresponding variable CSV_CHOICE_... in dfirtrack.config is set to False.
        """

        # add attributes as fields for manual editing if not automatically filled
        if not dfirtrack_config.CSV_CHOICE_ANALYSISSTATUS:
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

        # special form type or option
        widgets = {}

        # define widgets for choosen fields
        if not dfirtrack_config.CSV_CHOICE_ANALYSISSTATUS:
            widgets['analysisstatus'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_REASON:
            widgets['reason'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_DOMAIN:
            widgets['domain'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_DNSNAME:
            widgets['dnsname'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_SYSTEMTYPE:
            widgets['systemtype'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_OS:
            widgets['os'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_LOCATION:
            widgets['location'] = forms.RadioSelect()
        if not dfirtrack_config.CSV_CHOICE_SERVICEPROVIDER:
            widgets['serviceprovider'] = forms.RadioSelect()

class SystemIpFileImport(forms.ModelForm):

    # file upload field (variable is used in request object)
    systemipcsv = forms.FileField()

    class Meta:
        model = System
        # this HTML forms are shown
        fields = (
            'systemstatus',
            'analysisstatus',
            'reason',
            'systemtype',
            'domain',
            'dnsname',
            'os',
            'company',
            'location',
            'serviceprovider',
            'contact',
            'tag',
            'case',
        )
        # special form type or option
        widgets = {
            'systemstatus': forms.RadioSelect(),
            'analysisstatus': forms.RadioSelect(),
            'reason': forms.RadioSelect(),
            'systemtype': forms.RadioSelect(),
            'domain': forms.RadioSelect(),
            'dnsname': forms.RadioSelect(),
            'os': forms.RadioSelect(),
            'company': forms.CheckboxSelectMultiple(),
            'location': forms.RadioSelect(),
            'serviceprovider': forms.RadioSelect(),
            'contact': forms.RadioSelect(),
            'tag': forms.CheckboxSelectMultiple(),
            'case': forms.CheckboxSelectMultiple(),
        }

class SystemTagFileImport(forms.Form):

    # file upload field (variable is used in request object)
    systemtagcsv = forms.FileField()
