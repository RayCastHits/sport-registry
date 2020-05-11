from django.db import models
from .other import SportType, Rank


class Sportsman(models.Model):
    """
    Спортсмен
    """

    BODY_TYPE = (
        (0, "Эктоморф"),
        (1, "Эндоморф"),
        (2, "Мезоморф"),
    )
    GENDER = (
        (False, "Мужской"),
        (True, "Женский"),
    )
    SWIMMING = (
        (False, "нет"),
        (True, "есть"),
    )
    SCHOOL_PROGRESS = (
        (0, "Отлично"),
        (1, "Хорошо"),
        (2, "Удовлетворительно"),
    )
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Отчество"
    )
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    gender = models.BooleanField(
        max_length=10, choices=GENDER, verbose_name="Пол",
    )
    location = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Место жительства"
    )
    phone_number = models.CharField(
        max_length=12, verbose_name="Контактный номер", blank=True, null=True
    )
    sports_facility = models.CharField(
        max_length=250,
        verbose_name="Спортивное учреждение",
        blank=True,
        null=True,
    )
    is_swimming = models.BooleanField(
        blank=True, verbose_name="Умение плавать", null=True, choices=SWIMMING,
    )
    school_progress = models.IntegerField(
        choices=SCHOOL_PROGRESS, verbose_name="Успеваемость в школе",
    )
    is_desire = models.BooleanField(
        blank=True, verbose_name="Желание заниматься спортом"
    )
    # coach = models.ForeignKey(
    #     Coach, on_delete=models.CASCADE, verbose_name="Тренер"
    # )
    # parent = models.ForeignKey(
    #     Parent,
    #     on_delete=models.CASCADE,
    #     verbose_name="Представитель",
    #     blank=True,
    #     null=True,
    # )
    sport_type = models.ForeignKey(
        SportType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Вид спорта",
    )
    rank = models.ForeignKey(
        Rank,
        on_delete=models.SET_NULL,
        verbose_name="Разряд",
        blank=True,
        null=True,
    )

    def __str__(self):
        return "%s %s %s" % (self.surname, self.name, self.patronymic)

    def full_name(self):
        if self.patronymic:
            return "%s %s. %s." % (
                self.surname,
                self.name[0],
                self.patronymic[0],
            )
        else:
            return "%s %s." % (self.surname, self.name[0],)

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse("sportsman-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("surname",)
        verbose_name = "Спортсмен"
        verbose_name_plural = "Спортсмены"


class Parent(models.Model):
    """
    Родитель
    """

    child = models.ForeignKey(
        Sportsman, on_delete=models.SET_NULL, blank=True, null=True
    )
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(
        max_length=150, verbose_name="Отчество", blank=True, null=True
    )
    # status = models.CharField(
    #     max_length=15,
    #     choices=PARENT_STATUS,
    #     verbose_name="Статус представителя",
    # )
    telephone = models.CharField(
        max_length=12, verbose_name="Контактный номер", blank=True, null=True
    )
    email = models.EmailField(
        max_length=254, verbose_name="Электронная почта", blank=True, null=True
    )

    def __str__(self):
        return "%s %s %s" % (self.surname, self.name, self.patronymic)

    class Meta:
        ordering = ("surname",)
        verbose_name = "Представитель"
        verbose_name_plural = "Представители"
