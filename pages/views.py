from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor

# bedroom_choices, price_choices, state_choices are Dictionaries
# To provide choice value in search form in index.html
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    # GET latest listings from Class Listings properties -> Indirectly from Database
    latest_listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': latest_listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # GET all realtors from Class Realtors properties -> Indirectly from Database
    realtors = Realtor.objects.order_by('-hire_date')

    # GET mvp realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
