from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    # list_filter = ['auction', 'created_at']
    list_display = ['id', 'description', 'price', 'created_date', 'auction', 'update_date', 'get_html_image']
    list_filter = ['auction', 'created_at', 'update_at']

admin.site.register(Advertisements, AdvertisementAdmin)


# Register your models here.
