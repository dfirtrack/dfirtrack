from django import forms
import dfirtrack.config as dfirtrack_config
from dfirtrack_main.models import System

class SystemImporterFileCsv(forms.ModelForm):

    # file upload field (variable is used in request object)
    systemcsv = forms.FileField()

    class Meta:
        model = System

        """
        The following attributes are only shown if they are not selected for filling via CSV or dfirtrack.config.
        That means the corresponding variable CSV_CHOICE_... in dfirtrack.config is set to False.
        """

        # this HTML forms are shown
        fields = ()

        # add attributes as fields for manual editing if not automatically filled
        if not dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS:
            fields += ('systemstatus',)
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
        if not dfirtrack_config.CSV_CHOICE_TAG:
            fields += ('tag',)

        # special form type or option
        widgets = {}

        # define widgets for choosen fields
        if not dfirtrack_config.CSV_CHOICE_SYSTEMSTATUS:
            widgets['systemstatus'] = forms.RadioSelect()
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
        if not dfirtrack_config.CSV_CHOICE_TAG:
            widgets['tag'] = forms.CheckboxSelectMultiple()
