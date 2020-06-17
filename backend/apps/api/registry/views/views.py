# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from ..models import (
    Sportsman,
    Parent,
    SportType,
    Primary,
    Medical,
    SportResult,
)

from ..forms import PrimaryForm, MedicalForm, ParentForm, SportResultForm
from django.shortcuts import redirect

from django.contrib.contenttypes.models import ContentType

# Доступ разрешен для тренера и администратора
def role_trainer(user):
    if user.role == 0:
        return True
    if user.role == 1:
        return True
    if user.role == 2:
        return False


# Доступ разрешен для медицинского работника и администратора
def role_med(user):
    if user.role == 0:
        return True
    if user.role == 1:
        return False
    if user.role == 2:
        return True


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
        context["Medical"] = Medical.objects.filter(
            sportsman_id=self.object.pk
        )
        context["sport_results"] = SportResult.objects.filter(
            object_id=self.object.pk
        )
        return context


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_trainer, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class SportsmanUpdate(UpdateView):
    """
    Форма обновления спортсменов
    """

    model = Sportsman
    fields = "__all__"
    template_name = "registry/sportsman/update.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_trainer, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class SportsmanCreate(CreateView):
    """
    Форма создания спортсмена
    """

    model = Sportsman
    fields = "__all__"
    template_name = "registry/sportsman/create.html"
    success_url = reverse_lazy("registry:sportsman-list")


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_trainer, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class SportsmanDelete(DeleteView):
    """
    Удаление спортсмена
    """


@method_decorator(login_required, name="dispatch")
class SportTypeList(ListView):
    """
    Список видов спорта
    """

    model = SportType
    template_name = "registry/sporttype/list.html"


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_trainer, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class SportTypeUpdate(UpdateView):
    """
    Форма обновления вида спорта
    """

    model = SportType
    fields = "__all__"
    success_url = reverse_lazy("registry:sporttype-list")
    template_name = "registry/sporttype/update.html"


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_trainer, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class SportTypeCreate(CreateView):
    """
    Форма создания вида спорта
    """

    model = SportType
    fields = "__all__"
    template_name = "registry/sporttype/create.html"
    success_url = reverse_lazy("registry:sporttype-list")


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_trainer, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class ParentCreate(CreateView):
    """
    Форма добавления представителя
    """

    model = Parent
    form_class = ParentForm
    template_name = "registry/sportsman/parent/create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.child_id = self.kwargs["pk"]
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_trainer, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class ParentUpdate(UpdateView):
    """
    Форма обновления представителя
    """

    model = Parent
    form_class = ParentForm
    template_name = "registry/sportsman/parent/update.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.child_id = self.kwargs["pk"]
        obj.save()
        return super().form_valid(form)

    def get_object(self):
        return Parent.objects.get(pk=self.kwargs["parent_pk"])

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return "{}#parent".format(
            reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})
        )


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_med, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class PrimaryCreate(CreateView):
    """
    Форма добавления первичного обследования
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


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_med, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class PrimaryUpdate(UpdateView):
    """
    Форма обновления первичного обследования
    """

    model = Primary
    form_class = PrimaryForm
    template_name = "registry/primary/update.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sportsman_id = self.kwargs["pk"]
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})


@method_decorator(login_required, name="dispatch")
class PrimaryDetail(DetailView):
    """
    Форма просмотра первичного обследования
    """

    model = Primary
    form_class = PrimaryForm
    fields = "__all__"
    template_name = "registry/primary/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name="dispatch")
@method_decorator(
    user_passes_test(role_med, login_url="/", redirect_field_name=None,),
    name="dispatch",
)
class MedicalCreate(CreateView):
    """
    Форма добавления углубленного обследования
    """

    model = Medical
    form_class = MedicalForm
    template_name = "registry/medical/create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sportsman_id = self.kwargs["pk"]
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})


class SportResultPrimaryCreate(CreateView):
    """
    Форма добавления спортивного результата
    """

    model = SportResult
    form_class = SportResultForm
    template_name = "registry/primary/sportresult/create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.object_id = self.kwargs["pk"]
        # obj.content_type = "registry", "primarys"
        obj.content_type = ContentType.objects.get(
            app_label="registry", model="primary"
        )
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})


class SportResultMedicalCreate(CreateView):
    """
    Форма добавления спортивного результата
    """

    model = SportResult
    form_class = SportResultForm
    template_name = "registry/primary/sportresult/create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.object_id = self.kwargs["pk"]
        # obj.content_type = "registry", "primarys"
        obj.content_type = ContentType.objects.get(
            app_label="registry", model="medical"
        )
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})


class SportResultPrimaryUpdate(UpdateView):
    """
    Форма обновления спортивного результата
    """

    model = SportResult
    form_class = SportResultForm
    template_name = "registry/primary/sportresult/update.html"

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.object_id = self.kwargs["pk"]
    #     obj.content_type = ContentType.objects.get(
    #         app_label="registry", model="primary"
    #     )
    #     obj.save()
    #     return super().form_valid(form)

    def get_object(self):
        print(self.kwargs["sportrelust_pk"])
        return SportResult.objects.get(pk=self.kwargs["sportrelust_pk"])

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("registry:sportsman-detail", kwargs={"pk": pk})
