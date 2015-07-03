# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import orientationsite.apps.registrationmanager.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('building', models.CharField(max_length=2, choices=[(b'M', b'Morrison'), (b'W', b'Whitney'), (b'SD', b'Sir Daniel Wilson')])),
                ('cap', models.IntegerField()),
                ('don_name', models.CharField(max_length=50)),
                ('don_phone', models.CharField(max_length=30)),
                ('don_email', models.EmailField(max_length=254)),
                ('number_of_spare_rooms', models.IntegerField(blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'House',
                'verbose_name_plural': 'Houses',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=30)),
                ('last_name', models.CharField(default=b'', max_length=30)),
                ('email', models.EmailField(default=b'1@1.com', max_length=254, verbose_name=b'Your email address')),
                ('home_phone', models.CharField(default=b'', max_length=30, verbose_name=b'Home phone number')),
                ('cell_phone', models.CharField(default=b'', max_length=30, verbose_name=b'Cell phone number')),
                ('dob', models.DateField(auto_now=True, verbose_name=b'Date of Birth')),
                ('dietary_rest', models.CharField(default=b'', max_length=100, verbose_name=b'Select any dietary restrictions you may have')),
                ('allergies', models.CharField(default=b'', max_length=100, verbose_name=b'List any allergies you may have')),
                ('accessibility', models.CharField(default=b'', max_length=100, verbose_name=b'Describe any accessibility issues you may have')),
                ('gender', models.CharField(default=b'', max_length=100, verbose_name=b'Specify your gender')),
                ('emerg_contact_first_name', models.CharField(default=b'', max_length=30, verbose_name=b'The first name of your emergency contact')),
                ('emerg_contact_last_name', models.CharField(default=b'', max_length=30, verbose_name=b'The last name of your emergency contact')),
                ('emerg_contact_phone', models.CharField(default=b'', max_length=30, verbose_name=b'The phone number of your emergency contact')),
                ('emerg_contact_email', models.EmailField(default=b'1@1.com', max_length=254, null=True, verbose_name=b'The e-mail address of your emergency contact', blank=True)),
                ('emerg_contact_relation', models.CharField(default=b'', max_length=30, verbose_name=b'Your relationship with the emergency contact', blank=True)),
                ('commuter', models.CharField(default=b'', max_length=4, verbose_name=b'Your school year living situation', choices=[(b'res', b'I will be living in university residence during the school year as of September 2015.'), (b'comm', b'I will NOT be living in university residence during the school year as of September 2015.')])),
                ('offering_billet', models.NullBooleanField(default=b'', verbose_name=b'<strong>**IF YOU ARE LIVING IN RESIDENCE**</strong> Would you like to host a commuter in your room?')),
                ('requesting_billet', models.NullBooleanField(default=b'', verbose_name=b'<strong>**IF YOU ARE PLANNING TO COMMUTE**</strong> Would you like to stay with a frosh on residence?')),
                ('shirt_size', models.CharField(default=b'', max_length=3, choices=[(b'S', b'Small (36 inch chest)'), (b'M', b'Medium (38 inch chest)'), (b'L', b'Large (40 inch chest)'), (b'XL', b'Extra Large (42 inch chest)'), (b'XXL', b'Extra-Extra Large (44 inch chest)')])),
                ('program', models.CharField(default=b'', max_length=20, choices=[(b'compsci', b'Computer Science'), (b'lifesci', b'Life Sciences'), (b'humanities', b'Humanities'), (b'soc', b'Social Sciences'), (b'rot', b'Rotman Commerce'), (b'phymat', b'Physics and Math (Applied Sciences)'), (b'arch', b'Architecture'), (b'eng', b'Engineering'), (b'kin', b'Kinesiology')])),
                ('reg_date', models.DateField(auto_now=True, null=True)),
                ('paid', models.NullBooleanField(default=False)),
                ('paid_date', models.DateField(auto_now=True, null=True)),
                ('confirmation', models.CharField(default=b'', max_length=100)),
                ('checked_in', models.NullBooleanField(default=False)),
                ('house', models.ForeignKey(related_name='house', verbose_name=b'House', blank=True, to='registrationmanager.House', null=True)),
            ],
            options={
                'ordering': ['last_name'],
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=2, choices=[(b'F', b'Frosh'), (b'L', b'Leader'), (b'HL', b'Head Leader'), (b'E', b'Exec'), (b'CC', b'Co-Chair')])),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(related_name='role', default=orientationsite.apps.registrationmanager.models.get_frosh_object, verbose_name=b'Role', to='registrationmanager.Role', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
