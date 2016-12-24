# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0006_auto_20151120_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 0, 42, 23, 45005), verbose_name=b'auto_now_add=true'),
        ),
    ]
