# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0005_auto_20151119_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='lastpostauthor',
            field=models.CharField(default=b'John Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 0, 28, 48, 631757), verbose_name=b'auto_now_add=true'),
        ),
    ]
