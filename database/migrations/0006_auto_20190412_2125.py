# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20190412_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_order',
            new_name='orderNo',
        ),
    ]