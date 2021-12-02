from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from dfirtrack_main.forms import TagForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Tag


class TagList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Tag
    template_name = 'dfirtrack_main/tag/tag_list.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " TAG_LIST_ENTERED")
        return Tag.objects.order_by('tag_name')


class TagDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Tag
    template_name = 'dfirtrack_main/tag/tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.object
        tag.logger(str(self.request.user), " TAG_DETAIL_ENTERED")
        return context


class TagCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Tag
    form_class = TagForm
    template_name = 'dfirtrack_main/generic_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        debug_logger(str(request.user), " TAG_ADD_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Add',
                'object_type': 'tag',
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.tag_modified_by_user_id = request.user
            tag.save()
            tag.logger(str(request.user), " TAG_ADD_EXECUTED")
            messages.success(request, 'Tag added')
            return redirect(reverse('tag_detail', args=(tag.tag_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Add',
                    'object_type': 'tag',
                },
            )


class TagDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Tag
    template_name = 'dfirtrack_main/tag/tag_delete.html'

    def get(self, request, *args, **kwargs):
        tag = self.get_object()
        tag.logger(str(request.user), " TAG_DELETE_ENTERED")
        return render(request, self.template_name, {'tag': tag})

    def post(self, request, *args, **kwargs):
        tag = self.get_object()
        tag.logger(str(request.user), " TAG_DELETE_EXECUTED")
        tag.delete()
        messages.success(request, 'Tag deleted')
        return redirect(reverse('tag_list'))


class TagUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Tag
    form_class = TagForm
    template_name = 'dfirtrack_main/generic_form.html'

    def get(self, request, *args, **kwargs):
        tag = self.get_object()
        form = self.form_class(instance=tag)
        tag.logger(str(request.user), " TAG_EDIT_ENTERED")
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'title': 'Edit',
                'object_type': 'tag',
                'object_name': tag.tag_name,
            },
        )

    def post(self, request, *args, **kwargs):
        tag = self.get_object()
        form = self.form_class(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.tag_modified_by_user_id = request.user
            tag.save()
            tag.logger(str(request.user), " TAG_EDIT_EXECUTED")
            messages.success(request, 'Tag edited')
            return redirect(reverse('tag_detail', args=(tag.tag_id,)))
        else:
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'title': 'Edit',
                    'object_type': 'tag',
                    'object_name': tag.tag_name,
                },
            )


class TagSetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Tag

    def get(self, request, *args, **kwargs):
        tag = self.get_object()
        tag.tag_assigned_to_user_id = request.user
        tag.save()
        tag.logger(str(request.user), " TAG_SET_USER_EXECUTED")
        messages.success(request, 'Tag assigned to you')

        # redirect
        return redirect(reverse('tag_detail', args=(tag.tag_id,)))


class TagUnsetUser(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Tag

    def get(self, request, *args, **kwargs):
        tag = self.get_object()
        tag.tag_assigned_to_user_id = None
        tag.save()
        tag.logger(str(request.user), " TAG_UNSET_USER_EXECUTED")
        messages.warning(request, 'User assignment for tag deleted')

        # redirect
        return redirect(reverse('tag_detail', args=(tag.tag_id,)))
