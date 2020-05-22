from django.db.models import Max
from decimal import Decimal


def get_names_fields_model(model):
    """
    Возвращает названия полей модели
    """
    result = []
    for field in model._meta.get_fields():
        # print(field.)
        result.append(str(field).split(".")[-1])
    return result


def _get_maximum_attribute_values(model, fields):
    """
    Возвращает максимальные значения атрибутов
    """
    result = []
    for field_name in fields:
        result.append(model.objects.aggregate(Max(field_name)))
    return result


def _get_value_from_list_of_dicts(list_of_dicts, field_name):
    return next(
        item for item in list_of_dicts if field_name + "__max" in item
    )[field_name + "__max"]


def get_attribute_weight(parameter_list):
    return []


def get_primary_rating(model_examination, model_sportsman, fields):
    """
    Возвращает рейтинг первичных обследований
    """
    queryset = model_examination.objects.all()
    max_values = _get_maximum_attribute_values(model_examination, fields)
    result = []
    for instance in queryset:
        rating_value = 0
        sportsman_id = instance.sportsman_id
        for field_name in fields:
            value = getattr(instance, field_name)
            if isinstance(value, (int, Decimal)):
                max_value = _get_value_from_list_of_dicts(
                    max_values, field_name
                )
                if max_value != 0:
                    rating_value += Decimal(max_value) / Decimal(value)
                else:
                    rating_value += 0
            else:
                continue

        result.append(
            {
                "rating_value": round(rating_value, 3),
                "sportsman": model_sportsman.objects.filter(
                    pk=sportsman_id
                ).first(),
            }
        )
    return result
