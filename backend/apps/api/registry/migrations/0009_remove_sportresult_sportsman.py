# Generated by Django 3.0.5 on 2020-06-12 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0008_auto_20200612_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportresult',
            name='sportsman',
        ),
    ]
