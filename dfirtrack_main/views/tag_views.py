from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import TagForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Tag

class TagList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Tag
    template_name = 'dfirtrack_main/tag/tags_list.html'
    context_object_name = 'tag_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " TAG_ENTERED")
        return Tag.objects.order_by('tag_name')

class TagDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Tag
    template_name = 'dfirtrack_main/tag/tags_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.object
        tag.logger(str(self.request.user), " TAGDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def tags_add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.tag_modified_by_user_id = request.user
            tag.save()
            tag.logger(str(request.user), " TAG_ADD_EXECUTED")
            messages.success(request, 'Tag added')
            return redirect('/tags')
    else:
        form = TagForm()
        debug_logger(str(request.user), " TAG_ADD_ENTERED")
    return render(request, 'dfirtrack_main/tag/tags_add.html', {'form': form})

@login_required(login_url="/login")
def tags_delete(request, pk, template_name='dfirtrack_main/tag/tags_delete.html'):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.logger(str(request.user), " TAG_DELETE_EXECUTED")
        tag.delete()
        messages.success(request, 'Tag deleted')
        return redirect('/tags')
    return render(request, template_name, {'tag': tag})

@login_required(login_url="/login")
def tags_edit(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.tag_modified_by_user_id = request.user
            tag.save()
            tag.logger(str(request.user), " TAG_EDIT_EXECUTED")
            messages.success(request, 'Tag edited')
            return redirect('/tags')
    else:
        form = TagForm(instance=tag)
        tag.logger(str(request.user), " TAG_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/tag/tags_edit.html', {'form': form})
