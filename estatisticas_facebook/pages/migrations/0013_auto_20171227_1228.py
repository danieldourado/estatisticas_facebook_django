# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-27 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20171226_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='post_paging',
        ),
        migrations.AddField(
            model_name='pageinsights',
            name='post_paging',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
