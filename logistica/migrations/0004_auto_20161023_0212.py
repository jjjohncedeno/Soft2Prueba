# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-23 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0003_auto_20161023_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='marca',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='nDisco',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='placa',
            field=models.TextField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='tipo',
            field=models.CharField(choices=[(b'e', b'Entrada'), (b's', b'Salida')], default=((b'e', b'Entrada'), (b's', b'Salida')), max_length=2),
        ),
    ]
