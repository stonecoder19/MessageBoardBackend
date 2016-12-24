# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0010_auto_20151120_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='firstpostauthor',
            field=models.CharField(default=b'Jane Doe', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='lastpostauthor',
            field=models.CharField(default=b'John Doe', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 1, 6, 50, 645235), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
