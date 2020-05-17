from django import forms
from dfirtrack_main.models import System

class SystemImporterFileCsv(forms.Form):

    # file upload field (variable is used in request object)
    systemcsv = forms.FileField()

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
