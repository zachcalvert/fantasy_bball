# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0015_auto_20161222_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchup',
            name='result',
        ),
        migrations.RemoveField(
            model_name='team',
            name='needed_stat',
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default='Team', max_length=30),
        ),
    ]
