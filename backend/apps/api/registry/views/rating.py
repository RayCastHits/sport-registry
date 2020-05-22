# from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import View
from django.shortcuts import render

# from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..services.rating import get_primary_rating, get_names_fields_model
from ..models import Primary, Sportsman
from ..services.const import (
    ALL_PARAMS,
    PHUSICAL_ABILITIES_PARAMS,
    PHUSICAL_PARAMS,
    MENTAL_PARAMS,
)


@method_decorator(login_required, name="dispatch")
class PrimaryRating(View):
    """
    Список рейтингов спортсменов
    """

    # print(get_maximum_attribute_values(Primary))
    # print(get_primary_rating(Primary))
    template_name = "rating/primary.html"

    def get(self, request, *args, **kwargs):
        params = request.GET.getlist("params[]")
        if len(params) == 0:
            context = {
                "object_list": get_primary_rating(
                    Primary, Sportsman, ALL_PARAMS
                ),
                "params_list": ALL_PARAMS,
            }
        else:
            context = {
                "object_list": get_primary_rating(Primary, Sportsman, params),
                "params_list": ALL_PARAMS,
            }
        return render(request, self.template_name, context)
