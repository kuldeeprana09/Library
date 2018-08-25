# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-13 04:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bookapp', '0002_auto_20180813_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='', max_length=150)),
                ('Contact_Number', models.IntegerField(default='')),
                ('Address', models.CharField(default='', max_length=100)),
                ('Email_ID', models.CharField(default='', max_length=50)),
                ('City', models.CharField(default='', max_length=25)),
                ('State', models.CharField(default='', max_length=25)),
                ('Country', models.CharField(default='', max_length=25)),
                ('Pin_code', models.IntegerField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookdetail',
            name='user',
        ),
        migrations.DeleteModel(
            name='bookdetail',
        ),
    ]