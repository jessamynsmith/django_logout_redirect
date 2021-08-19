# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/index.html'


class TimeoutLogoutView(LogoutView):

    def dispatch(self, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, "You were logged out due to inactivity")
        return super(TimeoutLogoutView, self).dispatch(*args, **kwargs)
