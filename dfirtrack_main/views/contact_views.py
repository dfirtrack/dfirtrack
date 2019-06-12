from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from dfirtrack_main.forms import ContactForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Contact

class ContactList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Contact
    template_name = 'dfirtrack_main/contact/contacts_list.html'
    def get_queryset(self):
        debug_logger(str(self.request.user), " CONTACT_ENTERED")
        return Contact.objects.order_by('contact_name')

class ContactDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Contact
    template_name = 'dfirtrack_main/contact/contacts_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = self.object
        contact.logger(str(self.request.user), " CONTACTDETAIL_ENTERED")
        return context

@login_required(login_url="/login")
def contacts_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            contact.logger(str(request.user), " CONTACT_ADD_EXECUTED")
            messages.success(request, 'Contact added')
            return redirect('/contacts')
    else:
        form = ContactForm()
        debug_logger(str(request.user), " CONTACT_ADD_ENTERED")
    return render(request, 'dfirtrack_main/contact/contacts_add.html', {'form': form})

@login_required(login_url="/login")
def contacts_add_popup(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            contact.logger(str(request.user), " CONTACT_ADD_POPUP_EXECUTED")
            messages.success(request, 'Contact added')
            return HttpResponse('<script type="text/javascript">window.close();</script>')
    else:
        form = ContactForm()
        debug_logger(str(request.user), " CONTACT_ADD_POPUP_ENTERED")
    return render(request, 'dfirtrack_main/contact/contacts_add_popup.html', {'form': form})

@login_required(login_url="/login")
def contacts_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            contact.logger(str(request.user), " CONTACT_EDIT_EXECUTED")
            messages.success(request, 'Contact edited')
            return redirect('/contacts')
    else:
        form = ContactForm(instance=contact)
        contact.logger(str(request.user), " CONTACT_EDIT_ENTERED")
    return render(request, 'dfirtrack_main/contact/contacts_edit.html', {'form': form})
