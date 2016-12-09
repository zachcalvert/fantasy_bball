# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-08 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_matchup_league'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='statlines',
        ),
        migrations.AddField(
            model_name='game',
            name='statlines',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_stats', to='schedule.StatLine'),
        ),
    ]
