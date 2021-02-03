from django.urls import path
from . import views


urlpatterns = [
    # path(<urlpath_in_address_bar>, <views.py_file.FunctionName>, <name = name_mentioned_in_html_page>)

    # anything with 'listings/' will lead to 'index' method in views.py of listings app
    path('', views.index, name='listings'),

    # anything with 'listings/listing_id' will lead to 'listing' method in views.py of listings app
    path('<int:listing_id>', views.listing, name='listing'),

    # anything with 'listings/search' will lead to 'search' method in views.py of listings app
    path('search', views.search, name='search'),
]
