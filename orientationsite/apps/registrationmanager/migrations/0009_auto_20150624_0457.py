# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmanager', '0008_auto_20150624_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='confirmation',
        ),
        migrations.AddField(
            model_name='profile',
            name='stripe_id',
            field=models.CharField(default=b'', max_length=200, null=True),
        ),
    ]
