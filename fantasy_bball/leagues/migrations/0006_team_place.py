# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-12 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0005_league_roster_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='place',
            field=models.IntegerField(default=1),
        ),
    ]