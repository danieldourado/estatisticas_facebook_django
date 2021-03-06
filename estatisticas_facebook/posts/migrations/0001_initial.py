# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-30 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0010_auto_20171130_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('comments', models.IntegerField()),
                ('shares', models.IntegerField()),
                ('reactions', models.IntegerField()),
                ('post_reactions_like_total', models.IntegerField()),
                ('post_reactions_love_total', models.IntegerField()),
                ('post_reactions_wow_total', models.IntegerField()),
                ('post_reactions_haha_total', models.IntegerField()),
                ('post_reactions_sorry_total', models.IntegerField()),
                ('post_reactions_anger_total', models.IntegerField()),
                ('post_reactions_positivo_total', models.IntegerField()),
                ('post_reactions_negativo_total', models.IntegerField()),
                ('created_time', models.CharField(max_length=45)),
                ('message', models.CharField(max_length=4500)),
                ('permalink_url', models.CharField(max_length=4500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page')),
            ],
        ),
    ]
