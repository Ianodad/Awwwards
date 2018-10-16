# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 11:53
from __future__ import unicode_literals

import collect.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_auto_20181015_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=200, verbose_name=collect.models.Profile),
        ),
        migrations.AddField(
            model_name='categories',
            name='name',
            field=models.ManyToManyField(to='collect.Projects'),
        ),
    ]
