from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import HeadlineForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Headline

class HeadlineList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Headline
    template_name = 'dfirtrack_main/headline/headlines_list.html'
    context_object_name = 'headline_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " HEADLINE_ENTERED")
        return Headline.objects.order_by('headline_name')

class HeadlineDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Headline
    template_name = 'dfirtrack_main/headline/headlines_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headline = self.object
        headline.logger(str(self.request.user), " HEADLINEDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def headlines_add(request):
    if request.method == 'POST':
        form = HeadlineForm(request.POST)
        if form.is_valid():
            headline = form.save(commit=False)
            headline.save()
            headline.logger(str(request.user), " HEADLINE_ADD_EXECUTED")
            messages.success(request, 'Headline added')
            return redirect('/headlines')
    else:
        form = HeadlineForm()
        debug_logger(str(request.user), " HEADLINE_ADD_ENTERED")
    return render(request, 'dfirtrack_main/headline/headlines_add.html', {'form': form})

@login_required(login_url="/login")
def headlines_edit(request, pk):
    headline = get_object_or_404(Headline, pk=pk)
    if request.method == 'POST':
        form = HeadlineForm(request.POST, instance=headline)
        if form.is_valid():
            headline = form.save(commit=False)
            headline.save()
            headline.logger(str(request.user), " HEADLINE_EDIT_EXECUTED")
            messages.success(request, 'Headline edited')
            return redirect('/headlines')
    else:
        form = HeadlineForm(instance=headline)
        headline.logger(str(request.user), " HEADLINE_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/headline/headlines_edit.html', {'form': form})
