# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_auto_20170117_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcases',
            name='as_on_date',
            field=models.DateField(),
        ),
    ]
