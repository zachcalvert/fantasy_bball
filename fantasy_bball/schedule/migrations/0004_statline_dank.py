# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20161031_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='statline',
            name='dank',
            field=models.BooleanField(default=False),
        ),
    ]