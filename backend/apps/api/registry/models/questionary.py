from django.db import models
from .people import Sportsman


class Survey(models.Model):
    """
    Базовая модель обследований
    """

    STAGE = (
        (0, "1 этап"),
        (1, "2 этап"),
        (2, "3 этап"),
    )
    date = models.DateField(
        auto_now_add=False,
        blank=True,
        null=True,
        verbose_name="Дата обследования",
    )
    stage = models.IntegerField(
        choices=STAGE, blank=True, null=True, verbose_name="Этап",
    )
    weight = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Вес тела (кг)",
    )
    length = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Длина тела(см)",
    )
    spit_leg_length = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Длина ног от вертела(см)"
    )
    foot_length = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Длина стопы (см)",
    )
    torso_length_7 = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Длина туловища от 7-го шейного позвонка(см)",
    )
    arm_span = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Размах рук(см)"
    )
    chest_girth_inspiration = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Обхват грудной клетки на вдохе(см)",
    )
    exhaling_chest = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Обхват грудной клетки на выдохе(см)",
    )
    excursion_difference = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Экскурсия(разница)",
    )
    spirometry = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Спирометрия(ЖЕЛ)мл"
    )
    breath_hold_stange = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Проба с задер.дых.на вдохе(проба Штанге)сек",
    )
    dynamometry = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Становая динамометрия",
    )
    dynamometry_right = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Динамометрия правой кисти(кг)"
    )
    dynamometry_left = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Динамометрия левой кисти(кг)"
    )
    fat_mass = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="% жировой массы",
    )
    muscle_mass = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="% мышечной массы",
    )
    open_eyes = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Открытые глаза (фон)",
    )
    close_eyes = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Закрытые глаза",
    )
    target = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Мишень",
    )
    pwc_kg = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="PWC Кг мм",
    )
    pwc = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="PWC ЧСС",
    )
    pressure_up = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Артериальное давление(верхнее)",
    )
    pressure_down = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Артериальное давление(нижнее)",
    )
    oxygen = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Максимальное потребление кислорода",
    )

    def __str__(self):
        return "%s %s" % (self.date, self.sportsman)

    class Meta:
        ordering = ("date",)
        verbose_name = "Обследование"
        verbose_name_plural = "Обследование"
        abstract = True


class Primary(Survey):
    """
    Первичное медицинское обследование
    """

    MOTIVATION = (
        (0, "Низкая"),
        (1, "Средняя"),
        (2, "Высокая"),
    )
    WILLED_QUALITIES = (
        (0, "Не развитый"),
        (1, "Низкий"),
        (2, "Высокий"),
    )
    NERVOUS_SYSTEM_POTENTIAL = (
        (0, "Слабая"),
        (1, "Средне-слабая"),
        (2, "Средняя"),
        (3, "Средне-сильная"),
        (4, "Сильная"),
    )
    CHEST_SHAPE = (
        (0, "Уплощенная"),
        (1, "Цилиндрическая"),
        (2, "Коническая"),
        (3, "Нормальная"),
    )
    BACK_SHAPE = (
        (0, "Нормальная"),
        (1, "Плоская"),
        (2, "Плоско-выгнутая"),
        (3, "Сутуловатость"),
        (4, "Круглая"),
        (5, "Кругло-вогнутая"),
    )
    BODY_TYPE = (
        (0, "Эктоморф"),
        (1, "Эндоморф"),
        (2, "Мезоморф"),
    )
    sportsman = models.ForeignKey(
        Sportsman,
        on_delete=models.CASCADE,
        verbose_name="Спортсмен",
        related_name="primary",
    )
    diseases = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Перенесенные заболевания(травмы)",
    )
    height_father = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Рост отца",
    )
    weight_father = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Вес отца",
    )
    type_body_father = models.IntegerField(
        choices=BODY_TYPE, blank=True, null=True, verbose_name="Тип тела отца",
    )
    height_mother = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Рост матери",
    )
    weight_mother = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Вес матери",
    )
    type_body_mother = models.IntegerField(
        choices=BODY_TYPE,
        blank=True,
        null=True,
        verbose_name="Тип тела матери",
    )
    front_type = models.IntegerField(
        choices=CHEST_SHAPE,
        blank=True,
        null=True,
        verbose_name="Форма грудной клетки",
    )
    back_type = models.IntegerField(
        choices=BACK_SHAPE, blank=True, null=True, verbose_name="Форма спины",
    )
    # TODO: повтор поля
    past_diseases = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="Перенесенные заболевания(травмы)",
    )  #
    height_father = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Рост отца",
    )  #
    weight_father = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Вес отца",
    )  #
    body_type_father = models.IntegerField(
        choices=BODY_TYPE, blank=True, null=True, verbose_name="Тип тела отца",
    )  #
    height_mother = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Рост матери",
    )  #
    weight_mother = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Вес матери",
    )  #
    body_type_mother = models.IntegerField(
        choices=BODY_TYPE,
        blank=True,
        null=True,
        verbose_name="Тип тела матери",
    )  #
    chest_shape = models.IntegerField(
        choices=CHEST_SHAPE,
        blank=True,
        null=True,
        verbose_name="Форма грудной клетки",
    )  #
    back_shape = models.IntegerField(
        choices=BACK_SHAPE, blank=True, null=True, verbose_name="Форма спины",
    )  #
    speed = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Быстрота"
    )  #
    strength = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Сила%"
    )  #
    stamina = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Выносливость%"
    )  #
    coordination = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Координация%"
    )  #
    nervous_system_potential = models.IntegerField(
        choices=NERVOUS_SYSTEM_POTENTIAL,
        default="Средняя",
        blank=True,
        null=True,
        verbose_name="Потенциал нервной системы",
    )  # псих тест
    run_30 = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Бег 30м",
    )  #
    jump_place = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Прыжок в длину с места",
    )  #
    pull_ups = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Подтягивания на перекладине"
    )  #
    concept = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Концепт(техническая гребля)",
    )  #
    run_1500 = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Бег 1500м",
    )  #
    concept_500 = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Концепт 500м",
    )  #
    motivation = models.IntegerField(
        choices=MOTIVATION,
        blank=True,
        null=True,
        verbose_name="Мотивация к тренеровочному процессу",
    )  # псих тест
    willed_qualities = models.IntegerField(
        choices=WILLED_QUALITIES,
        blank=True,
        null=True,
        verbose_name="Развитие волевых качеств",
    )  # псих тест
    # recommendations = models.ManyToManyField(
    #     Sport_type, blank=True, null=True, verbose_name="Рекомендации"
    # )  #

    def __str__(self):
        return "%s %s" % (self.date, self.stage)

    class Meta:
        ordering = ("date",)
        verbose_name = "Первичное"
        verbose_name_plural = "Первичные"


class Medical(Survey):
    """
    Углубленное медицинское обследование
    """

    sportsman = models.ForeignKey(
        Sportsman,
        on_delete=models.CASCADE,
        verbose_name="Спортсмен",
        related_name="medical",
    )
    ecg = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="ЭКГ в покое"
    )
    ecg_load = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="ЭКГ с нагрузкой"
    )
    heart = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Узи сердца"
    )
    plantometry = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Плантометрия"
    )
    cns_functional = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Фукц.возможности ЦНС"
    )
    cns_level = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Уров.работоспособности ЦНС"
    )
    grv = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="ГРВ",
    )
    golden_ratio = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Золотое сечение(0,16-0,62)"
    )
    voltage_index = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Индекс напряжения"
    )
    spectral_analysis = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Спектральный анализ"
    )
    integral_indicator = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Интегральный показатель"
    )
    adaptive_capabilities = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Адаптационные возм.организма"
    )
    functional_reserves = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Функциональные резервы"
    )

    def __str__(self):
        return "%s %s" % (self.date, self.stage)

    class Meta:
        ordering = ("date",)
        verbose_name = "УМО"
        verbose_name_plural = "УМО"
