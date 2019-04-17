# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-16 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_comment_retry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='retry',
        ),
        migrations.AddField(
            model_name='comment',
            name='retry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Comment'),
        ),
    ]
