from django import forms
from dfirtrack_artifacts.models import Artifactstatus
from dfirtrack_config.models import ArtifactExporterSpreadsheetXlsConfigModel, SystemImporterFileCsvConfigbasedConfigModel, SystemImporterFileCsvFormbasedConfigModel

class ArtifactExporterSpreadsheetXlsConfigForm(forms.ModelForm):
    """ artifact exporter spreadsheet xls config form """

# TODO: CheckboxSelectMultiple does not work properly
#    # reorder field choices
#    artifactlist_choice_artifactstatus = forms.ModelChoiceField(
#        required = False,
#        widget = forms.CheckboxSelectMultiple(),
#        label = 'Export only artifacts with this artifactstatus',
#        queryset = Artifactstatus.objects.all()
#    )

    class Meta:

        # model
        model = ArtifactExporterSpreadsheetXlsConfigModel

        # this HTML forms are shown
        fields = (
            'artifactlist_xls_choice_artifactstatus',
            'artifactlist_xls_artifact_id',
            'artifactlist_xls_system_id',
            'artifactlist_xls_system_name',
            'artifactlist_xls_artifactstatus',
            'artifactlist_xls_artifacttype',
            'artifactlist_xls_artifact_source_path',
            'artifactlist_xls_artifact_storage_path',
            'artifactlist_xls_artifact_note',
            'artifactlist_xls_artifact_md5',
            'artifactlist_xls_artifact_sha1',
            'artifactlist_xls_artifact_sha256',
            'artifactlist_xls_artifact_create_time',
            'artifactlist_xls_artifact_modify_time',
            'artifactlist_xls_worksheet_artifactstatus',
            'artifactlist_xls_worksheet_artifacttype',
        )

        labels = {
            'artifactlist_xls_choice_artifactstatus': 'Export only artifacts with this artifactstatus',
            'artifactlist_xls_artifact_id': 'Export artifact ID',
            'artifactlist_xls_system_id': 'Export system ID',
            'artifactlist_xls_system_name': 'Export system name',
            'artifactlist_xls_artifactstatus': 'Export artifactstatus',
            'artifactlist_xls_artifacttype': 'Export artifacttype',
            'artifactlist_xls_artifact_source_path': 'Export source path',
            'artifactlist_xls_artifact_storage_path': 'Export storage path',
            'artifactlist_xls_artifact_note': 'Export note',
            'artifactlist_xls_artifact_md5': 'Export MD5',
            'artifactlist_xls_artifact_sha1': 'Export SHA1',
            'artifactlist_xls_artifact_sha256': 'Export SHA256',
            'artifactlist_xls_artifact_create_time': 'Export create time',
            'artifactlist_xls_artifact_modify_time': 'Export modify time',
            'artifactlist_xls_worksheet_artifactstatus': 'Export worksheet to explain artifactstatus',
            'artifactlist_xls_worksheet_artifacttype': 'Export worksheet to explain artifacttype',
        }

        widgets = {
            'artifactlist_xls_choice_artifactstatus': forms.CheckboxSelectMultiple(),
        }

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
        ('dom', 'Sorted by domain'),
        ('sys', 'Sorted by system'),
    ]
    # create field
    markdown_sorting = forms.ChoiceField(
        required = True,
        widget = forms.RadioSelect(),
        label = 'Choose sorting for system markdown export',
        choices = markdown_sorting_choices,
    )

# TODO: switch to model form
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

# TODO: switch to model form
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

class SystemImporterFileCsvConfigbasedConfigForm(forms.ModelForm):
    """ system importer CSV config form (config based only) """

    class Meta:

        # model
        model = SystemImporterFileCsvConfigbasedConfigModel

        # this HTML forms are shown
        fields = (
            'csv_skip_existing_system',
            'csv_column_system',
            'csv_headline',
            'csv_choice_ip',
            'csv_remove_ip',
            'csv_column_ip',
            'csv_remove_case',
            'csv_remove_company',
            'csv_remove_tag',
            'csv_default_systemstatus',
            'csv_default_analysisstatus',
            'csv_default_reason',
            'csv_default_domain',
            'csv_default_dnsname',
            'csv_default_systemtype',
            'csv_default_os',
            'csv_default_location',
            'csv_default_serviceprovider',
            'csv_default_case',
            'csv_default_company',
            'csv_default_tag',
        )

        labels = {
            'csv_skip_existing_system': 'Skip existing systems',
            'csv_column_system': 'Number of the column in the CSV file that contains the system name',
            'csv_headline': 'CSV file contains a headline row',
            'csv_choice_ip': 'CSV file contains IP addresses',
            'csv_remove_ip': 'Remove / overwrite existing IP addresses for already existing systems',
            'csv_column_ip': 'Number of the column in the CSV file that contains the IP addresses',
            'csv_remove_case': 'Remove / overwrite existing cases for already existing systems',
            'csv_remove_company': 'Remove / overwrite existing companies for already existing systems',
            'csv_remove_tag': 'Remove / overwrite existing tags for already existing systems',
            'csv_default_systemstatus': 'Set systemstatus (*)',
            'csv_default_analysisstatus': 'Set analysisstatus (*)',
            'csv_default_reason': 'Set reason',
            'csv_default_domain': 'Set domain',
            'csv_default_dnsname': 'Set DNS name',
            'csv_default_systemtype': 'Set systemtype',
            'csv_default_os': 'Set OS',
            'csv_default_location': 'Set location',
            'csv_default_serviceprovider': 'Set serviceprovider',
            'csv_default_case': 'Set cases',
            'csv_default_company': 'Set companies',
            'csv_default_tag': 'Set tags',
        }

        widgets = {
            'csv_column_system': forms.NumberInput(
                attrs={
                    #'style': 'width:6ch',
                    'min': '1',
                    'max': '99',
                    'size': '3',
                },
            ),
            'csv_column_ip': forms.NumberInput(
                attrs={
                    #'style': 'width:6ch',
                    'min': '1',
                    'max': '99',
                    'size': '3',
                },
            ),
            'csv_default_systemstatus': forms.RadioSelect(),
            'csv_default_analysisstatus': forms.RadioSelect(),
            'csv_default_case': forms.CheckboxSelectMultiple(),
            'csv_default_company': forms.CheckboxSelectMultiple(),
            'csv_default_tag': forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        """ custom field validation """

        # get form data
        cleaned_data = super().clean()

        # get relevant values
        csv_column_system = self.cleaned_data['csv_column_system']
        csv_column_ip = self.cleaned_data['csv_column_ip']

        # compare column values
        if csv_column_system == csv_column_ip:
            raise forms.ValidationError('The columns for system and IP must not have the same values.')

        return cleaned_data

class SystemImporterFileCsvFormbasedConfigForm(forms.ModelForm):
    """ system importer CSV config form (form based only) """

    class Meta:

        # model
        model = SystemImporterFileCsvFormbasedConfigModel

        # this HTML forms are shown
        fields = (
            'csv_skip_existing_system',
            'csv_column_system',
            'csv_headline',
            'csv_choice_ip',
            'csv_remove_ip',
            'csv_column_ip',
            'csv_remove_case',
            'csv_remove_company',
            'csv_remove_tag',
        )

        labels = {
            'csv_skip_existing_system': 'Skip existing systems',
            'csv_column_system': 'Number of the column in the CSV file that contains the system name',
            'csv_headline': 'CSV file contains a headline row',
            'csv_choice_ip': 'CSV file contains IP addresses',
            'csv_remove_ip': 'Remove / overwrite existing IP addresses for already existing systems',
            'csv_column_ip': 'Number of the column in the CSV file that contains the IP addresses',
            'csv_remove_case': 'Remove / overwrite existing cases for already existing systems',
            'csv_remove_company': 'Remove / overwrite existing companies for already existing systems',
            'csv_remove_tag': 'Remove / overwrite existing tags for already existing systems',
        }

        widgets = {
            'csv_column_system': forms.NumberInput(
                attrs={
                    #'style': 'width:6ch',
                    'min': '1',
                    'max': '99',
                    'size': '3',
                },
            ),
            'csv_column_ip': forms.NumberInput(
                attrs={
                    #'style': 'width:6ch',
                    'min': '1',
                    'max': '99',
                    'size': '3',
                },
            ),
        }

    def clean(self):
        """ custom field validation """

        # get form data
        cleaned_data = super().clean()

        # get relevant values
        csv_column_system = self.cleaned_data['csv_column_system']
        csv_column_ip = self.cleaned_data['csv_column_ip']

        # compare column values
        if csv_column_system == csv_column_ip:
            raise forms.ValidationError('The columns for system and IP must not have the same values.')

        return cleaned_data
