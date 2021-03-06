# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-09 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20180509_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_reactions_negativo_porcentagem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_positivo_porcentagem',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='taxa_de_engajamento',
            field=models.FloatField(default=0),
        ),
    ]
