from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from braces.views import LoginRequiredMixin


class LogoutView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self):
        logout(self.request)
        return reverse_lazy('users:login')

