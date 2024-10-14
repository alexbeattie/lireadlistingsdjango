from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils import timezone  # Add this line


ISLAND_TYPES = (
    ('Salt Spring Island', 'Salt Spring Island'),
    ('Vancouver Island', 'Vancouver Island'),
    ('Mayne Island', 'Mayne Island'),
    ('Galiano Island', 'Galiano Island'),
)
island = models.CharField(max_length=100, choices=ISLAND_TYPES)

VIEW_TYPES = (
    ('Oceanfront', 'Oceanfront'),
    ('Oceanview', 'Oceanview'),
    ('Residential', 'Residential'),
    ('Land', 'Land'),
    ('Non Ocean View', 'Non Ocean View'),
    ('Commercial', 'Commercial'),
)
view_type = models.CharField(max_length=100, choices=VIEW_TYPES)

PROPERTY_TYPES = (
    ('House', 'House'),
    ('Apartment', 'Apartment'),
    ('Land', 'Land'),
    ('Commercial', 'Commercial'),
)
property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please upload a PDF file.')


def validate_video_or_matterport_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError("Please enter a valid URL.")

    # Check if the URL is from YouTube, Vimeo, or Matterport
    if ("youtube.com" not in value.lower() and
            "vimeo.com" not in value.lower() and
            "my.matterport.com" not in value.lower()):
        raise ValidationError("Please enter a valid YouTube, Vimeo, or Matterport URL.")

class Listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    is_published = models.BooleanField()
    list_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    realtor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='listings/', null=True, blank=True)
    floor_plan_one = models.FileField(upload_to='floor_plans/', null=True, blank=True)
    floor_plan_two = models.FileField(upload_to='floor_plans/', null=True, blank=True)
    maps_plan = models.FileField(upload_to='maps_plans/', null=True, blank=True)
    video_or_3d_tour = models.URLField(max_length=255, null=True, blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)
    zipcode = models.CharField(max_length=20, default='')
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    island = models.CharField(max_length=100, choices=ISLAND_TYPES)
    view_type = models.CharField(max_length=100, choices=VIEW_TYPES)

    def __str__(self):
        return self.title

class Photo(models.Model):
    listing = models.ForeignKey(Listing, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listing_photos/')
    description = models.CharField(max_length=200, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.listing.title}"
