# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-02 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concertowl', '0013_auto_20180823_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='details_url',
            field=models.URLField(max_length=500),
        ),
    ]