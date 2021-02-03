from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    # To display multiple fields on listing admin page as Table view
    list_display = (
        'id',
        'title',
        'is_published',
        'price',
        'list_date',
        'realtor'
    )

    # To make 'id' and 'title' Clickable on the above list.
    # By default only first given field is clickable
    list_display_links = ('id', 'title')

    # To filter list by 'realtor' field
    list_filter = ('realtor',)

    # To make given fields editable on above table view list
    list_editable = ('is_published',)

    # Search bar for searching in given fields
    search_fields = (
        'title',
        'description',
        'address',
        'city',
        'state',
        'zipcode',
        'price',
    )

    list_per_page = 25

    # Register your models here.
admin.site.register(Listing, ListingAdmin)
