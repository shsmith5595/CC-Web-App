# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 05:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_auto_20171206_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]