# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-13 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='bookid',
            field=models.IntegerField(),
        ),
    ]
