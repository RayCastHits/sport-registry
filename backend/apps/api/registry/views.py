# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Sportsman, Parent, SportType, Primary, UMO

from .forms import PrimaryForm

# from . import forms


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
        context["primarys"] = Primary.objects.filter(
            sportsman_id=self.object.pk
        )
        context["UMO"] = UMO.objects.filter(sportsman_id=self.object.pk)
        # TODO: объекты обследований.
        return context


@method_decorator(login_required, name="dispatch")
class SportsmanUpdate(UpdateView):
    """
    Форма спортсменов
    """

    model = Sportsman
    fields = "__all__"
    template_name = "registry/sportsman/update.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})


@method_decorator(login_required, name="dispatch")
class SportTypeList(ListView):
    """
    Список виды спорта
    """

    model = SportType
    template_name = "registry/sporttype/list.html"


@method_decorator(login_required, name="dispatch")
class SportTypeUpdate(UpdateView):
    """
    Форма виды спорта
    """

    model = SportType
    fields = "__all__"
    success_url = reverse_lazy("registry:sporttype-list")
    template_name = "registry/sporttype/update.html"


@method_decorator(login_required, name="dispatch")
class PrimaryCreate(CreateView):
    """
    Форма виды спорта
    """

    model = Primary
    form_class = PrimaryForm
    template_name = "registry/primary/create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sportsman_id = self.kwargs["pk"]
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})
