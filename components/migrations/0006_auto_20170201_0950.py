# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_auto_20170117_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcases',
            name='comp_id',
        ),
        migrations.DeleteModel(
            name='TestCases',
        ),
    ]
