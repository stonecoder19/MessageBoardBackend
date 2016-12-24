# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0012_auto_20151121_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 23, 8, 56, 503768), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
