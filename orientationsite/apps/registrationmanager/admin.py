from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django import forms

from . import models
import time

# Register your models here.

def paid(modeladmin, request, queryset):
	queryset.update(paid=True)
	queryset.update(paid_date=time.strftime("%d/%m/%Y"))

def check_in(modeladmin, request, queryset):
	queryset.update(checked_in=True)

def check_out(modeladmin, request, queryset):
	queryset.update(checked_in=False)

check_in.short_description = "Check in selected person(s)"
check_out.short_description = "Check out selected person(s)"

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = models.Profile

class UserProfileAdmin(UserAdmin):
    form = UserChangeForm
    inlines = [ UserProfileInline, ]

@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(User, UserAdmin)
































# class PersonCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""

#     # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = models.Person
#         exclude = ['']


#     # def clean_password2(self):
#     #     # Check that the two password entries match
#     #     password1 = self.cleaned_data.get("password1")
#     #     password2 = self.cleaned_data.get("password2")
#     #     if password1 and password2 and password1 != password2:
#     #         raise forms.ValidationError("Passwords don't match")
#     #     return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(PersonCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class PersonChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = models.Person
#         exclude = ['personid', 'reg_date', 'paid', 'paid_date', 'confirmation', 'checked_in', 'house', 'role', 'user','is_active', 'last_login']


#     # def clean_password(self):
#     #     # Regardless of what the user provides, return the initial value.
#     #     # This is done here, rather than on the field, because the
#     #     # field does not have access to the initial value
#     #     return self.initial["password"]


# class PersonAdmin(UserAdmin):
#     # The forms to add and change user instances
#     form = PersonChangeForm
#     add_form = PersonCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('first_name', 'last_name', 'email', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('first_name', 'last_name',)}),
#         ('Personal info', {'fields': ( 'gender', 'dob', 'shirt_size', 'program', 'commuter', 'home_phone', 'cell_phone', 'dietary_rest', 'allergies', 'accessibility', 'emerg_contact_first_name', 'emerg_contact_last_name', 'emerg_contact_phone', 'emerg_contact_email', 'emerg_contact_relation',  'offering_billet', 'requesting_billet', 'permission_to_diclose', 'reg_date', 'paid', 'paid_date', 'confirmation', 'checked_in','email',)}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'dob', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


# Now register the new UserAdmin...
# admin.site.register(models.Person, PersonAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
