from django import forms

class SystemExporterMarkdownConfigForm(forms.Form):

    markdown_path = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={
            'size': '55',
            'style': 'font-family: monospace',
        }),
        label = 'Path for the markdown documentation export',
    )

    markdown_sorting_choices = [
        ('domainsorted', 'Sorted by domain'),
        ('systemsorted', 'Sorted by system'),
    ]

    markdown_sorting = forms.ChoiceField(
        required = True,
        widget = forms.RadioSelect(),
        label = 'Choose sorting for system markdown export',
        choices = markdown_sorting_choices,
    )

class SystemExporterSpreadsheetCsvConfigForm(forms.Form):

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

class SystemImporterFileCsvConfigForm(forms.Form):

    csv_choice_ip = forms.BooleanField(
        required = False,
        label = 'CSV file contains IP addresses',
    )
