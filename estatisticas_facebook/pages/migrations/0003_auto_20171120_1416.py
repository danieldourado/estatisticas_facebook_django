# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-20 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='since',
            field=models.DateField(auto_now_add=True),
        ),
    ]