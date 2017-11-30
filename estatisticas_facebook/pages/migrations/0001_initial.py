# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-17 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=4000)),
                ('pretty_name', models.CharField(blank=True, max_length=4000, null=True)),
                ('paging_next', models.CharField(blank=True, max_length=4000, null=True)),
                ('access_token', models.CharField(blank=True, max_length=4500, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageInsights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('end_time', models.DateTimeField()),
                ('period', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=4500)),
                ('description', models.CharField(max_length=4500)),
                ('name', models.CharField(max_length=4500)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page')),
            ],
        ),
    ]