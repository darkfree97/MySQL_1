# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Strahova', '0003_auto_20171114_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinformation',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images', verbose_name='Картинка'),
        ),
    ]
