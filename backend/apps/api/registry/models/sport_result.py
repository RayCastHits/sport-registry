from django.db import models
from .people import Sportsman

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Distance(models.Model):
    """
    Дистанция
    """

    count = models.IntegerField(verbose_name="Кол-во метров")

    def __str__(self):
        return self.count

    class Meta:
        verbose_name = "Дистанция"
        verbose_name_plural = "Дистанции"


class SportResult(models.Model):
    """
    Спортивный результат
    """

    LEVEL = (
        (0, "Локальный"),
        (1, "Областной"),
        (2, "Всероссийский"),
        (3, "Международный"),
    )
    PRIZE = (
        (0, "Другое"),
        (1, "1 место"),
        (2, "2 место"),
        (3, "3 место"),
    )
    # sportsman = models.ForeignKey(
    #     Sportsman,
    #     verbose_name="Спортсмен",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="sport_result",
    # )
    date = models.DateField(verbose_name="Дата")
    level = models.IntegerField(
        verbose_name="Уровень соревнований", choices=LEVEL
    )
    prize = models.IntegerField(verbose_name="Место", choices=PRIZE)
    result = models.TimeField(verbose_name="Время")
    distance = models.ForeignKey(
        Distance,
        verbose_name="Дистанция",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return "%s %s" % (self.date, self.level)

    class Meta:
        verbose_name = "Спортивный результат"
        verbose_name_plural = "Спортивные результаты"
