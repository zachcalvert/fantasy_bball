# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-14 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0007_draftpick'),
    ]

    operations = [
        migrations.AddField(
            model_name='draftpick',
            name='draft_round',
            field=models.IntegerField(default=1),
        ),
    ]