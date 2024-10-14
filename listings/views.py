from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.gis import forms
from .models import Listing


def listing_list(request):
    sort_by = request.GET.get('sort', '-list_date')  # Default to newest first

    if sort_by not in ['-price', 'price', '-list_date', 'list_date']:
        sort_by = '-list_date'  # If an invalid sort option is provided, default to newest first

    listings = Listing.objects.filter(is_published=True).order_by(sort_by)

    paginator = Paginator(listings, 10)  # Show 10 listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'current_sort': sort_by
    }
    return render(request, 'listings/listing_list.html', context)


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    photos = listing.photos.all()
    return render(request, 'listings/listing_detail.html', {'listing': listing, 'photos': photos})
