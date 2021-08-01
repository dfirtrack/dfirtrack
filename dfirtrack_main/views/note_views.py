from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from dfirtrack_main.forms import NoteForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Note, Notestatus


class NoteList(LoginRequiredMixin, ListView):
    login_url = "/login"
    model = Note
    template_name = "dfirtrack_main/note/note_list.html"
    context_object_name = "note_list"

    def get_queryset(self):
        debug_logger(str(self.request.user), " NOTE_LIST_ENTERED")
        return Note.objects.order_by("note_title")


class NoteDetail(LoginRequiredMixin, DetailView):
    login_url = "/login"
    model = Note
    template_name = "dfirtrack_main/note/note_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Note = self.object
        Note.logger(str(self.request.user), " NOTE_DETAIL_ENTERED")
        return context


class NoteCreate(LoginRequiredMixin, CreateView):
    login_url = "/login"
    model = Note
    form_class = NoteForm
    template_name = "dfirtrack_main/note/note_generic_form.html"

    def get(self, request, *args, **kwargs):

        # get id of first status objects sorted by name
        notestatus = Notestatus.objects.order_by("notestatus_name")[0].notestatus_id

        # show empty form with default values for convenience and speed reasons
        form = self.form_class(
            initial={
                "notestatus": notestatus,
            }
        )
        debug_logger(str(request.user), " NOTE_ADD_ENTERED")
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Add",
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.note_created_by_user_id = request.user
            note.note_modified_by_user_id = request.user
            note.save()
            form.save_m2m()
            note.logger(str(request.user), " NOTE_ADD_EXECUTED")
            messages.success(request, "Note added")
            if "documentation" in request.GET:
                return redirect(
                    reverse("documentation_list") + f"#note_id_{note.note_id}"
                )
            else:
                return redirect(reverse("note_detail", args=(note.note_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Add",
                },
            )


class NoteUpdate(LoginRequiredMixin, UpdateView):
    login_url = "/login"
    model = Note
    form_class = NoteForm
    template_name = "dfirtrack_main/note/note_generic_form.html"

    def get(self, request, *args, **kwargs):
        note = self.get_object()
        form = self.form_class(instance=note)
        note.logger(str(request.user), " NOTE_EDIT_ENTERED")
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "title": "Edit",
                "note": note,
            },
        )

    def post(self, request, *args, **kwargs):
        note = self.get_object()
        form = self.form_class(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.Note_modified_by_user_id = request.user
            note.save()
            form.save_m2m()
            note.logger(str(request.user), " NOTE_EDIT_EXECUTED")
            messages.success(request, "Note edited")
            if "documentation" in request.GET:
                return redirect(
                    reverse("documentation_list") + f"#note_id_{note.note_id}"
                )
            else:
                return redirect(reverse("note_detail", args=(note.note_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "title": "Edit",
                    "note": note,
                },
            )
