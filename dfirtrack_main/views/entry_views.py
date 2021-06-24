from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from dfirtrack_main.forms import EntryForm, EntryFileImport, EntryFileImportColumns
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Entry
from django.contrib.auth.decorators import login_required
from django_q.tasks import async_task
import uuid
import csv


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
    template_name = 'dfirtrack_main/entry/entry_add.html'

    def get(self, request, *args, **kwargs):
        if 'system' in request.GET:
            system = request.GET['system']
            form = self.form_class(
                initial={'system': system,}
            )
        else:
            form = self.form_class()
        debug_logger(str(request.user), " ENTRY_ADD_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.entry_created_by_user_id = request.user
            entry.entry_modified_by_user_id = request.user
            entry.save()
            entry.logger(str(request.user), " ENTRY_ADD_EXECUTED")
            messages.success(request, 'Entry added')
            return redirect(reverse('system_detail', args=(entry.system.system_id,)))
        else:
            return render(request, self.template_name, {'form': form})

class EntryUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Entry
    form_class = EntryForm
    template_name = 'dfirtrack_main/entry/entry_edit.html'

    def get(self, request, *args, **kwargs):
        entry = self.get_object()
        form = self.form_class(instance=entry)
        entry.logger(str(request.user), " ENTRY_EDIT_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        entry = self.get_object()
        form = self.form_class(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.entry_modified_by_user_id = request.user
            entry.save()
            entry.logger(str(request.user), " ENTRY_EDIT_EXECUTED")
            messages.success(request, 'Entry edited')
            return redirect(reverse('system_detail', args=(entry.system.system_id,)))
        else:
            return render(request, self.template_name, {'form': form})

@login_required(login_url="/login")
def import_csv_step1(request):

    if request.method == "POST":
        form = EntryFileImport(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['entryfile']

            file_name = '/tmp/' + str(uuid.uuid4())
            with open(file_name, 'wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)
  
            with open(file_name, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                columns = next(spamreader)

            entry = form.save(commit=False)

            request.session['entry_csv_import'] = {
                'columns': columns,
                'system': entry.system.system_id,
                'case': entry.case.case_id if entry.case else None,
                'file_name': file_name
            }
           
            return redirect(reverse('entry_import_step2'))
        else:
            return render(request, 'dfirtrack_main/entry/entry_import_step1.html', {'form': form})
    else:
        form = EntryFileImport()
        return render(request, 'dfirtrack_main/entry/entry_import_step1.html', {'form': form})    


def import_csv_step2(request):
    
    if request.method == "POST":
        #TODO injection testen
        form = EntryFileImportColumns(
            request.session['entry_csv_import']['columns'], 
            request.POST
        )
        if form.is_valid():
            
            field_mapping = {
                'entry_time': int(form.cleaned_data['entry_time']),
                'entry_type': int(form.cleaned_data['entry_type']),
                'entry_content': int(form.cleaned_data['entry_content']),
            }

            async_task(
                "dfirtrack_main.importer.file.csv_entry_import.csv_entry_import_async",
                request.session['entry_csv_import']['system'],
                request.session['entry_csv_import']['file_name'],
                field_mapping,
                request.user,
                request.session['entry_csv_import']['case'],
            )

            messages.success(request, 'Entry timesketch importer started')
            
            return redirect(reverse('entry_list'))
        else:
            return render(request, 'dfirtrack_main/entry/entry_import_step2.html', {'form': form})
    else:
        form = EntryFileImportColumns(request.session['entry_csv_import']['columns'])
        return render(request, 'dfirtrack_main/entry/entry_import_step2.html', {'form': form})  