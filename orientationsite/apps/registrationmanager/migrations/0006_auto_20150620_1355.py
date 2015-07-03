# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmanager', '0005_remove_profile_userstripe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstripe',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserStripe',
        ),
    ]
