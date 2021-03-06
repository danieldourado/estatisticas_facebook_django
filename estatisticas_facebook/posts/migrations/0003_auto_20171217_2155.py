# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-17 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20171206_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_reactions_negativo_porcentagem',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='post_reactions_positivo_porcentagem',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=450),
        ),
        migrations.AlterField(
            model_name='post',
            name='permalink_url',
            field=models.CharField(default='', max_length=450),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_anger_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_haha_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_like_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_love_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_negativo_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_positivo_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_sorry_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_reactions_wow_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='reactions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]
