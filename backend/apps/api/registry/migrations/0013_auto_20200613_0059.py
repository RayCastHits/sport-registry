# Generated by Django 3.0.5 on 2020-06-12 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0012_sportresult_sportsman'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primary',
            options={'ordering': ('date',), 'verbose_name': 'Первичное обследование', 'verbose_name_plural': 'Первичные обследования'},
        ),
    ]
