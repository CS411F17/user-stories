# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171201_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]