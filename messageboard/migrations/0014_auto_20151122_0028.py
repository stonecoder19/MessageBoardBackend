# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0013_auto_20151121_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 22, 0, 28, 25, 743553), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
