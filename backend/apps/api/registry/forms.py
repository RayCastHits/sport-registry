from django.forms import ModelForm, inlineformset_factory
from . import models


class ParentForm(ModelForm):
    """
    Форма Родителя
    """

    class Meta:
        model = models.Parent
        fields = "__all__"
        # exclude = ['']


class SportsmanForm(ModelForm):
    """
    Форма спортсмена
    """

    class Meta:
        model = models.Sportsman
        fields = "__all__"
        # exclude = ['']


SportsmanFormSet = inlineformset_factory(
    models.Sportsman,
    models.Parent,
    form=ParentForm,
    max_num=2,
    fields="__all__",
)


class PrimaryForm(ModelForm):
    class Meta:
        model = models.Primary
        exclude = ["sportsman"]


class MedicalForm(ModelForm):
    class Meta:
        model = models.Medical
        exclude = ["sportsman"]


class ParentForm(ModelForm):
    class Meta:
        model = models.Parent
        exclude = ["child"]


class SportResultForm(ModelForm):
    class Meta:
        model = models.SportResult
        exclude = ["content_object", "object_id", "content_type"]
