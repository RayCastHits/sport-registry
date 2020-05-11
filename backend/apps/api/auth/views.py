from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class LoginView(FormView):
    """
    Авторизация
    """

    form_class = AuthenticationForm
    template_name = "auth/login.html"
    success_url = "/registry/"

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    """
    Выход
    """

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
