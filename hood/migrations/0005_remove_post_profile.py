# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-16 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_remove_post_business'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]
