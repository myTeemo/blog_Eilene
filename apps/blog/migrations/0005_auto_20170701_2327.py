# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-01 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_imagelib'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelib',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m', verbose_name='\u56fe\u7247\u5730\u5740'),
        ),
    ]
