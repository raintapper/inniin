# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20171219_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyitem',
            name='description',
            field=models.CharField(default='This is a property description', max_length=400),
        ),
    ]