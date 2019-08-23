# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-01 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=90, verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('parent_message', models.IntegerField(default=0)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic')),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
