# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=255)),
                ('created', models.DateTimeField(verbose_name=b'auto_now_add=True')),
                ('forum', models.ForeignKey(to='messageboard.Forum')),
            ],
        ),
    ]
