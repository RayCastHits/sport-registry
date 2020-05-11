# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Sportsman, Parent

from . import forms


@method_decorator(login_required, name="dispatch")
class SportsmanList(ListView):
    """
    Список спортсменов
    """

    model = Sportsman
    template_name = "registry/sportsman/list.html"


@method_decorator(login_required, name="dispatch")
class SportsmanDetail(DetailView):
    """
    Детальный просмотр спортсменов
    """

    model = Sportsman
    template_name = "registry/sportsman/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["parents"] = Parent.objects.filter(child=self.object.pk)
        # TODO: объекты обследований.
        return context


@method_decorator(login_required, name="dispatch")
class SportsmanUpdate(UpdateView):
    """
    Форма спортсменов
    """

    model = Sportsman
    fields = "__all__"
    success_url = reverse_lazy("registry:sportsman-list")
    template_name = "registry/sportsman/update.html"
