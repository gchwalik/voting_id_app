# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicSite', '0006_auto_20171210_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpee',
            name='info',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='helpee',
            name='money',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='helpee',
            name='travel',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
