from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import RecommendationForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Recommendation

class RecommendationList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Recommendation
    template_name = 'dfirtrack_main/recommendation/recommendations_list.html'
    context_object_name = 'recommendation_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " RECOMMENDATION_ENTERED")
        return Recommendation.objects.order_by('recommendation_name')

class RecommendationDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Recommendation
    template_name = 'dfirtrack_main/recommendation/recommendations_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recommendation = self.object
        recommendation.logger(str(self.request.user), " RECOMMENDATIONDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def recommendations_add(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.save()
            recommendation.logger(str(request.user), " RECOMMENDATION_ADD_EXECUTED")
            messages.success(request, 'Recommendation added')
            return redirect('/recommendations')
    else:
        form = RecommendationForm()
        debug_logger(str(request.user), " RECOMMENDATION_ADD_ENTERED")
    return render(request, 'dfirtrack_main/recommendation/recommendations_add.html', {'form': form})

@login_required(login_url="/login")
def recommendations_add_popup(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.save()
            recommendation.logger(str(request.user), " RECOMMENDATION_ADD_POPUP_EXECUTED")
            messages.success(request, 'Recommendation added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = RecommendationForm()
        debug_logger(str(request.user), " RECOMMENDATION_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/recommendation/recommendations_add_popup.html', {'form': form})

@login_required(login_url="/login")
def recommendations_edit(request, pk):
    recommendation = get_object_or_404(Recommendation, pk=pk)
    if request.method == 'POST':
        form = RecommendationForm(request.POST, instance=recommendation)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.save()
            recommendation.logger(str(request.user), " RECOMMENDATION_EDIT_EXECUTED")
            messages.success(request, 'Recommendation edited')
            return redirect('/recommendations')
    else:
        form = RecommendationForm(instance=recommendation)
        recommendation.logger(str(request.user), " RECOMMENDATION_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/recommendation/recommendations_edit.html', {'form': form})
