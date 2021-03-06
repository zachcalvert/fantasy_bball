# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-14 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0008_draftpick_draft_round'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('week', models.IntegerField(default=22)),
                ('finalized', models.BooleanField(default=False)),
                ('home_points', models.FloatField(default=0.0)),
                ('away_points', models.FloatField(default=0.0)),
                ('result', models.CharField(blank=True, max_length=10, null=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away', to='leagues.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='leagues.Team')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='league', to='leagues.League')),
            ],
        ),
    ]
