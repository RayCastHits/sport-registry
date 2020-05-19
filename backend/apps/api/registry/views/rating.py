# from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import View

# from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..services.rating import get_primary_rating
from ..models import Primary
from django.shortcuts import render


@method_decorator(login_required, name="dispatch")
class PrimaryRating(View):
    """
    Список спортсменов
    """

    # print(get_maximum_attribute_values(Primary))
    # print(get_primary_rating(Primary))
    template_name = "rating/primary.html"

    def get(self, request, *args, **kwargs):
        context = {"object_list": get_primary_rating(Primary)}

        return render(request, self.template_name, context)
