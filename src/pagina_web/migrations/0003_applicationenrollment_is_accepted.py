# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-07 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0002_applicationenrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationenrollment',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]