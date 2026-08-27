from django.contrib import admin
from .models import Shipment

admin.site.site_header = "Sachu Logistics"
admin.site.site_title = "Sachu Logistics"
admin.site.index_title = "Sachu Logistics Dashboard"

admin.site.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):

    list_display = (
        'tracking_number',
        'sender_name',
        'receiver_name',
        'origin',
        'destination',
        'current_location',
        'status',
        'estimated_delivery',
    )

    list_filter = (
        'status',
        'origin',
        'destination',
    )

    search_fields = (
        'tracking_number',
        'sender_name',
        'receiver_name',
        'origin',
        'destination',
        'current_location',
    )

    ordering = ('-created_at',)