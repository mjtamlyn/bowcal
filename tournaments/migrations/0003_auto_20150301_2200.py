# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20150301_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tournament',
            name='submission_notes',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
    ]
