from django.db import models
from . import managers
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
# UNDO THIS
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

# Create your models here.

def get_frosh_object():
	try: 
		return Role.roles.filter(id=1)[0]	
	except IndexError:
		return None;

class Profile(models.Model):

	# def create_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Profile.objects.create(user=instance)
	
	# post_save.connect(create_user_profile, sender=User)
	objects = managers.ProfileManager()
	# Relations

	house = models.ForeignKey(
		'House',
		related_name = "house",
		verbose_name = "House",
		null=True,
		blank=True,
		)

	role = models.ForeignKey(
		'Role', 
		related_name = "role",
		verbose_name = "Role",
		default=get_frosh_object,
		null=True
		)

	associated_user = models.OneToOneField(User,
		related_name="user",
		unique=True,
		null=True,
		blank=True,
		)

	# Attributes - Mandatory

	COMMUTER_CHOICES = (
		('res', 'I will be living in university residence during the school year as of September 2015.'),
		('comm', 'I will NOT be living in university residence during the school year as of September 2015.'),
		)

	SHIRT_CHOICES = (
		('S', 'Small (36 inch chest)'),
		('M', 'Medium (38 inch chest)'),
		('L', 'Large (40 inch chest)'),
		('XL', 'Extra Large (42 inch chest)'),
		('XXL', 'Extra-Extra Large (44 inch chest)'),
		)

	PROGRAM_CHOICES = (
		('compsci', 'Computer Science'),
		('lifesci', 'Life Sciences'),
		('humanities', 'Humanities'),
		('soc', 'Social Sciences'),
		('rot', 'Rotman Commerce'),
		('phymat', 'Physics and Math (Applied Sciences)'),
		('arch', 'Architecture'),
		('eng', 'Engineering'),
		('kin', 'Kinesiology'),
		)

	first_name = models.CharField(max_length=30, default='')
	last_name = models.CharField(max_length=30, default='')
	email = models.EmailField(verbose_name='Your email address', default='1@1.com')
	home_phone = models.CharField(max_length=30, verbose_name='Home phone number', default='')
	cell_phone = models.CharField(max_length=30, verbose_name='Cell phone number', default='')
	dob = models.DateField(verbose_name='Date of Birth', auto_now=True, blank=True)
	# Fix the form so that they choose out of a list and have an option for other.
	dietary_rest = models.CharField(max_length=100, verbose_name='Select any dietary restrictions you may have', default='')
	allergies = models.CharField(max_length=100, verbose_name='List any allergies you may have', default='')
	accessibility = models.CharField(max_length=100, verbose_name='Describe any accessibility issues you may have', default='')
	# Fix the form so that they choose out of a list and have an option for other.
	gender = models.CharField(max_length=100, verbose_name='Specify your gender', default='')
	emerg_contact_first_name = models.CharField(max_length=30, verbose_name='The first name of your emergency contact', default='')
	emerg_contact_last_name = models.CharField(max_length=30, verbose_name='The last name of your emergency contact', default='')
	emerg_contact_phone = models.CharField(max_length=30, verbose_name='The phone number of your emergency contact', default='')
	emerg_contact_email = models.EmailField(verbose_name='The e-mail address of your emergency contact',blank=True, default='1@1.com', null=True)
	emerg_contact_relation = models.CharField(max_length=30, verbose_name='Your relationship with the emergency contact', default='', blank=True)
	commuter = models.CharField(max_length=4, choices=COMMUTER_CHOICES, verbose_name='Your school year living situation', default='')
	offering_billet = models.NullBooleanField(blank=True, verbose_name="<strong>**IF YOU ARE LIVING IN RESIDENCE**</strong> Would you like to host a commuter in your room?",default='', null=True)
	requesting_billet = models.NullBooleanField("<strong>**IF YOU ARE PLANNING TO COMMUTE**</strong> Would you like to stay with a frosh on residence?",default='', null=True)
	shirt_size = models.CharField(max_length=3, choices=SHIRT_CHOICES, default='')
	program = models.CharField(max_length=20, choices=PROGRAM_CHOICES, default='')

	reg_date = models.DateField(auto_now=True, null=True)
	paid = models.NullBooleanField(default=False, null=True)
	paid_date = models.DateField(auto_now=True, null=True)
	# payment method
	# invoice number
	# dietary restrictions should be able to filter ones with it, or search by, same for accesssibility
	# communications leader and head leaders to house
	stripe_id = models.CharField(max_length=200, default='', null=True)
	checked_in = models.NullBooleanField(default=False, null=True)

	# Attributes - Optional
	# Object Manager

	people = managers.ProfileManager()

	# Custom Properties
	# Methods
	# Meta and String

	class Meta:
		verbose_name = "profile"
		verbose_name_plural = "profiles"
		ordering = ['last_name']

	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)

class House(models.Model):

	# Relations

	# Attributes - Mandatory

	BUILDING_CHOICES = (
		('M', 'Morrison'),
		('W', 'Whitney'),
		('SD', 'Sir Daniel Wilson'),
		)

	name = models.CharField(max_length=20)
	building = models.CharField(max_length=2, choices=BUILDING_CHOICES)
	cap = models.IntegerField()
	don_name = models.CharField(max_length=50)
	don_phone = models.CharField(max_length=30)
	don_email = models.EmailField()
	number_of_spare_rooms = models.IntegerField(blank=True)

	# Attributes - Optional
	# Object Manager

	houses = managers.HouseManager()

	# Custom Properties
	# Methods
	# Meta and String

	class Meta:
		verbose_name = "House"
		verbose_name_plural = "Houses"
		ordering = ['name']

	def __str__(self):
		return "%s" % (self.name)


class Role(models.Model):

	# Relations

	# Attributes - Mandatory

	TITLE_CHOICES = (
		('F', 'Frosh'),
		('L', 'Leader'),
		('HL', 'Head Leader'),
		('E', 'Exec'),
		('CC', 'Co-Chair'),
		)

	title = models.CharField(max_length=2, choices=TITLE_CHOICES)

	# Attributes - Optional
	# Object Manager

	roles = managers.RoleManager()

	# Custom Properties
	# Methods
	# Meta and String

	class Meta:
		verbose_name = "Role"
		verbose_name_plural = "Roles"
		ordering = ['title']

	def __str__(self):
		return "%s" % (self.title)

