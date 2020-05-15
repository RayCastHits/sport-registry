# Generated by Django 3.0.5 on 2020-05-15 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_auto_20200418_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsman',
            name='gender',
            field=models.BooleanField(choices=[(False, 'Мужской'), (True, 'Женский')], max_length=10, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='sportsman',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Место жительства'),
        ),
    ]