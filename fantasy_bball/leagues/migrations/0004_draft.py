# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-12 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0003_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League')),
            ],
        ),
    ]
