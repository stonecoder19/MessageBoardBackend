# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0009_auto_20151120_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 12, 49, 25, 129156), verbose_name=b'auto_now_add=true'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='discussnumber',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
