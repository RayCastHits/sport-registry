# Generated by Django 3.0.5 on 2020-06-13 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0015_sportresult_sportsman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportresult',
            name='sportsman',
        ),
    ]
