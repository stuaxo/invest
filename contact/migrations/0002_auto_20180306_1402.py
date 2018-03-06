# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformpage',
            name='heading',
            field=models.CharField(default='Contact Us', max_length=255),
        ),
        migrations.AddField(
            model_name='feedbackformpage',
            name='heading',
            field=models.CharField(default='Feedback', max_length=255),
        ),
        migrations.AddField(
            model_name='reportissueformpage',
            name='heading',
            field=models.CharField(default='Report Issue', max_length=255),
        ),
    ]
