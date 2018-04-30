# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-22 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sector', '0005_auto_20180305_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorlandingpage',
            name='heading_zh',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_ja',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_pt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='description_zh',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='heading_zh',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_ar',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_de',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_en',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_es',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_fr',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_ja',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_pt',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='pullout_zh',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=0)),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_ar',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_de',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_en',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_es',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_fr',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_ja',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_pt',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='sectorpage',
            name='subsections_zh',
            field=wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))), ('location', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('info', wagtailmarkdown.blocks.MarkdownBlock()), ('map', wagtail.images.blocks.ImageChooserBlock()))))), null=True),
        ),
    ]
