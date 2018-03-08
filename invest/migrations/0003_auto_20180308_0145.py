# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0002_branding_footer_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='branding',
            name='footer_copyright',
            field=models.CharField(default='© Crown copyright 2018. All rights reserved.', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branding',
            name='footer_secondary_nav',
            field=wagtail.core.fields.StreamField((('internal_link', wagtail.core.blocks.PageChooserBlock()),), blank=True),
        ),
    ]
