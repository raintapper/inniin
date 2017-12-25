# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-20 13:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import properties.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0010_propertyitem_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyitem',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propertyitem',
            name='title',
            field=models.CharField(max_length=120, validators=[properties.validators.validate_title]),
        ),
    ]
