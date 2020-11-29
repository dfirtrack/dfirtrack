from django import forms
from dfirtrack_config.models import ArtifactExporterSpreadsheetXlsConfigModel, MainConfigModel, SystemExporterMarkdownConfigModel, SystemExporterSpreadsheetCsvConfigModel, SystemExporterSpreadsheetXlsConfigModel, SystemImporterFileCsvConfigbasedConfigModel, SystemImporterFileCsvFormbasedConfigModel

class ArtifactExporterSpreadsheetXlsConfigForm(forms.ModelForm):
    """ artifact exporter spreadsheet xls config form """

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
            'artifactlist_xls_artifactpriority',
            'artifactlist_xls_artifacttype',
            'artifactlist_xls_artifact_source_path',
            'artifactlist_xls_artifact_storage_path',
            'artifactlist_xls_artifact_note_internal',
            'artifactlist_xls_artifact_note_external',
            'artifactlist_xls_artifact_note_analysisresult',
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
            'artifactlist_xls_artifactpriority': 'Export artifactpriority',
            'artifactlist_xls_artifacttype': 'Export artifacttype',
            'artifactlist_xls_artifact_source_path': 'Export source path',
            'artifactlist_xls_artifact_storage_path': 'Export storage path',
            'artifactlist_xls_artifact_note_internal': 'Export internal note',
            'artifactlist_xls_artifact_note_external': 'Export external note',
            'artifactlist_xls_artifact_note_analysisresult': 'Export analysis result',
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

class MainConfigForm(forms.ModelForm):
    """ main config form """

    class Meta:

        # model
        model = MainConfigModel

        # this HTML forms are shown
        fields = (
            'system_name_editable',
            'artifactstatus_open',
            'statushistory_entry_numbers',
        )

        labels = {
            'system_name_editable': 'Make system name editable',
            'artifactstatus_open': 'Artifactstatus to be considered open',
            'statushistory_entry_numbers': 'Show only this number of last statushistory entries',
        }

        widgets = {
            'artifactstatus_open': forms.CheckboxSelectMultiple(),
            'statushistory_entry_numbers': forms.NumberInput(
                attrs={
                    'min': '1',
                    'max': '99',
                    'size': '3',
                },
            ),
        }

class SystemExporterMarkdownConfigForm(forms.ModelForm):
    """ system exporter markdown config form """

    class Meta:

        # model
        model = SystemExporterMarkdownConfigModel

        # this HTML forms are shown
        fields = (
            'markdown_path',
            'markdown_sorting',
        )

        labels = {
            'markdown_path': 'Path for the markdown documentation export',
            'markdown_sorting': 'Choose sorting for system markdown export',
        }

        widgets = {
            'markdown_path': forms.TextInput(attrs={
                'size': '55',
                'style': 'font-family: monospace',
            }),
            'markdown_sorting': forms.RadioSelect(),
        }

class SystemExporterSpreadsheetCsvConfigForm(forms.ModelForm):
    """ system exporter spreadsheet CSV config form """

    class Meta:

        # model
        model = SystemExporterSpreadsheetCsvConfigModel

        # this HTML forms are shown
        fields = (
            'spread_csv_system_id',
            'spread_csv_dnsname',
            'spread_csv_domain',
            'spread_csv_systemstatus',
            'spread_csv_analysisstatus',
            'spread_csv_reason',
            'spread_csv_recommendation',
            'spread_csv_systemtype',
            'spread_csv_ip',
            'spread_csv_os',
            'spread_csv_company',
            'spread_csv_location',
            'spread_csv_serviceprovider',
            'spread_csv_tag',
            'spread_csv_case',
            'spread_csv_system_create_time',
            'spread_csv_system_modify_time',
        )

        labels = {
            'spread_csv_system_id': 'Export system ID',
            'spread_csv_dnsname': 'Export DNS name',
            'spread_csv_domain': 'Export domain',
            'spread_csv_systemstatus': 'Export systemstatus',
            'spread_csv_analysisstatus': 'Export analysisstatus',
            'spread_csv_reason': 'Export reason',
            'spread_csv_recommendation': 'Export recommendation',
            'spread_csv_systemtype': 'Export systemtype',
            'spread_csv_ip': 'Export IP',
            'spread_csv_os': 'Export OS',
            'spread_csv_company': 'Export company',
            'spread_csv_location': 'Export location',
            'spread_csv_serviceprovider': 'Export serviceprovider',
            'spread_csv_tag': 'Export tag',
            'spread_csv_case': 'Export case',
            'spread_csv_system_create_time': 'Export system create time',
            'spread_csv_system_modify_time': 'Export system modify time',
        }

class SystemExporterSpreadsheetXlsConfigForm(forms.ModelForm):
    """ system exporter spreadsheet XLS config form """

    class Meta:

        # model
        model = SystemExporterSpreadsheetXlsConfigModel

        # this HTML forms are shown
        fields = (
            'spread_xls_system_id',
            'spread_xls_dnsname',
            'spread_xls_domain',
            'spread_xls_systemstatus',
            'spread_xls_analysisstatus',
            'spread_xls_reason',
            'spread_xls_recommendation',
            'spread_xls_systemtype',
            'spread_xls_ip',
            'spread_xls_os',
            'spread_xls_company',
            'spread_xls_location',
            'spread_xls_serviceprovider',
            'spread_xls_tag',
            'spread_xls_case',
            'spread_xls_system_create_time',
            'spread_xls_system_modify_time',
            'spread_xls_worksheet_systemstatus',
            'spread_xls_worksheet_analysisstatus',
            'spread_xls_worksheet_reason',
            'spread_xls_worksheet_recommendation',
            'spread_xls_worksheet_tag',
        )

        labels = {
            'spread_xls_system_id': 'Export system ID',
            'spread_xls_dnsname': 'Export DNS name',
            'spread_xls_domain': 'Export domain',
            'spread_xls_systemstatus': 'Export systemstatus',
            'spread_xls_analysisstatus': 'Export analysisstatus',
            'spread_xls_reason': 'Export reason',
            'spread_xls_recommendation': 'Export recommendation',
            'spread_xls_systemtype': 'Export systemtype',
            'spread_xls_ip': 'Export IP',
            'spread_xls_os': 'Export OS',
            'spread_xls_company': 'Export company',
            'spread_xls_location': 'Export location',
            'spread_xls_serviceprovider': 'Export serviceprovider',
            'spread_xls_tag': 'Export tag',
            'spread_xls_case': 'Export case',
            'spread_xls_system_create_time': 'Export system create time',
            'spread_xls_system_modify_time': 'Export system modify time',
            'spread_xls_worksheet_systemstatus': 'Export worksheet to explain systemstatus',
            'spread_xls_worksheet_analysisstatus': 'Export worksheet to explain analysisstatus',
            'spread_xls_worksheet_reason': 'Export worksheet to explain reason',
            'spread_xls_worksheet_recommendation': 'Export worksheet to explain recommendation',
            'spread_xls_worksheet_tag': 'Export worksheet to explain tag',
        }

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
