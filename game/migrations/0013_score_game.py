# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_score_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='game',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='score', to='game.Game'),
            preserve_default=False,
        ),
    ]