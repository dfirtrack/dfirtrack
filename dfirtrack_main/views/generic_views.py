from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from dfirtrack_main.logger.default_logger import debug_logger


class AboutView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = 'dfirtrack_main/about.html'

    def get(self, request, *args, **kwargs):
        debug_logger(str(request.user), ' ABOUT_ENTERED')
        return render(request, self.template_name)

class FaqView(LoginRequiredMixin, TemplateView):
    login_url = '/login'
    template_name = 'dfirtrack_main/faq.html'

    def get(self, request, *args, **kwargs):
        debug_logger(str(request.user), ' FAQ_ENTERED')
        return render(request, self.template_name)
