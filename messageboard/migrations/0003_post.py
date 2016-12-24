# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_discussion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(verbose_name=b'auto_now_add=True')),
                ('discussion', models.ForeignKey(to='messageboard.Discussion')),
            ],
        ),
    ]
