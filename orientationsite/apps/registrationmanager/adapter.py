from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class MyUserAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        # user.email = data.get('email')
        # user.username = data.get('username')
        # all your custom fields
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.home_phone = data.get('home_phone')
        user.cell_phone = data.get('cell_phone')
        user.dob = data.get('dob')
        user.dietary_rest = data.get('dietary_rest')
        user.allergies = data.get('allergies')
        user.accessibility = data.get('accessibility')
        user.gender = data.get('gender')
        user.emerg_contact_first_name = data.get('emerg_contact_first_name')
        user.emerg_contact_last_name = data.get('emerg_contact_last_name')
        user.emerg_contact_phone = data.get('emerg_contact_phone')
        user.emerg_contact_email = data.get('emerg_contact_email')
        user.emerg_contact_relation = data.get('emerg_contact_relation')
        user.commuter = data.get('commuter')
        user.offering_billet = data.get('offering_billet')
        user.requesting_billet = data.get('requesting_billet')
        user.program = data.get('program')
        user.permission_to_diclose = data.get('permission_to_diclose')
        user.reg_date = data.get('reg_date')
        user.paid = data.get('paid')
        user.paid_date = data.get('paid_date')
        user.confirmation = data.get('confirmation')
        user.checked_in = data.get('checked_in')
        user.password = data.get('password')

        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user