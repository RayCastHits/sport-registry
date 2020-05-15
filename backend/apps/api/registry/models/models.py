# from django.db import models


# class SportType(models.Model):
#     """
#     Вид спорта
#     """

#     name = models.CharField(max_length=250, verbose_name="Наименование")

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ("name",)
#         verbose_name = "Вид спорта"
#         verbose_name_plural = "Виды спорта"


# class Rank(models.Model):
#     """
#     Спортивный разряд
#     """

#     name = models.CharField(
#         max_length=250, verbose_name="Наименование разряда"
#     )
#     rank = models.PositiveIntegerField(verbose_name="Разряд")

#     def __str__(self):
#         return "%s %s" % (self.name, self.rank)

#     class Meta:
#         ordering = (
#             "name",
#             "rank",
#         )
#         verbose_name = "Разряд"
#         verbose_name_plural = "Разряд"


# class Sportsman(models.Model):
#     """
#     Спортсмен
#     """

#     CHEST_SHAPE = (
#         (0, "Уплощенная"),
#         (1, "Цилиндрическая"),
#         (2, "Коническая"),
#         (3, "Нормальная"),
#     )

#     BACK_SHAPE = (
#         (0, "Нормальная"),
#         (1, "Плоская"),
#         (2, "Плоско-выгнутая"),
#         (3, "Сутуловатость"),
#         (4, "Круглая"),
#         (5, "Кругло-вогнутая"),
#     )

#     BODY_TYPE = (
#         (0, "Эктоморф"),
#         (1, "Эндоморф"),
#         (2, "Мезоморф"),
#     )
#     GENDER = (
#         (False, "М"),
#         (True, "Ж"),
#     )
#     SWIMMING = (
#         (False, "нет"),
#         (True, "есть"),
#     )
#     SCHOOL_PROGRESS = (
#         (0, "Отлично"),
#         (1, "Хорошо"),
#         (2, "Удовлетворительно"),
#     )
#     name = models.CharField(max_length=150, verbose_name="Имя")
#     surname = models.CharField(max_length=150, verbose_name="Фамилия")
#     patronymic = models.CharField(
#         max_length=150, blank=True, null=True, verbose_name="Отчество"
#     )
#     date_of_birth = models.DateField(verbose_name="Дата рождения")
#     gender = models.BooleanField(
#         max_length=10, choices=GENDER, verbose_name="Пол",
#     )
#     location = models.TextField(
#         blank=True, null=True, verbose_name="Место жительства"
#     )
#     phone_number = models.CharField(
#         max_length=12, verbose_name="Контактный номер", blank=True, null=True
#     )
#     sports_facility = models.CharField(
#         max_length=250,
#         verbose_name="Спортивное учреждение",
#         blank=True,
#         null=True,
#     )
#     is_swimming = models.BooleanField(
#         blank=True, verbose_name="Умение плавать", null=True, choices=SWIMMING,
#     )
#     school_progress = models.IntegerField(
#         max_length=4,
#         choices=SCHOOL_PROGRESS,
#         verbose_name="Успеваемость в школе",
#     )
#     is_desire = models.BooleanField(
#         blank=True, verbose_name="Желание заниматься спортом"
#     )
#     # coach = models.ForeignKey(
#     #     Coach, on_delete=models.CASCADE, verbose_name="Тренер"
#     # )
#     # parent = models.ForeignKey(
#     #     Parent,
#     #     on_delete=models.CASCADE,
#     #     verbose_name="Представитель",
#     #     blank=True,
#     #     null=True,
#     # )
#     sport_type = models.ForeignKey(
#         SportType,
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#         verbose_name="Вид спорта",
#     )
#     rank = models.ForeignKey(
#         Rank,
#         on_delete=models.SET_NULL,
#         verbose_name="Разряд",
#         blank=True,
#         null=True,
#     )
#     diseases = models.CharField(
#         max_length=250,
#         blank=True,
#         null=True,
#         verbose_name="Перенесенные заболевания(травмы)",
#     )
#     height_father = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Рост отца",
#     )
#     weight_father = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Вес отца",
#     )
#     type_body_father = models.CharField(
#         max_length=10,
#         choices=BODY_TYPE,
#         blank=True,
#         null=True,
#         verbose_name="Тип тела отца",
#     )
#     height_mother = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Рост матери",
#     )
#     weight_mother = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Вес матери",
#     )
#     type_body_mother = models.CharField(
#         max_length=10,
#         choices=BODY_TYPE,
#         blank=True,
#         null=True,
#         verbose_name="Тип тела матери",
#     )
#     front_type = models.CharField(
#         max_length=15,
#         choices=CHEST_SHAPE,
#         blank=True,
#         null=True,
#         verbose_name="Форма грудной клетки",
#     )
#     back_type = models.CharField(
#         max_length=20,
#         choices=BACK_SHAPE,
#         blank=True,
#         null=True,
#         verbose_name="Форма спины",
#     )

#     def __str__(self):
#         return "%s %s %s" % (self.surname, self.name, self.patronymic)

#     def full_name(self):
#         if self.patronymic:
#             return "%s %s. %s." % (
#                 self.surname,
#                 self.name[0],
#                 self.patronymic[0],
#             )
#         else:
#             return "%s %s." % (self.surname, self.name[0],)

#     # def get_absolute_url(self, *args, **kwargs):
#     #     return reverse("sportsman-detail", kwargs={"pk": self.pk})

#     class Meta:
#         ordering = ("surname",)
#         verbose_name = "Спортсмен"
#         verbose_name_plural = "Спортсмены"


# class Survey(models.Model):
#     """
#     Базовая модель обследований
#     """

#     STAGE = (
#         (0, "1 этап"),
#         (1, "2 этап"),
#         (2, "3 этап"),
#     )
#     date = models.DateField(
#         auto_now_add=False,
#         blank=True,
#         null=True,
#         verbose_name="Дата обследования",
#     )
#     stage = models.CharField(
#         max_length=15,
#         choices=STAGE,
#         blank=True,
#         null=True,
#         verbose_name="Этап",
#     )
#     sportsman = models.ForeignKey(
#         Sportsman, on_delete=models.CASCADE, verbose_name="Спортсмен"
#     )
#     weight = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Вес тела (кг)",
#     )
#     length = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Длина тела(см)",
#     )
#     spit_leg_length = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Длина ног от вертела(см)"
#     )
#     foot_length = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Длина стопы (см)",
#     )
#     torso_length_7 = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Длина туловища от 7-го шейного позвонка(см)",
#     )
#     arm_span = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Размах рук(см)"
#     )
#     chest_girth_inspiration = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Обхват грудной клетки на вдохе(см)",
#     )
#     exhaling_chest = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Обхват грудной клетки на выдохе(см)",
#     )
#     excursion_difference = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Экскурсия(разница)",
#     )
#     spirometry = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Спирометрия(ЖЕЛ)мл"
#     )
#     breath_hold_stange = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Проба с задер.дых.на вдохе(проба Штанге)сек",
#     )
#     dynamometry = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Становая динамометрия",
#     )
#     dynamometry_right = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Динамометрия правой кисти(кг)"
#     )
#     dynamometry_left = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Динамометрия левой кисти(кг)"
#     )
#     fat_mass = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="% жировой массы",
#     )
#     muscle_mass = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="% мышечной массы",
#     )
#     open_eyes = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Открытые глаза (фон)",
#     )
#     close_eyes = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Закрытые глаза",
#     )
#     target = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Мишень",
#     )
#     pwc_kg = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="PWC Кг мм",
#     )
#     pwc = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="PWC ЧСС",
#     )
#     pressure_up = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Артериальное давление(верхнее)",
#     )
#     pressure_down = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Артериальное давление(нижнее)",
#     )
#     oxygen = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="Максимальное потребление кислорода",
#     )

#     def __str__(self):
#         return "%s %s" % (self.date, self.sportsman)

#     class Meta:
#         ordering = ("date",)
#         verbose_name = "Обследование"
#         verbose_name_plural = "Обследование"
#         abstract = True


# class UMO(Survey):
#     """
#     Углубленное медицинское обследование
#     """

#     ecg = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="ЭКГ в покое"
#     )
#     ecg_load = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="ЭКГ с нагрузкой"
#     )
#     heart = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Узи сердца"
#     )
#     plantometry = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Плантометрия"
#     )
#     cns_functional = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Фукц.возможности ЦНС"
#     )
#     cns_level = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Уров.работоспособности ЦНС"
#     )
#     grv = models.DecimalField(
#         max_digits=4,
#         decimal_places=1,
#         blank=True,
#         null=True,
#         verbose_name="ГРВ",
#     )
#     golden_ratio = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Золотое сечение(0,16-0,62)"
#     )
#     voltage_index = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Индекс напряжения"
#     )
#     spectral_analysis = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Спектральный анализ"
#     )
#     integral_indicator = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Интегральный показатель"
#     )
#     adaptive_capabilities = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Адаптационные возм.организма"
#     )
#     functional_reserves = models.PositiveIntegerField(
#         blank=True, null=True, verbose_name="Функциональные резервы"
#     )

#     def __str__(self):
#         return "%s %s" % (self.date, self.stage)

#     class Meta:
#         ordering = ("date",)
#         verbose_name = "УМО"
#         verbose_name_plural = "УМО"
