# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 16:56
from __future__ import unicode_literals

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160222_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=core.models.EAWTextField(help_text='Describe yourself with 500 characters or less. There will be no formatting.', max_length=1000, verbose_name='biography'),
        ),
    ]
