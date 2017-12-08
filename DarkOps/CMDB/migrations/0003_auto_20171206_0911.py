# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0002_auto_20171205_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhost',
            name='host',
        ),
        migrations.RemoveField(
            model_name='userhost',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='UserHost',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]