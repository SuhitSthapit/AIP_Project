# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquors', '0006_auto_20171016_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquorlist',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]