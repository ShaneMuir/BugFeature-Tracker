# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-11 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_feature_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='price',
            new_name='upvote_price',
        ),
    ]
