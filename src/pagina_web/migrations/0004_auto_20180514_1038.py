# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-14 07:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0003_auto_20180512_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequentlyaskedquestions',
            name='faq_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina_web.FaqCategory'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 14, 7, 38, 56, 824283, tzinfo=utc), verbose_name='date joined'),
        ),
    ]