from django import forms
from django.utils.translation import gettext_lazy
from dfirtrack_main.models import Case, Company, Domain, Dnsname, Location, Os, Reason, Serviceprovider, System, Systemtype, Tag

class SystemImporterFileCsvConfigbasedForm(forms.Form):

    # file upload field (variable is used in request object)
    systemcsv = forms.FileField(
        label = 'CSV with systems (*)',
    )

class SystemImporterFileCsvFormbasedForm(forms.ModelForm, SystemImporterFileCsvConfigbasedForm):

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

    # create empty list for available cases
    case_choices = []
    # get all cases
    case_all = Case.objects.order_by('case_name')
    # prepare choices (append tupel consisting of case_id and case_name to list (therefore double brackets))
    for case in case_all:
        case_choices.append((case.case_id, case.case_name))
    # create field
    case = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        choices = case_choices,
        label = 'Cases',
    )

    # company

    # create empty list for available companies
    company_choices = []
    # get all companies
    company_all = Company.objects.order_by('company_name')
    # prepare choices (append tupel consisting of company_id and company_name to list (therefore double brackets))
    for company in company_all:
        company_choices.append((company.company_id, company.company_name))
    # create field
    company = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        choices = company_choices,
        label = 'Companies',
    )

    # tag

    # create empty list for available tags
    tag_choices = []
    # get all tags
    tag_all = Tag.objects.order_by('tag_name')
    # prepare choices (append tupel consisting of tag_id and tag_name to list (therefore double brackets))
    for tag in tag_all:
        tag_choices.append((tag.tag_id, tag.tag_name))
    # create field
    tag = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        choices = tag_choices,
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

        # non default form labeling
        labels = {
            'systemstatus': gettext_lazy('Systemstatus (*)'),
        }

        # define widgets for choosen fields
        widgets = {
            'systemstatus': forms.RadioSelect(),
            'analysisstatus': forms.RadioSelect(),
        }
