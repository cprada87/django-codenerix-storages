# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-18 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_storages', '0004_auto_20180118_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagebox',
            name='weight',
            field=models.FloatField(default=0, verbose_name='Weight'),
        ),
    ]