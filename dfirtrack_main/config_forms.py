from django import forms
from dfirtrack_main.models import Analysisstatus, Case, Company, Dnsname, Domain, Location, Os, Reason, Serviceprovider, Systemstatus, Systemtype, Tag

class SystemExporterMarkdownConfigForm(forms.Form):
    """ system exporter markdown config form """

    markdown_path = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={
            'size': '55',
            'style': 'font-family: monospace',
        }),
        label = 'Path for the markdown documentation export',
    )

    # prepare choices
    markdown_sorting_choices = [
        ('domainsorted', 'Sorted by domain'),
        ('systemsorted', 'Sorted by system'),
    ]
    # create field
    markdown_sorting = forms.ChoiceField(
        required = True,
        widget = forms.RadioSelect(),
        label = 'Choose sorting for system markdown export',
        choices = markdown_sorting_choices,
    )

class SystemExporterSpreadsheetCsvConfigForm(forms.Form):
    """ system exporter spreadsheet config form (CSV and XLS) """

    spread_system_id = forms.BooleanField(
        required = False,
        label = 'Export system ID',
    )

    spread_dnsname = forms.BooleanField(
        required = False,
        label = 'Export DNS name',
    )

    spread_domain = forms.BooleanField(
        required = False,
        label = 'Export domain',
    )

    spread_systemstatus = forms.BooleanField(
        required = False,
        label = 'Export systemstatus',
    )

    spread_analysisstatus = forms.BooleanField(
        required = False,
        label = 'Export analysisstatus',
    )

    spread_reason = forms.BooleanField(
        required = False,
        label = 'Export reason',
    )

    spread_recommendation = forms.BooleanField(
        required = False,
        label = 'Export recommendation',
    )

    spread_systemtype = forms.BooleanField(
        required = False,
        label = 'Export systemtype',
    )

    spread_ip = forms.BooleanField(
        required = False,
        label = 'Export IP',
    )

    spread_os = forms.BooleanField(
        required = False,
        label = 'Export OS',
    )

    spread_company = forms.BooleanField(
        required = False,
        label = 'Export company',
    )

    spread_location = forms.BooleanField(
        required = False,
        label = 'Export location',
    )

    spread_serviceprovider = forms.BooleanField(
        required = False,
        label = 'Export serviceprovider',
    )

    spread_tag = forms.BooleanField(
        required = False,
        label = 'Export tag',
    )

    spread_case = forms.BooleanField(
        required = False,
        label = 'Export case',
    )

    spread_system_create_time = forms.BooleanField(
        required = False,
        label = 'Export system create time',
    )

    spread_system_modify_time = forms.BooleanField(
        required = False,
        label = 'Export system modify time',
    )

class SystemExporterSpreadsheetXlsConfigForm(SystemExporterSpreadsheetCsvConfigForm):
    """ system exporter spreadsheet config form (XLS only) """

    spread_worksheet_systemstatus = forms.BooleanField(
        required = False,
        label = 'Export worksheet to explain systemstatus',
    )

    spread_worksheet_analysisstatus = forms.BooleanField(
        required = False,
        label = 'Export worksheet to explain analysisstatus',
    )

    spread_worksheet_reason = forms.BooleanField(
        required = False,
        label = 'Export worksheet to explain reason',
    )

    spread_worksheet_recommendation = forms.BooleanField(
        required = False,
        label = 'Export worksheet to explain recommendation',
    )

    spread_worksheet_tag = forms.BooleanField(
        required = False,
        label = 'Export worksheet to explain tag',
    )

class SystemImporterFileCsvFormbasedConfigForm(forms.Form):
    """ system importer CSV config form (config and form based) """

    # general settings
    csv_skip_existing_system = forms.BooleanField(
        required = False,
        label = 'Skip existing systems',
    )
    csv_column_system = forms.IntegerField(
        required = False,
        label = 'Number of the column in the CSV file that contains the system name',
        widget = forms.NumberInput(attrs={
            #'style': 'width:6ch',
            'size': '3',
        }),
        min_value = 1,
        max_value = 256,
    )
    csv_headline = forms.BooleanField(
        required = False,
        label = 'CSV file contains a headline row',
    )
    # IP related settings
    csv_choice_ip = forms.BooleanField(
        required = False,
        label = 'CSV file contains IP addresses',
    )
    csv_remove_ip = forms.BooleanField(
        required = False,
        label = 'Remove / overwrite existing IP addresses for already existing systems',
    )
    csv_column_ip = forms.IntegerField(
        required = False,
        label = 'Number of the column in the CSV file that contains the IP addresses',
        widget = forms.NumberInput(attrs={
            #'style': 'width:6ch',
            'size': '3',
        }),
        min_value = 1,
        max_value = 256,
    )
    # overriding settings
    csv_remove_case = forms.BooleanField(
        required = False,
        label = 'Remove / overwrite existing cases for already existing systems',
    )
    csv_remove_company = forms.BooleanField(
        required = False,
        label = 'Remove / overwrite existing companies for already existing systems',
    )
    csv_remove_tag = forms.BooleanField(
        required = False,
        label = 'Remove / overwrite existing tags for already existing systems',
    )

    def clean(self):
        """ custom field validation """

        # get form data
        cleaned_data = super().clean()

        # get relevant values
        csv_column_system = self.cleaned_data['csv_column_system']
        csv_column_ip = self.cleaned_data['csv_column_ip']

        # compare column values
        if csv_column_system == csv_column_ip:
            raise forms.ValidationError('The columns for system and IP should not have the same values.')

        return cleaned_data

class SystemImporterFileCsvConfigbasedConfigForm(SystemImporterFileCsvFormbasedConfigForm):
    """ system importer CSV config form (config based only) """

    # systemstatus

    # create empty list for available systemstatus
    systemstatus_choices = []
    # get all systemstatus
    systemstatus_all = Systemstatus.objects.order_by('systemstatus_id')
    # prepare choices (append tupel consisting of systemstatus_id and systemstatus_name to list (therefore double brackets))
    for systemstatus in systemstatus_all:
        systemstatus_choices.append((systemstatus.systemstatus_id, systemstatus.systemstatus_name))
    # create field
    csv_default_systemstatus = forms.ChoiceField(
        required = True,
        widget = forms.RadioSelect(),
        choices = systemstatus_choices,
        label = 'Set systemstatus',
    )

    # analysisstatus

    # create empty list for available analysisstatus
    analysisstatus_choices = []
    # get all analysisstatus
    analysisstatus_all = Analysisstatus.objects.order_by('analysisstatus_id')
    # prepare choices (append tupel consisting of analysisstatus_id and analysisstatus_name to list (therefore double brackets))
    for analysisstatus in analysisstatus_all:
        analysisstatus_choices.append((analysisstatus.analysisstatus_id, analysisstatus.analysisstatus_name))
    # create field
    csv_default_analysisstatus = forms.ChoiceField(
        required = True,
        widget = forms.RadioSelect(),
        choices = analysisstatus_choices,
        label = 'Set analysisstatus',
    )

    # reason

    # create empty list for available reason
    reason_choices = []
    # append empty choice
    reason_choices.append(('', 'None selected'))
    # get all reasons
    reason_all = Reason.objects.order_by('reason_name')
    # prepare choices (append tupel consisting of reason_id and reason_name to list (therefore double brackets))
    for reason in reason_all:
        reason_choices.append((reason.reason_id, reason.reason_name))
    # create field
    csv_default_reason = forms.ChoiceField(
        required = False,
        choices = reason_choices,
        label = 'Set reason',
    )

    # domain

    # create empty list for available domain
    domain_choices = []
    # append empty choice
    domain_choices.append(('', 'None selected'))
    # get all domains
    domain_all = Domain.objects.order_by('domain_name')
    # prepare choices (append tupel consisting of domain_id and domain_name to list (therefore double brackets))
    for domain in domain_all:
        domain_choices.append((domain.domain_id, domain.domain_name))
    # create field
    csv_default_domain = forms.ChoiceField(
        required = False,
        choices = domain_choices,
        label = 'Set domain',
    )

    # dnsname

    # create empty list for available dnsname
    dnsname_choices = []
    # append empty choice
    dnsname_choices.append(('', 'None selected'))
    # get all dnsnames
    dnsname_all = Dnsname.objects.order_by('dnsname_name')
    # prepare choices (append tupel consisting of dnsname_id and dnsname_name to list (therefore double brackets))
    for dnsname in dnsname_all:
        dnsname_choices.append((dnsname.dnsname_id, dnsname.dnsname_name))
    # create field
    csv_default_dnsname = forms.ChoiceField(
        required = False,
        choices = dnsname_choices,
        label = 'Set DNS name',
    )

    # systemtype

    # create empty list for available systemtype
    systemtype_choices = []
    # append empty choice
    systemtype_choices.append(('', 'None selected'))
    # get all systemtypes
    systemtype_all = Systemtype.objects.order_by('systemtype_name')
    # prepare choices (append tupel consisting of systemtype_id and systemtype_name to list (therefore double brackets))
    for systemtype in systemtype_all:
        systemtype_choices.append((systemtype.systemtype_id, systemtype.systemtype_name))
    # create field
    csv_default_systemtype = forms.ChoiceField(
        required = False,
        choices = systemtype_choices,
        label = 'Set systemtype',
    )

    # os

    # create empty list for available os
    os_choices = []
    # append empty choice
    os_choices.append(('', 'None selected'))
    # get all oss
    os_all = Os.objects.order_by('os_name')
    # prepare choices (append tupel consisting of os_id and os_name to list (therefore double brackets))
    for os in os_all:
        os_choices.append((os.os_id, os.os_name))
    # create field
    csv_default_os = forms.ChoiceField(
        required = False,
        choices = os_choices,
        label = 'Set OS',
    )

    # location

    # create empty list for available location
    location_choices = []
    # append empty choice
    location_choices.append(('', 'None selected'))
    # get all locations
    location_all = Location.objects.order_by('location_name')
    # prepare choices (append tupel consisting of location_id and location_name to list (therefore double brackets))
    for location in location_all:
        location_choices.append((location.location_id, location.location_name))
    # create field
    csv_default_location = forms.ChoiceField(
        required = False,
        choices = location_choices,
        label = 'Set location',
    )

    # serviceprovider

    # create empty list for available serviceprovider
    serviceprovider_choices = []
    # append empty choice
    serviceprovider_choices.append(('', 'None selected'))
    # get all serviceproviders
    serviceprovider_all = Serviceprovider.objects.order_by('serviceprovider_name')
    # prepare choices (append tupel consisting of serviceprovider_id and serviceprovider_name to list (therefore double brackets))
    for serviceprovider in serviceprovider_all:
        serviceprovider_choices.append((serviceprovider.serviceprovider_id, serviceprovider.serviceprovider_name))
    # create field
    csv_default_serviceprovider = forms.ChoiceField(
        required = False,
        choices = serviceprovider_choices,
        label = 'Set serviceprovider',
    )

    # case

    # create empty list for available case
    case_choices = []
    # get all cases
    case_all = Case.objects.order_by('case_name')
    # prepare choices (append tupel consisting of case_id and case_name to list (therefore double brackets))
    for case in case_all:
        case_choices.append((case.case_id, case.case_name))
    # create field
    csv_default_case = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        choices = case_choices,
        label = 'Set cases',
    )

    # company

    # create empty list for available company
    company_choices = []
    # get all companies
    company_all = Company.objects.order_by('company_name')
    # prepare choices (append tupel consisting of company_id and company_name to list (therefore double brackets))
    for company in company_all:
        company_choices.append((company.company_id, company.company_name))
    # create field
    csv_default_company = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        choices = company_choices,
        label = 'Set companies',
    )

    # tag

    # create empty list for available tag
    tag_choices = []
    # get all tags
    tag_all = Tag.objects.order_by('tag_name')
    # prepare choices (append tupel consisting of tag_id and tag_name to list (therefore double brackets))
    for tag in tag_all:
        tag_choices.append((tag.tag_id, tag.tag_name))
    # create field
    csv_default_tag = forms.MultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        required = False,
        choices = tag_choices,
        label = 'Set tags',
    )
