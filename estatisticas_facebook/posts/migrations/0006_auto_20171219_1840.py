# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-19 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20171218_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
