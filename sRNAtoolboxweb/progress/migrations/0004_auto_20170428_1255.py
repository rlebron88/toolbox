# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-28 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0003_auto_20170428_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobstatus',
            name='finish_time',
            field=models.DateTimeField(null=True),
        ),
    ]
