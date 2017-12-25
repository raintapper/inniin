# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_propertyitem_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='propertyitem',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
