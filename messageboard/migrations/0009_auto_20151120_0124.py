# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0008_auto_20151120_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='firstpostauthor',
            field=models.CharField(default=b'Jane Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='discussion',
            name='postnumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='forum',
            name='discussnumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='lastposttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 1, 24, 54, 856499), verbose_name=b'auto_now_add=true'),
        ),
    ]
