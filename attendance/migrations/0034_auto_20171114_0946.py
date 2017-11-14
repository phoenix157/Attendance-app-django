# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-14 04:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0033_auto_20171114_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='attendance.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]