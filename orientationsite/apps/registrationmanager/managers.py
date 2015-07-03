# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class ProfileManager(models.Manager):
	
    def get_active_members(self):
        """
        GET EVERYONE WHO IS ACTIVE.
        """
        return self.filter(is_active=True)


class HouseManager(models.Manager):
	pass

class RoleManager(models.Manager):
	pass




























    

# class PersonManager(BaseUserManager):

#     def create_user(self, first_name, last_name, email, home_phone, cell_phone, dob, dietary_rest, allergies, accessibility, gender, emerg_contact_first_name, emerg_contact_last_name, emerg_contact_phone, emerg_contact_email, emerg_contact_relation, commuter, offering_billet, requesting_billet, shirt_size, program, permission_to_diclose, reg_date, paid, paid_date, confirmation, checked_in, password):
#         """
#         Creates and saves a User with the given info.
#         """

#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#         	first_name = first_name,
#         	last_name = last_name,
#         	email = self.normalize_email(email),
#         	home_phone = home_phone,
#         	cell_phone = cell_phone,
#         	dob = dob,
#         	dietary_rest = dietary_rest,
#         	allergies = allergies,
#         	accessibility = accessibility,
#         	gender = gender,
#         	emerg_contact_first_name = emerg_contact_first_name,
#         	emerg_contact_last_name = emerg_contact_last_name,
#         	emerg_contact_phone = emerg_contact_phone,
#         	emerg_contact_email = emerg_contact_email,
#         	emerg_contact_relation = emerg_contact_relation,
#             commuter = commuter, 
#         	offering_billet = offering_billet,
#         	requesting_billet = requesting_billet,
#         	shirt_size = shirt_size,
#         	program = program,
#         	permission_to_diclose = permission_to_diclose,
#         	reg_date = self.getreg_date,
#         	paid = paid,
#         	paid_date = paid_date,
#         	confirmation = confirmation,
#         	checked_in = checked_in,
#             password = password, 
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, first_name, last_name, email, home_phone, cell_phone, dob, dietary_rest, allergies, accessibility, gender, emerg_contact_first_name, emerg_contact_last_name, emerg_contact_phone, emerg_contact_email, emerg_contact_relation, commuter, offering_billet, requesting_billet, shirt_size, program, permission_to_diclose, reg_date, paid, paid_date, confirmation, checked_in, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
# 			first_name = first_name,
#         	last_name = last_name,
#         	email = self.normalize_email(email),
#         	home_phone = home_phone,
#         	cell_phone = cell_phone,
#         	dob = dob,
#         	dietary_rest = dietary_rest,
#         	allergies = allergies,
#         	accessibility = accessibility,
#         	gender = gender,
#         	emerg_contact_first_name = emerg_contact_first_name,
#         	emerg_contact_last_name = emerg_contact_last_name,
#         	emerg_contact_phone = emerg_contact_phone,
#         	emerg_contact_email = emerg_contact_email,
#         	emerg_contact_relation = emerg_contact_relation,
#             commuter = commuter,
#         	offering_billet = offering_billet,
#         	requesting_billet = requesting_billet,
#         	shirt_size = shirt_size,
#         	program = program,
#         	permission_to_diclose = permission_to_diclose,
#         	reg_date = reg_date,
#         	paid = paid,
#         	paid_date = paid_date,
#         	confirmation = confirmation,
#         	checked_in = checked_in,
#             password = password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
