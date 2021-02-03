from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# bedroom_choices, price_choices, state_choices are Dictionaries
# To provide choice value in search form in index.html
from listings.choices import bedroom_choices, price_choices, state_choices


from .models import Listing


def index(request):
    # GET Listing property values
    # order by list_date in desc order '-' is used for desc
    # filter() --> Only get data with 'is_published' as True value
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Fecth only 3 rows from database and display per page
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # Dict format paged_listings
    context = {
        'listings': paged_listings
    }

    # Pass the dict format listings to front-end
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # get_object_or_404 -> Fetch the object values or 404 page if doesn't exist
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keyword Search
    if 'keywords' in request.GET:
        # From search.html page
        # <input type="text" name="keywords" class="form-control" placeholder="Keyword (Pool, Garage, etc)">
        # <<<< name value is "keywords" >>>>
        keywords = request.GET['keywords']
        if keywords:
            # description__icontains -> Used to search of a keyword in whole paragraph
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City Keyword
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # iexact -> Case insensitive | exact -> Case sensitive
            queryset_list = queryset_list.filter(city__iexact=city)

    # State Keyword
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # iexact -> Case insensitive | exact -> Case sensitive
            queryset_list = queryset_list.filter(state__iexact=state)

    # bedrooms Keyword
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__exact=bedrooms)

    # price Keyword
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # lte -> less than or equal to
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'searched_values': request.GET,
    }

    return render(request, 'listings/search.html', context)
