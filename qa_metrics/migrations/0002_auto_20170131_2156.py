# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_metrics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]