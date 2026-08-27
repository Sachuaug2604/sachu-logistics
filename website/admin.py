from django.contrib import admin
from .models import Shipment


@admin.register(Shipment)
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