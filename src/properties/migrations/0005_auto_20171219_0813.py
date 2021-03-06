# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20171219_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2)),
            ],
        ),
        migrations.RenameField(
            model_name='propertyitem',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='propertyitem',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='propertyitem',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]
