# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20180322_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='heading_zh',
            new_name='heading_zh_cn',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='how_we_help_title_zh',
            new_name='how_we_help_title_zh_cn',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='how_we_help_zh',
            new_name='how_we_help_zh_cn',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='sector_title_zh',
            new_name='sector_title_zh_cn',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='setup_guide_lead_in_zh',
            new_name='setup_guide_lead_in_zh_cn',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='setup_guide_title_zh',
            new_name='setup_guide_title_zh_cn',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='sub_heading_zh',
            new_name='sub_heading_zh_cn',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='subsections_zh',
            new_name='subsections_zh_cn',
        ),
    ]
