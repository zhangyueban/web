# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-29 13:58
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VipMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vip_name', models.CharField(max_length=30, verbose_name='留言者')),
                ('content', ckeditor.fields.RichTextField(verbose_name='留言内容')),
                ('message_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '留言板',
                'verbose_name_plural': '留言板',
                'db_table': 'tb_message',
            },
        ),
    ]