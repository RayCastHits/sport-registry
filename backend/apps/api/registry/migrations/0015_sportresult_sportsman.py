# Generated by Django 3.0.5 on 2020-06-12 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0014_remove_sportresult_sportsman'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportresult',
            name='sportsman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sport_result', to='registry.Sportsman', verbose_name='Спортсмен'),
        ),
    ]
