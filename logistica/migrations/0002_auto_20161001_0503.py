# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-01 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('cedula', models.TextField(max_length=10)),
            ],
            options={
                'verbose_name': 'Conductor',
                'verbose_name_plural': 'Conductores',
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Ruta',
                'verbose_name_plural': 'Rutas',
            },
        ),
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name': 'Bus', 'verbose_name_plural': 'Buses'},
        ),
    ]