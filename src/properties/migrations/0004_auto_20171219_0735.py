# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 07:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20171219_0732'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Property',
            new_name='PropertyItem',
        ),
    ]
