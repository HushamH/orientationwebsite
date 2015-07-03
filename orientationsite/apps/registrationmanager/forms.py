from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Profile

class ProfileForm(forms.ModelForm):

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(ProfileForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Profile
		exclude = ['reg_date', 'paid', 'paid_date', 'confirmation', 'checked_in', 'house', 'role', 'associated_user', 'stripe_id', 'email']

	def save(self, user):

		profile = Profile.objects.get_or_create(associated_user=user)[0]
		profile.first_name = self.cleaned_data['first_name']
		print profile.first_name
		profile.last_name = self.cleaned_data['last_name']
		profile.email = user.email
		profile.home_phone = self.cleaned_data['home_phone']
		profile.cell_phone = self.cleaned_data['cell_phone']
		profile.dietary_rest = self.cleaned_data['dietary_rest']
		profile.allergies = self.cleaned_data['allergies']
		profile.accessibility = self.cleaned_data['accessibility']
		profile.gender = self.cleaned_data['gender']
		profile.emerg_contact_first_name = self.cleaned_data['emerg_contact_first_name']
		profile.emerg_contact_last_name = self.cleaned_data['emerg_contact_last_name']
		profile.emerg_contact_phone = self.cleaned_data['emerg_contact_phone']
		profile.emerg_contact_email = self.cleaned_data['emerg_contact_email']
		profile.emerg_contact_relation = self.cleaned_data['emerg_contact_relation']
		profile.commuter = self.cleaned_data['commuter']
		profile.offering_billet = self.cleaned_data['offering_billet']
		profile.requesting_billet = self.cleaned_data['requesting_billet']
		profile.shirt_size = self.cleaned_data['shirt_size']
		profile.program = self.cleaned_data['program']
		profile.save()
		return profile























# class PersonForm(forms.ModelForm):

# 	def signup(self, request, user):
# 		user.first_name = self.cleaned_data['first_name']
# 		user.email = self.cleaned_data['email']
# 		u_p = user.Profile
# 		u_p.first_name = self.cleaned_data['first_name']
# 		u_p.email = self.cleaned_data['email']
# 		user.save()
# 		u_p.save()

# 	class Meta:
# 		model = Person
# 		exclude = ['personid', 'reg_date', 'paid', 'paid_date', 'confirmation', 'checked_in', 'house', 'role', 'user']


