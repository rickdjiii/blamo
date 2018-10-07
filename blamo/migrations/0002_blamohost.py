# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blamo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlamoHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=150)),
                ('api_key', models.CharField(max_length=128)),
            ],
        ),
    ]