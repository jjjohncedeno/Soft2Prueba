# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-23 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0002_auto_20161001_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateTimeField(auto_now=True)),
                ('fechaFin', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.AlterField(
            model_name='bus',
            name='cParados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='cSentados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Horario', to='logistica.Bus'),
        ),
        migrations.AddField(
            model_name='horario',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Horario', to='logistica.Conductor'),
        ),
        migrations.AddField(
            model_name='horario',
            name='ruta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Horario', to='logistica.Ruta'),
        ),
    ]
