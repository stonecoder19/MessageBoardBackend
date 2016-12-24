# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0011_auto_20151121_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 21, 1, 9, 2, 326876), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='postnumber',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
