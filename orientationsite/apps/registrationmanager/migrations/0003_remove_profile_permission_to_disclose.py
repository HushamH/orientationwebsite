# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmanager', '0002_profile_permission_to_disclose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='permission_to_disclose',
        ),
    ]
