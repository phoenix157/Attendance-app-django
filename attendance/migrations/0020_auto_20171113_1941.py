# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-13 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0019_auto_20171113_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='principal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]