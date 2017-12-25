# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-22 03:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20171221_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='activation_key',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL),
        ),
    ]