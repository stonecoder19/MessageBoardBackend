# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
    ]
