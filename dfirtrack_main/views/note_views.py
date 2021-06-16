from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from dfirtrack_main.forms import NoteForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Note


class NoteList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Note
    template_name = 'dfirtrack_main/note/note_list.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " NOTE_LIST_ENTERED")
        return Note.objects.order_by('note_title')

class NoteDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Note
    template_name = 'dfirtrack_main/note/note_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Note = self.object
        Note.logger(str(self.request.user), " NOTE_DETAIL_ENTERED")
        return context

class NoteCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Note
    form_class = NoteForm
    template_name = 'dfirtrack_main/note/note_add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        debug_logger(str(request.user), " NOTE_ADD_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.note_created_by_user_id = request.user
            note.note_modified_by_user_id = request.user
            note.save()
            form.save_m2m()
            note.logger(str(request.user), " NOTE_ADD_EXECUTED")
            messages.success(request, 'Note added')
            return redirect(reverse('note_detail', args=(note.note_id,)))
        else:
            return render(request, self.template_name, {'form': form})

class NoteDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Note
    template_name = 'dfirtrack_main/note/note_delete.html'

    def get(self, request, *args, **kwargs):
        Note = self.get_object()
        Note.logger(str(request.user), " NOTE_DELETE_ENTERED")
        return render(request, self.template_name, {'Note': Note})

    def post(self, request, *args, **kwargs):
        Note = self.get_object()
        Note.logger(str(request.user), " NOTE_DELETE_EXECUTED")
        Note.delete()
        messages.success(request, 'Note deleted')
        return redirect(reverse('note_list'))

class NoteUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Note
    form_class = NoteForm
    template_name = 'dfirtrack_main/note/note_add.html'

    def get(self, request, *args, **kwargs):
        Note = self.get_object()
        form = self.form_class(instance=Note)
        Note.logger(str(request.user), " NOTE_EDIT_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        Note = self.get_object()
        form = self.form_class(request.POST, instance=Note)
        if form.is_valid():
            note = form.save(commit=False)
            note.Note_modified_by_user_id = request.user
            note.save()
            form.save_m2m()
            note.logger(str(request.user), " NOTE_EDIT_EXECUTED")
            messages.success(request, 'Note edited')
            return redirect(reverse('note_detail', args=(note.note_id,)))
        else:
            return render(request, self.template_name, {'form': form})
