# Generated by Django 3.0.5 on 2020-05-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0004_auto_20200520_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='oxygen',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Максимальное потребление кислорода'),
        ),
        migrations.AlterField(
            model_name='primary',
            name='height_father',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', max_digits=4, null=True, verbose_name='Рост отца'),
        ),
        migrations.AlterField(
            model_name='primary',
            name='oxygen',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Максимальное потребление кислорода'),
        ),
    ]