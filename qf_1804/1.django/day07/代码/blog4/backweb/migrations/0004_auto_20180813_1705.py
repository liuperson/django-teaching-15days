# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='out_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='session_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
