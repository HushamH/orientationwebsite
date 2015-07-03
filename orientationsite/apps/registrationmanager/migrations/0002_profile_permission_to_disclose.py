# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='permission_to_disclose',
            field=models.BooleanField(default=False, verbose_name=b'I agree to disclose this information to my leaders in the case of emergencies.'),
        ),
    ]
