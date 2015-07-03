from django.shortcuts import render
# from .apps.registrationmanager.forms import ProfileForm
from django.conf import settings
import stripe 
from django.contrib.auth.decorators import login_required
from orientationsite.apps.registrationmanager import forms
from orientationsite.apps.registrationmanager.models import Profile
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, "orientationsite/index.html", {})
def info(request):
    return render(request, "orientationsite/info.html", {})
def schedule(request):
    return render(request, "orientationsite/schedule.html", {})
def team(request):
    return render(request, "orientationsite/team.html", {})
def media(request):
    return render(request, "orientationsite/media.html", {})
def contact(request):
    return render(request, "orientationsite/contact.html", {})
def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def register(request):
    try:
        profile = Profile.objects.get(email=request.user.email)
        p_e = True
    except ObjectDoesNotExist:
       p_e = False
       profile = 'Fuck'
    return render(request, "orientationsite/register.html", {'p_e': p_e, 'profile': profile})

@login_required
def regform(request):

    request.session['old_post'] = request.POST
    pform = forms.ProfileForm(request.user, data=request.session['old_post'])

    print 'WASSSSSSSSSSSSUP!!!!!!!!'
    print request.method

    if request.method == "POST":

        print str(pform.is_valid())

    if pform.is_valid():

        print request.session['old_post']

        curr_user = request.user
        profile = pform.save(curr_user)
        # profile.user = request.user
        # profile.save(curr_user)

    return render(request, "regform.html", {'pform': pform, 'reqmet': request.method})

def stripeIdGenerator(user):

    stripe.api_key = settings.STRIPE_SECRET_KEY
    u_p = user.profile
    
    if u_p.stripe_id is None or u_p.stripe_id == '':
        print ' WAAAAAAAAAAA'
        new_stripe_id = stripe.Customer.create(email=user.email)
        u_p.stripe_id = new_stripe_id['id']
        user.profile.save()

@login_required
def confirmation(request):

    stripeIdGenerator(request.user)
    stripe_id = request.user.profile.stripe_id
    request.user.profile.save()
    return render(request, "orientationsite/accounts/confirmation.html", {"stripe_id" : stripe_id})





















# def register(request):
#     # form = ProfileForm(request.POST or None)

#     if form.is_valid():
#     publishKey = settings.STRIPE_PUBLISHABLE_KEY
#     context = {'publishKey': publishKey}
#     template = 'orientationsite/register.html'

#     if request.method == 'POST':
#     token = request.POST.get('stripeToken')
#     # Create the charge on Stripe's servers - this will charge the user's card
#     try:
#       charge = stripe.Charge.create(
#           amount=10000000, # amount in cents, again
#           currency="cad",
#           source=token,
#           description="Example charge"
#           )
#     except stripe.error.CardError, e:
#       # The card has been declined
#       pass

#     save_it = form.save(commit=False)
#     save_it.save()

#     return render(request, "orientationsite/register.html", {'form': form})



