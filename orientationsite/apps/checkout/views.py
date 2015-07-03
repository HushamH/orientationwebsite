from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
from orientationsite.apps.registrationmanager.models import Profile


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):

	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	print request.method
	if request.method == "POST" and 'stripeToken' in request.POST.keys():

		token = request.POST['stripeToken']
		print token

		try:
		    profile = Profile.objects.get(email=request.user.email)
		    new_stripe_id = stripe.Customer.create(email=request.user.email)
		    customer = stripe.Customer.retrieve(new_stripe_id['id'])
		    customer.sources.create(source=token)
		    profile.stripe_id = new_stripe_id['id']
		    charge = stripe.Charge.create(
		        amount=100000, # amount in cents, again
		        currency="cad",
		        customer=customer.id,
		        description="Example charge"
		    )
		    profile.paid = True
		    profile.save()


		except stripe.error.CardError, e:
			# The card has been declined
			pass

	context = {'publishKey': publishKey,  'reqmet': request.method}
	template = 'orientationsite/checkout.html'
	return render(request, template, context)

