# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-02 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('gender', models.CharField(default='unknown', max_length=16)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('hobby', models.CharField(default=None, max_length=256)),
                ('description', models.CharField(default=None, max_length=512)),
                ('regis_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('blog_num', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
