# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sector', '0006_auto_20180322_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sectorlandingpage',
            old_name='heading_zh',
            new_name='heading_zh_cn',
        ),
        migrations.RenameField(
            model_name='sectorpage',
            old_name='description_zh',
            new_name='description_zh_cn',
        ),
        migrations.RenameField(
            model_name='sectorpage',
            old_name='heading_zh',
            new_name='heading_zh_cn',
        ),
        migrations.RenameField(
            model_name='sectorpage',
            old_name='pullout_zh',
            new_name='pullout_zh_cn',
        ),
        migrations.RenameField(
            model_name='sectorpage',
            old_name='subsections_zh',
            new_name='subsections_zh_cn',
        ),
    ]