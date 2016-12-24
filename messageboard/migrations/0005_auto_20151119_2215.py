# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0004_auto_20151119_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
    ]
