from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.utils.html import format_html


from .models import Listing, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ('image', 'description')

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('title', 'price', 'property_type', 'bedrooms', 'bathrooms', 'is_published', 'list_date', 'realtor', 'photo_count', 'main_image_preview')
    list_filter = ('is_published', 'realtor', 'property_type', 'island', 'view_type')
    search_fields = ('title', 'description', 'city', 'state', 'island')
    readonly_fields = ('list_date', 'main_image_preview')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'price', 'description', 'realtor')
        }),
        ('Property Details', {
            'fields': ('property_type', 'bedrooms', 'bathrooms')
        }),
        ('Location', {
            'fields': ('city', 'state', 'island', 'view_type')
        }),
        ('Images | Media', {
            'fields': ('main_image', 'main_image_preview', 'floor_plan_one', 'floor_plan_two', 'video_or_3d_tour')
        }),
        ('Publication', {
            'fields': ('is_published', 'list_date')
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    def photo_count(self, obj):
        return obj.photos.count()
    photo_count.short_description = 'Number of Photos'

    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.main_image.url)
        return "No image"
    main_image_preview.short_description = 'Main Image Preview'

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('listing', 'description', 'upload_date', 'image_preview')
    list_filter = ('upload_date',)  # Remove fields that don't exist in Photo model
    search_fields = ('listing__title', 'description')
    readonly_fields = ('upload_date', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Image Preview'