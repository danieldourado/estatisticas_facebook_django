# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-06 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='name',
        ),
    ]
