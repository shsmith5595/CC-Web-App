# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='grad_year',
            field=models.IntegerField(blank=True, max_length=4),
        ),
    ]
