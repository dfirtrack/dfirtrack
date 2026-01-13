from django.conf import settings
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = "dfirtrack_main/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["OIDC_ENABLED"] = getattr(settings, "OIDC_ENABLED", False)
        return context
