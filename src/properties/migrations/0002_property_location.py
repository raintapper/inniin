# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=120, null=True),
        ),
    ]