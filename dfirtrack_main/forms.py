from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from martor.fields import MartorFormField

from dfirtrack_artifacts.models import Artifact
from dfirtrack_main.models import (
    Analysisstatus,
    Analystmemo,
    Case,
    Casepriority,
    Casestatus,
    Casetype,
    Company,
    Contact,
    Division,
    Dnsname,
    Domain,
    Domainuser,
    Entry,
    Headline,
    Location,
    Note,
    Notestatus,
    Os,
    Osarch,
    Osimportname,
    Reason,
    Recommendation,
    Reportitem,
    Serviceprovider,
    System,
    Systemstatus,
    Systemtype,
    Systemuser,
    Tag,
    Tagcolor,
    Task,
    Taskname,
    Taskpriority,
    Taskstatus,
)
from dfirtrack_main.widgets import TagWidget


class AdminStyleSelectorForm(forms.ModelForm):
    """inherit from this class if you want to use the ModelMultipleChoiceField with the FilteredSelectMultiple widget"""

    # needed for system selector
    class Media:
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)


class AnalystmemoForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    system = forms.ModelChoiceField(
        label=gettext_lazy('System (*)'),
        empty_label='Select system',
        queryset=System.objects.order_by('system_name'),
    )

    class Meta:

        # model
        model = Analystmemo

        # this HTML forms are shown
        fields = (
            'system',
            'analystmemo_note',
        )

        # non default form labeling
        labels = {
            'analystmemo_note': gettext_lazy('Analystmemo note (*)'),
        }

        # special form type or option
        widgets = {
            'analystmemo_note': forms.Textarea(
                attrs={'autofocus': 'autofocus', 'rows': 20}
            ),
        }


class CaseForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    casepriority = forms.ModelChoiceField(
        label=gettext_lazy('Casepriority (*)'),
        queryset=Casepriority.objects.order_by('casepriority_name'),
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    casestatus = forms.ModelChoiceField(
        label=gettext_lazy('Casestatus (*)'),
        queryset=Casestatus.objects.order_by('casestatus_name'),
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    casetype = forms.ModelChoiceField(
        label=gettext_lazy('Casetype'),
        queryset=Casetype.objects.order_by('casetype_name'),
        empty_label='Select casetype (optional)',
        required=False,
    )

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    class Meta:

        # model
        model = Case

        # this HTML forms are shown
        fields = (
            'case_id_external',
            'case_name',
            'case_is_incident',
            'case_note_analysisresult',
            'case_note_external',
            'case_note_internal',
            'casepriority',
            'casestatus',
            'casetype',
            'tag',
        )

        # non default form labeling
        labels = {
            'case_id_external': gettext_lazy('Case external ID'),
            'case_name': gettext_lazy('Case name (*)'),
            'case_is_incident': gettext_lazy('Is incident'),
            'case_note_analysisresult': gettext_lazy('Analysis result'),
            'case_note_external': gettext_lazy('External note'),
            'case_note_internal': gettext_lazy('Internal note'),
        }

        # special form type or option
        widgets = {
            'case_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class CaseCreatorForm(forms.Form):
    """case creator form"""

    # show all existing case objects as multiple choice field
    case = forms.ModelMultipleChoiceField(
        queryset=Case.objects.order_by('case_name'),
        widget=forms.CheckboxSelectMultiple(),
        label='Cases (*)',
        required=True,
    )

    # show all existing system objects as multiple choice field
    system = forms.ModelMultipleChoiceField(
        queryset=System.objects.order_by('system_name'),
        widget=forms.CheckboxSelectMultiple(),
        label='Systems (*)',
        required=True,
    )


class CasetypeForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Casetype

        # this HTML forms are shown
        fields = [
            'casetype_name',
            'casetype_note',
        ]

        # non default form labeling
        labels = {
            'casetype_name': gettext_lazy('Casetype name (*)'),
        }

        # special form type or option
        widgets = {
            'casetype_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class CompanyForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    division = forms.ModelChoiceField(
        label=gettext_lazy('Division'),
        empty_label='Select division (optional)',
        queryset=Division.objects.order_by('division_name'),
        required=False,
    )

    class Meta:

        # model
        model = Company

        # this HTML forms are shown
        fields = (
            'company_name',
            'division',
            'company_note',
        )

        # non default form labeling
        labels = {
            'company_name': gettext_lazy('Company name (*)'),
        }

        # special form type or option
        widgets = {
            'company_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class ContactForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Contact

        # this HTML forms are shown
        fields = (
            'contact_name',
            'contact_phone',
            'contact_email',
            'contact_note',
        )

        # non default form labeling
        labels = {
            'contact_name': gettext_lazy('Contact name (*)'),
            'contact_email': gettext_lazy('Contact email (*)'),
        }

        # special form type or option
        widgets = {
            'contact_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class DivisionForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Division

        # this HTML forms are shown
        fields = (
            'division_name',
            'division_note',
        )

        # non default form labeling
        labels = {
            'division_name': gettext_lazy('Division name (*)'),
        }

        # special form type or option
        widgets = {
            'division_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class DnsnameForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    domain = forms.ModelChoiceField(
        label=gettext_lazy('Domain'),
        empty_label='Select domain (optional)',
        queryset=Domain.objects.order_by('domain_name'),
        required=False,
    )

    class Meta:

        # model
        model = Dnsname

        # this HTML forms are shown
        fields = (
            'domain',
            'dnsname_name',
            'dnsname_note',
        )

        # non default form labeling
        labels = {
            'dnsname_name': gettext_lazy('DNS name (*)'),
            'dnsname_note': gettext_lazy('Note'),
        }

        # special form type or option
        widgets = {
            'dnsname_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class DomainForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Domain

        # this HTML forms are shown
        fields = (
            'domain_name',
            'domain_note',
        )

        # non default form labeling
        labels = {
            'domain_name': gettext_lazy('Domain name (*)'),
        }

        # special form type or option
        widgets = {
            'domain_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class DomainuserForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    domain = forms.ModelChoiceField(
        label=gettext_lazy('Domain (*)'),
        empty_label='Select domain',
        queryset=Domain.objects.order_by('domain_name'),
    )

    # reorder field choices
    system_was_logged_on = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Systems where this domainuser was logged on'),
        queryset=System.objects.order_by('system_name'),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:

        # model
        model = Domainuser

        # this HTML forms are shown
        fields = (
            'domainuser_name',
            'domainuser_is_domainadmin',
            'domain',
            'system_was_logged_on',
        )

        # non default form labeling
        labels = {
            'domainuser_name': gettext_lazy('Domainuser name (*)'),
        }

        # special form type or option
        widgets = {
            'domainuser_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class EntryForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    case = forms.ModelChoiceField(
        label=gettext_lazy('Case'),
        empty_label='Select case (optional)',
        queryset=Case.objects.order_by('case_name'),
        required=False,
    )

    # reorder field choices
    system = forms.ModelChoiceField(
        label=gettext_lazy('System (*)'),
        empty_label='Select system',
        queryset=System.objects.order_by('system_name'),
    )

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    class Meta:

        # model
        model = Entry

        # this HTML forms are shown
        fields = (
            'entry_time',
            'system',
            'entry_sha1',
            'entry_type',
            'entry_content',
            'entry_note',
            'case',
            'tag',
        )

        # non default form labeling
        labels = {
            'entry_time': gettext_lazy(
                'Entry time (for sorting) (YYYY-MM-DD HH:MM:SS) (*)'
            ),
        }

        # special form type or option
        widgets = {
            'entry_time': forms.DateTimeInput(attrs={'autofocus': 'autofocus'}),
            'entry_sha1': forms.TextInput(),
            'entry_type': forms.TextInput(),
            'entry_content': forms.Textarea(attrs={'rows': 3}),
            'entry_note': forms.Textarea(attrs={'rows': 10}),
        }


class EntryFileImport(forms.ModelForm):
    """file import form"""

    # reorder field choices
    system = forms.ModelChoiceField(
        label='System (*)',
        empty_label='Select system',
        queryset=System.objects.order_by('system_name'),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    # reorder field choice
    case = forms.ModelChoiceField(
        label='Case',
        empty_label='Select case (optional)',
        queryset=Case.objects.order_by('case_name'),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    # file upload field (variable is used in request object)
    entryfile = forms.FileField(
        label='CSV file (*)', widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:

        # model
        model = Entry
        fields = ('system', 'case')


class EntryFileImportFields(forms.Form):
    """entry csv import field assignment"""

    # placeholder, choices will be generated
    INITIAL_CHOICES = []

    # entry_time mapping
    entry_time = forms.ChoiceField(
        label='Datetime field',
        choices=INITIAL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    # entry type mapping
    entry_type = forms.ChoiceField(
        choices=INITIAL_CHOICES, widget=forms.Select(attrs={'class': 'form-select'})
    )

    # entry content mapping
    entry_content = forms.ChoiceField(
        choices=INITIAL_CHOICES, widget=forms.Select(attrs={'class': 'form-select'})
    )

    # entry tag mapping
    entry_tag = forms.ChoiceField(
        choices=INITIAL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
    )

    def clean(self):

        if (
            'entry_time' in self.cleaned_data
            and self.cleaned_data['entry_time'] == '-1'
        ):
            raise ValidationError('Please select a datetime value.')
        if (
            'entry_type' in self.cleaned_data
            and self.cleaned_data['entry_type'] == '-1'
        ):
            raise ValidationError('Please select an entry type value.')
        if (
            'entry_content' in self.cleaned_data
            and self.cleaned_data['entry_content'] == '-1'
        ):
            raise ValidationError('Please select an entry content value.')

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices.insert(0, '--')
        index = list(range(-1, len(choices)))
        form_choices = sorted(set(zip(index, choices)))

        # set select choices dynamically, based on uploaded csv file
        self.fields['entry_time'].choices = form_choices
        self.fields['entry_type'].choices = form_choices
        self.fields['entry_content'].choices = form_choices
        self.fields['entry_tag'].choices = form_choices


class HeadlineForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Headline

        # this HTML forms are shown
        fields = ('headline_name',)

        # non default form labeling
        labels = {
            'headline_name': gettext_lazy('Headline (*)'),
        }

        # special form type or option
        widgets = {
            'headline_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class LocationForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Location

        # this HTML forms are shown
        fields = (
            'location_name',
            'location_note',
        )

        # non default form labeling
        labels = {
            'location_name': gettext_lazy('Location name (*)'),
        }

        # special form type or option
        widgets = {
            'location_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class NoteForm(forms.ModelForm):
    """default model form"""

    # make hidden version field to make custom field validation work
    note_version = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    # make hidden id field to make custom field validation work
    note_id = forms.CharField(
        widget=forms.HiddenInput,
        required=False,
    )

    # markdown field
    note_content = MartorFormField(
        label=gettext_lazy('Note (*)'),
    )

    # reorder field choices
    case = forms.ModelChoiceField(
        label=gettext_lazy('Corresponding case'),
        queryset=Case.objects.order_by('case_name'),
        required=False,
        empty_label='Select case (optional)',
    )

    # reorder field choices
    notestatus = forms.ModelChoiceField(
        queryset=Notestatus.objects.order_by('notestatus_name'),
        label='Notestatus (*)',
        required=True,
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    def clean_note_version(self):
        """custom field validation to prevent accidental overwriting between analysts"""

        note_version = self.cleaned_data['note_version']
        if note_version != '':
            note_id = self.initial['note_id']
            current_version = Note.objects.get(note_id=note_id)
            if int(note_version) + 1 <= current_version.note_version:
                raise ValidationError('There is a newer version of this note.')
        return note_version

    class Meta:

        # model
        model = Note

        # this HTML forms are shown
        fields = (
            'note_id',
            'note_title',
            'note_content',
            'tag',
            'case',
            'note_version',
            'notestatus',
        )

        # non default form labeling
        labels = {
            'note_title': gettext_lazy('Note title (*)'),
        }

        # special form type or option
        widgets = {
            'note_title': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class OsForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Os

        # this HTML forms are shown
        fields = ('os_name',)

        # non default form labeling
        labels = {
            'os_name': gettext_lazy('Os name (*)'),
        }

        # special form type or option
        widgets = {
            'os_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class OsimportnameForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    os = forms.ModelChoiceField(
        label=gettext_lazy('Operating system (*)'),
        empty_label='Select OS',
        queryset=Os.objects.order_by('os_name'),
    )

    class Meta:

        # model
        model = Osimportname

        # this HTML forms are shown
        fields = (
            'osimportname_name',
            'os',
            'osimportname_importer',
        )

        # non default form labeling
        labels = {
            'osimportname_name': gettext_lazy('Importname (*)'),
            'osimportname_importer': gettext_lazy('Importer (*)'),
        }

        # special form type or option
        widgets = {
            'osimportname_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class ReasonForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Reason

        # this HTML forms are shown
        fields = (
            'reason_name',
            'reason_note',
        )

        # non default form labeling
        labels = {
            'reason_name': gettext_lazy('Reason name (*)'),
        }

        # special form type or option
        widgets = {
            'reason_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class RecommendationForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Recommendation

        # this HTML forms are shown
        fields = (
            'recommendation_name',
            'recommendation_note',
        )

        # non default form labeling
        labels = {
            'recommendation_name': gettext_lazy('Recommendation name (*)'),
        }

        # special form type or option
        widgets = {
            'recommendation_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class ReportitemForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    case = forms.ModelChoiceField(
        label=gettext_lazy('Corresponding case'),
        queryset=Case.objects.order_by('case_name'),
        required=False,
        empty_label='Select case (optional)',
    )

    # reorder field choices
    headline = forms.ModelChoiceField(
        label=gettext_lazy('Headline (*)'),
        empty_label='Select headline',
        queryset=Headline.objects.order_by('headline_name'),
    )

    reportitem_note = MartorFormField(
        label=gettext_lazy('Note (*)'),
    )

    # reorder field choices
    notestatus = forms.ModelChoiceField(
        queryset=Notestatus.objects.order_by('notestatus_name'),
        label='Notestatus (*)',
        required=True,
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    system = forms.ModelChoiceField(
        label=gettext_lazy('System (*)'),
        empty_label='Select system',
        queryset=System.objects.order_by('system_name'),
    )

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    class Meta:

        # model
        model = Reportitem

        # this HTML forms are shown
        fields = (
            'case',
            'headline',
            'notestatus',
            'system',
            'tag',
            'reportitem_subheadline',
            'reportitem_note',
        )

        # non default form labeling
        labels = {
            'reportitem_subheadline': gettext_lazy('Subheadline'),
        }

        # special form type or option
        widgets = {
            'reportitem_note': forms.Textarea(
                attrs={
                    'autofocus': 'autofocus',
                    'rows': 20,
                    'style': 'font-family: monospace',
                }
            ),
        }


class ServiceproviderForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Serviceprovider

        # this HTML forms are shown
        fields = (
            'serviceprovider_name',
            'serviceprovider_note',
        )

        # non default form labeling
        labels = {
            'serviceprovider_name': gettext_lazy('Serviceprovider name (*)'),
        }

        # special form type or option
        widgets = {
            'serviceprovider_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class SystemBaseForm(forms.ModelForm):
    """form base class with shared form fields for system"""

    # reorder field choices
    analysisstatus = forms.ModelChoiceField(
        queryset=Analysisstatus.objects.order_by('analysisstatus_name'),
        label='Analysisstatus',
        required=False,
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    company = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Companies'),
        queryset=Company.objects.order_by('company_name'),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    # reorder field choices
    systemstatus = forms.ModelChoiceField(
        queryset=Systemstatus.objects.order_by('systemstatus_name'),
        label='Systemstatus (*)',
        required=True,
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    class Meta:

        # model
        model = System

        # this HTML forms are shown
        fields = (
            'analysisstatus',
            'company',
            'systemstatus',
            'tag',
        )


class SystemExtendedBaseForm(SystemBaseForm):
    """extended form base class with shared form fields for system, inherits from system base form"""

    # reorder field choices
    case = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Cases'),
        queryset=Case.objects.order_by('case_name'),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    # reorder field choices
    contact = forms.ModelChoiceField(
        label=gettext_lazy('Contact'),
        queryset=Contact.objects.order_by('contact_name'),
        required=False,
        empty_label='Select contact (optional)',
    )

    # reorder field choices
    dnsname = forms.ModelChoiceField(
        label=gettext_lazy('DNS name'),
        queryset=Dnsname.objects.order_by('dnsname_name'),
        empty_label='Select DNS name (optional)',
        required=False,
    )

    # reorder field choices
    domain = forms.ModelChoiceField(
        label=gettext_lazy('Domain'),
        queryset=Domain.objects.order_by('domain_name'),
        empty_label='Select domain (optional)',
        required=False,
    )

    # reorder field choices
    location = forms.ModelChoiceField(
        label=gettext_lazy('Location'),
        queryset=Location.objects.order_by('location_name'),
        required=False,
        empty_label='Select location (optional)',
    )

    # reorder field choices
    os = forms.ModelChoiceField(
        label=gettext_lazy('Operating system'),
        queryset=Os.objects.order_by('os_name'),
        empty_label='Select OS (optional)',
        required=False,
    )

    # reorder field choices
    osarch = forms.ModelChoiceField(
        label=gettext_lazy('OS architecture'),
        queryset=Osarch.objects.order_by('osarch_name'),
        empty_label='Select OS architecture (optional)',
        required=False,
    )

    # reorder field choices
    reason = forms.ModelChoiceField(
        label=gettext_lazy('Reason for investigation'),
        queryset=Reason.objects.order_by('reason_name'),
        empty_label='Select reason (optional)',
        required=False,
    )

    # reorder field choices
    serviceprovider = forms.ModelChoiceField(
        label=gettext_lazy('Serviceprovider'),
        queryset=Serviceprovider.objects.order_by('serviceprovider_name'),
        required=False,
        empty_label='Select serviceprovider (optional)',
    )

    # reorder field choices
    systemtype = forms.ModelChoiceField(
        label=gettext_lazy('Systemtype'),
        queryset=Systemtype.objects.order_by('systemtype_name'),
        empty_label='Select systemtype (optional)',
        required=False,
    )

    class Meta(SystemBaseForm.Meta):

        # this HTML forms are shown
        fields = SystemBaseForm.Meta.fields + (
            'case',
            'contact',
            'dnsname',
            'domain',
            'location',
            'os',
            'osarch',
            'reason',
            'serviceprovider',
            'systemtype',
        )


class SystemForm(SystemExtendedBaseForm):
    """this form does not allow editing of system_name, inherits from system extended base form"""

    # reorder field choices
    host_system = forms.ModelChoiceField(
        label=gettext_lazy('Host system (hypervisor)'),
        queryset=System.objects.order_by('system_name'),
        empty_label='Select host system (optional)',
        required=False,
    )

    # large text area for line separated iplist
    iplist = forms.CharField(
        label=gettext_lazy('IP addresses'),
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'placeholder': 'One IP address per line',
            },
        ),
        required=False,
    )

    # reorder field choices
    recommendation = forms.ModelChoiceField(
        label=gettext_lazy('Recommendation'),
        queryset=Recommendation.objects.order_by('recommendation_name'),
        empty_label='Select recommendation (optional)',
        required=False,
    )

    class Meta(SystemExtendedBaseForm.Meta):

        # this HTML forms are shown
        fields = SystemExtendedBaseForm.Meta.fields + (
            'host_system',
            'recommendation',
            'system_deprecated_time',
            'system_export_markdown',
            'system_export_spreadsheet',
            'system_install_time',
            'system_is_vm',
            'system_lastbooted_time',
        )

        # non default form labeling
        labels = {
            'system_deprecated_time': gettext_lazy(
                'System is deprecated since (YYYY-MM-DD HH:MM:SS)'
            ),
            'system_export_markdown': gettext_lazy('Export system to markdown'),
            'system_export_spreadsheet': gettext_lazy('Export system to spreadsheet'),
            'system_install_time': gettext_lazy(
                'Installation time (YYYY-MM-DD HH:MM:SS)'
            ),
            'system_is_vm': gettext_lazy('System is a VM'),
            'system_lastbooted_time': gettext_lazy('Last booted (YYYY-MM-DD HH:MM:SS)'),
        }

        # special form type or option
        widgets = {
            'host_system': forms.Select(),
            'system_deprecated_time': forms.DateTimeInput(),
            'system_install_time': forms.DateTimeInput(),
            'system_is_vm': forms.NullBooleanSelect(),
            'system_lastbooted_time': forms.DateTimeInput(),
        }


class SystemNameForm(SystemForm):
    """this form allows editing of system_name, inherits from system form"""

    class Meta(SystemForm.Meta):

        # add system_name to shown HTML forms
        fields = SystemForm.Meta.fields + ('system_name',)

        # non default form labeling for system_name
        SystemForm.Meta.labels['system_name'] = gettext_lazy('System name (*)')

        # special form type or option for system_name
        SystemForm.Meta.widgets['system_name'] = forms.TextInput(
            attrs={
                'autofocus': 'autofocus',
                'placeholder': 'Enter system name / hostname here',
            }
        )


class SystemCreatorForm(SystemExtendedBaseForm):
    """system creator form, inherits from system extended base form"""

    # large text area for line separated systemlist
    systemlist = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 20,
                'placeholder': 'One systemname per line',
                'autofocus': 'autofocus',
            },
        ),
        label='System list (*)',
    )


class SystemModificatorForm(AdminStyleSelectorForm, SystemBaseForm):
    """system modificator form, inherits from system base form"""

    """ non-model fields referencing models """

    # no model field comes into question, because optional choice in combination with delete checkbox
    contact = forms.ModelChoiceField(
        label=gettext_lazy('Contact'),
        queryset=Contact.objects.order_by('contact_name'),
        required=False,
        empty_label='Select contact (optional)',
    )

    # no model field comes into question, because optional choice in combination with delete checkbox
    location = forms.ModelChoiceField(
        label=gettext_lazy('Location'),
        queryset=Location.objects.order_by('location_name'),
        required=False,
        empty_label='Select location (optional)',
    )

    # no model field comes into question, because optional choice in combination with delete checkbox
    serviceprovider = forms.ModelChoiceField(
        label=gettext_lazy('Serviceprovider'),
        queryset=Serviceprovider.objects.order_by('serviceprovider_name'),
        required=False,
        empty_label='Select serviceprovider (optional)',
    )

    """ m2m related choices """

    # prepare m2m choices
    M2M_CHOICES = (
        ('keep_not_add', 'Do not change and keep existing'),
        ('keep_and_add', 'Keep existing and add new items'),
        ('remove_and_add', 'Delete existing and add new items'),
    )

    # add checkbox
    company_delete = forms.ChoiceField(
        label=gettext_lazy('How to deal with existing companies'),
        widget=forms.RadioSelect(),
        choices=M2M_CHOICES,
    )

    # add checkbox
    tag_delete = forms.ChoiceField(
        label=gettext_lazy('How to deal with existing tags'),
        widget=forms.RadioSelect(),
        choices=M2M_CHOICES,
    )

    """ fk related choices """

    # prepare fk choices
    FK_CHOICES = (
        ('keep_existing', 'Do not change and keep existing'),
        ('switch_new', 'Switch to selected item or none'),
    )

    # add checkbox
    contact_delete = forms.ChoiceField(
        label=gettext_lazy('How to deal with contacts'),
        widget=forms.RadioSelect(),
        choices=FK_CHOICES,
    )

    # add checkbox
    location_delete = forms.ChoiceField(
        label=gettext_lazy('How to deal with locations'),
        widget=forms.RadioSelect(),
        choices=FK_CHOICES,
    )

    # add checkbox
    serviceprovider_delete = forms.ChoiceField(
        label=gettext_lazy('How to deal with serviceproviders'),
        widget=forms.RadioSelect(),
        choices=FK_CHOICES,
    )

    """ admin UI style related functions """

    def __init__(self, *args, **kwargs):
        self.use_system_charfield = kwargs.pop('use_system_charfield', False)
        super().__init__(*args, **kwargs)
        # if use_system_charfield is set, we replace the ModelMultipleChoiceField with the (old) CharField for system selection
        if self.use_system_charfield:
            self.fields['systemlist'] = forms.CharField(
                widget=forms.Textarea(
                    attrs={
                        'rows': 20,
                        'placeholder': 'One systemname per line',
                        'autofocus': 'autofocus',
                    },
                ),
                label='System list (*)',
            )

    # TODO: [code] required flag for ModelMultipleChoiceField does not seem to work
    # admin UI style system chooser
    systemlist = forms.ModelMultipleChoiceField(
        queryset=System.objects.order_by('system_name'),
        widget=FilteredSelectMultiple('Systems', is_stacked=False),
        required=True,
        label='System list (*)',
    )


class SystemtypeForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Systemtype

        # this HTML forms are shown
        fields = ('systemtype_name',)

        # non default form labeling
        labels = {
            'systemtype_name': gettext_lazy('Systemtype name (*)'),
        }

        # special form type or option
        widgets = {
            'systemtype_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class SystemuserForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    system = forms.ModelChoiceField(
        label=gettext_lazy('System (*)'),
        empty_label='Select system',
        queryset=System.objects.order_by('system_name'),
    )

    class Meta:

        # model
        model = Systemuser

        # this HTML forms are shown
        fields = (
            'systemuser_name',
            'systemuser_lastlogon_time',
            'systemuser_is_systemadmin',
            'system',
        )

        # non default form labeling
        labels = {
            'systemuser_name': gettext_lazy('Systemuser name (*)'),
            'systemuser_lastlogon_time': gettext_lazy(
                'Last logon time (YYYY-MM-DD HH:MM:SS)'
            ),
        }

        # special form type or option
        widgets = {
            'systemuser_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class TagForm(forms.ModelForm):
    """default model form"""

    # reorder field choices
    tagcolor = forms.ModelChoiceField(
        label=gettext_lazy('Tag color (*)'),
        empty_label='Select tag color',
        queryset=Tagcolor.objects.order_by('tagcolor_name'),
    )

    class Meta:

        # model
        model = Tag

        # this HTML forms are shown
        fields = (
            'tag_name',
            'tagcolor',
            'tag_note',
        )

        # non default form labeling
        labels = {
            'tag_name': gettext_lazy('Tag name (*)'),
            'tag_note': gettext_lazy('Tag note'),
        }

        # special form type or option
        widgets = {
            'tag_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }


class TagCreatorForm(forms.Form):
    """tag creator form"""

    # show all existing tag objects as tag widget
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags (*)'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=True,
    )

    # show all existing system objects as multiple choice field
    system = forms.ModelMultipleChoiceField(
        queryset=System.objects.order_by('system_name'),
        widget=forms.CheckboxSelectMultiple(),
        label='Systems (*)',
        required=True,
    )


class TaskBaseForm(forms.ModelForm):
    """form base class with shared form fields for task"""

    # reorder field choices
    tag = forms.ModelMultipleChoiceField(
        label=gettext_lazy('Tags'),
        widget=TagWidget,
        queryset=Tag.objects.order_by('tag_name'),
        required=False,
    )

    # reorder field choices
    task_assigned_to_user_id = forms.ModelChoiceField(
        label=gettext_lazy('Assigned to user'),
        queryset=User.objects.order_by('username'),
        required=False,
        empty_label='Select user (optional)',
    )

    # reorder field choices
    taskpriority = forms.ModelChoiceField(
        queryset=Taskpriority.objects.order_by('taskpriority_name'),
        label='Taskpriority (*)',
        required=True,
        widget=forms.RadioSelect(),
    )

    # reorder field choices
    taskstatus = forms.ModelChoiceField(
        queryset=Taskstatus.objects.order_by('taskstatus_name'),
        label='Taskstatus (*)',
        required=True,
        widget=forms.RadioSelect(),
    )

    class Meta:

        # model
        model = Task

        # this HTML forms are shown
        fields = (
            'tag',
            'task_assigned_to_user_id',
            'task_note',
            'taskpriority',
            'taskstatus',
        )

        # special form type or option
        widgets = {
            'task_note': forms.Textarea(attrs={'rows': 10}),
        }


class TaskForm(TaskBaseForm):
    """default model form, inherits from task base form"""

    # reorder field choices
    artifact = forms.ModelChoiceField(
        label=gettext_lazy('Corresponding artifact'),
        queryset=Artifact.objects.order_by('artifact_id'),
        required=False,
        empty_label='Select artifact (optional)',
    )

    # reorder field choices
    case = forms.ModelChoiceField(
        label=gettext_lazy('Corresponding case'),
        queryset=Case.objects.order_by('case_name'),
        required=False,
        empty_label='Select case (optional)',
    )

    # reorder field choices
    parent_task = forms.ModelChoiceField(
        label=gettext_lazy('Parent task'),
        queryset=Task.objects.order_by('task_id'),
        required=False,
        empty_label='Select parent task (optional)',
    )

    # reorder field choices
    system = forms.ModelChoiceField(
        label=gettext_lazy('Corresponding system'),
        queryset=System.objects.order_by('system_name'),
        required=False,
        empty_label='Select system (optional)',
    )

    # reorder field choices
    taskname = forms.ModelChoiceField(
        label=gettext_lazy('Taskname (*)'),
        empty_label='Select taskname',
        queryset=Taskname.objects.order_by('taskname_name'),
    )

    class Meta(TaskBaseForm.Meta):

        # this HTML forms are shown
        fields = TaskBaseForm.Meta.fields + (
            'parent_task',
            'artifact',
            'case',
            'system',
            'task_due_time',
            'task_scheduled_time',
            'taskname',
        )

        # non default form labeling
        labels = {
            'task_due_time': gettext_lazy('Due (YYYY-MM-DD HH:MM:SS)'),
            'task_scheduled_time': gettext_lazy('Scheduled (YYYY-MM-DD HH:MM:SS)'),
        }

        # special form type or option
        new_widgets = {
            'task_due_time': forms.DateTimeInput(),
            'task_scheduled_time': forms.DateTimeInput(),
        }
        TaskBaseForm.Meta.widgets.update(new_widgets)


class TaskCreatorForm(AdminStyleSelectorForm, TaskBaseForm):
    """task creator form, inherits from task base form"""

    # admin UI style system chooser
    system = forms.ModelMultipleChoiceField(
        queryset=System.objects.order_by('system_name'),
        widget=FilteredSelectMultiple('Systems', is_stacked=False),
        label='Corresponding systems (*)',
        required=True,
    )

    # show all existing taskname objects as multiple choice field
    taskname = forms.ModelMultipleChoiceField(
        queryset=Taskname.objects.order_by('taskname_name'),
        widget=forms.CheckboxSelectMultiple(),
        label='Tasknames (*)',
        required=True,
    )


class TasknameForm(forms.ModelForm):
    """default model form"""

    class Meta:

        # model
        model = Taskname

        # this HTML forms are shown
        fields = ('taskname_name',)

        # non default form labeling
        labels = {
            'taskname_name': gettext_lazy('Taskname (*)'),
        }

        # special form type or option
        widgets = {
            'taskname_name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
        }
