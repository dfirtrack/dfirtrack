import csv
import uuid

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django_q.tasks import async_task

from dfirtrack_main.forms import EntryFileImport, EntryFileImportFields, EntryForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Entry


class EntryList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Entry
    template_name = 'dfirtrack_main/entry/entry_list.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " ENTRY_LIST_ENTERED")
        return Entry.objects.order_by('entry_id')


class EntryDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Entry
    template_name = 'dfirtrack_main/entry/entry_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entry = self.object
        entry.logger(str(self.request.user), " ENTRY_DETAIL_ENTERED")
        return context


class EntryCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Entry
    form_class = EntryForm
    template_name = 'dfirtrack_main/generic_form.html'

    def get(self, request, *args, **kwargs):
        if 'system' in request.GET:
            system = request.GET['system']
            form = self.form_class(
                initial={
                    'system': system,
                }
            )
        else:
            form = self.form_class()
        debug_logger(str(request.user), " ENTRY_ADD_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Add',
                'object_type': 'entry',
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.entry_created_by_user_id = request.user
            entry.entry_modified_by_user_id = request.user
            entry.save()
            form.save_m2m()
            entry.logger(str(request.user), " ENTRY_ADD_EXECUTED")
            messages.success(request, 'Entry added')
            return redirect(reverse('system_detail', args=(entry.system.system_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Add',
                    'object_type': 'entry',
                },
            )


class EntryUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Entry
    form_class = EntryForm
    template_name = 'dfirtrack_main/generic_form.html'

    def get(self, request, *args, **kwargs):
        entry = self.get_object()
        form = self.form_class(instance=entry)
        entry.logger(str(request.user), " ENTRY_EDIT_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Edit',
                'object_type': 'entry',
            },
        )

    def post(self, request, *args, **kwargs):
        entry = self.get_object()
        form = self.form_class(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.entry_modified_by_user_id = request.user
            entry.save()
            form.save_m2m()
            entry.logger(str(request.user), " ENTRY_EDIT_EXECUTED")
            messages.success(request, 'Entry edited')
            return redirect(reverse('system_detail', args=(entry.system.system_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Edit',
                    'object_type': 'entry',
                },
            )


@login_required(login_url="/login")
def import_csv_step1(request):

    if request.method == "POST":
        # POST request
        form = EntryFileImport(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['entryfile']
            delimiter = request.POST['delimiter']
            quotechar = request.POST['quotechar']

            # write upload to random tmp file
            file_name = f'/tmp/{uuid.uuid4()}'
            with open(file_name, 'wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)

            # get first row of uploaded csv (fields)
            with open(file_name, newline='') as csvfile:
                spamreader = csv.reader(
                    csvfile, delimiter=delimiter, quotechar=quotechar
                )
                fields = next(spamreader)

            # save form for case and system info
            entry = form.save(commit=False)

            # add all values to session to access during step2
            request.session['entry_csv_import'] = {
                'fields': fields,
                'system': entry.system.system_id,
                'case': entry.case.case_id if entry.case else None,
                'file_name': file_name,
                'delimiter': delimiter,
                'quotechar': quotechar,
            }

            messages.success(request, 'Uploaded csv to DFIRTrack.')

            # goto step 2
            return redirect(reverse('entry_import_step2'))
        else:
            return render(
                request, 'dfirtrack_main/entry/entry_import_step1.html', {'form': form}
            )
    else:
        # GET request
        debug_logger(str(request.user), ' ENTRY_CSV_IMPORTER_STEP1_ENTERED')
        form = EntryFileImport()
        return render(
            request, 'dfirtrack_main/entry/entry_import_step1.html', {'form': form}
        )


@login_required(login_url="/login")
def import_csv_step2(request):
    # check if step1 was successful
    if 'entry_csv_import' not in request.session:
        return redirect(reverse('entry_import_step1'))

    # POST request
    if request.method == "POST":
        # get form with dynamic fields
        form = EntryFileImportFields(
            request.session['entry_csv_import']['fields'], request.POST
        )
        if form.is_valid():
            # get field mappings
            field_mapping = {
                'entry_time': int(form.cleaned_data['entry_time']),
                'entry_type': int(form.cleaned_data['entry_type']),
                'entry_content': int(form.cleaned_data['entry_content']),
                'entry_tag': int(form.cleaned_data['entry_tag']),
            }

            # run async task
            async_task(
                "dfirtrack_main.importer.file.csv_entry_import.csv_entry_import_async",
                request.session['entry_csv_import']['system'],
                request.session['entry_csv_import']['file_name'],
                field_mapping,
                request.user,
                request.session['entry_csv_import']['delimiter'],
                request.session['entry_csv_import']['quotechar'],
                request.session['entry_csv_import']['case'],
            )
            # delete session information
            del request.session['entry_csv_import']

            messages.success(request, 'Entry csv importer started')

            return redirect(reverse('entry_list'))
        else:
            return render(
                request, 'dfirtrack_main/entry/entry_import_step2.html', {'form': form}
            )
    else:
        # GET request
        debug_logger(str(request.user), ' ENTRY_CSV_IMPORTER_STEP2_ENTERED')
        # prepare dynamic form with csv field information
        form = EntryFileImportFields(request.session['entry_csv_import']['fields'])
        return render(
            request, 'dfirtrack_main/entry/entry_import_step2.html', {'form': form}
        )
