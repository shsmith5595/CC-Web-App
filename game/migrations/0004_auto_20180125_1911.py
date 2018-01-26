# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20171225_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='away_cups',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='home_cups',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='loser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='game.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='played',
            field=models.BooleanField(default=False, verbose_name='Played'),
        ),
        migrations.AddField(
            model_name='game',
            name='scrimmage',
            field=models.BooleanField(default=False, verbose_name='Scrimmage'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='game.Team'),
            preserve_default=False,
        ),
    ]
