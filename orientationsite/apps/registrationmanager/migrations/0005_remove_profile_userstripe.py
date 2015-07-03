# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmanager', '0004_auto_20150620_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='userStripe',
        ),
    ]
