# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-12 10:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0002_auto_20180512_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FrequentlyAskedQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=500)),
                ('answer', models.TextField(blank=True, max_length=500)),
                ('faq_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pagina_web.FaqCategory')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 12, 10, 40, 12, 884968, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
