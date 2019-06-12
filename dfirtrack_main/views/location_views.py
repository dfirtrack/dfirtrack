from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import LocationForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Location

class LocationList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Location
    template_name = 'dfirtrack_main/location/locations_list.html'
    context_object_name = 'location_list'
    def get_queryset(self):
        debug_logger(str(self.request.user), " LOCATION_ENTERED")
        return Location.objects.order_by('location_name')

class LocationDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Location
    template_name = 'dfirtrack_main/location/locations_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = self.object
        location.logger(str(self.request.user), " LOCATIONDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def locations_add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            location.logger(str(request.user), " LOCATION_ADD_EXECUTED")
            messages.success(request, 'Location added')
            return redirect('/locations')
    else:
        form = LocationForm()
        debug_logger(str(request.user), " LOCATION_ADD_ENTERED")
    return render(request, 'dfirtrack_main/location/locations_add.html', {'form': form})

@login_required(login_url="/login")
def locations_add_popup(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            location.logger(str(request.user), " LOCATION_ADD_POPUP_EXECUTED")
            messages.success(request, 'Location added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = LocationForm()
        debug_logger(str(request.user), " LOCATION_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/location/locations_add_popup.html', {'form': form})

@login_required(login_url="/login")
def locations_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            location.logger(str(request.user), " LOCATION_EDIT_EXECUTED")
            messages.success(request, 'Location edited')
            return redirect('/locations')
    else:
        form = LocationForm(instance=location)
        location.logger(str(request.user), " LOCATION_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/location/locations_edit.html', {'form': form})
