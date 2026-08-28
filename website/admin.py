from django.contrib import admin
from .models import Shipment, TrackingUpdate


admin.site.site_header = "Sachu Logistics"
admin.site.site_title = "Sachu Logistics"
admin.site.index_title = "Sachu Logistics Dashboard"


class TrackingUpdateInline(admin.TabularInline):
    model = TrackingUpdate
    extra = 1
    ordering = ('-timestamp',)


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

    inlines = [TrackingUpdateInline]


@admin.register(TrackingUpdate)
class TrackingUpdateAdmin(admin.ModelAdmin):

    list_display = (
        'shipment',
        'status',
        'location',
        'description',
        'timestamp',
    )

    list_filter = (
        'status',
        'location',
    )

    search_fields = (
        'shipment__tracking_number',
        'location',
        'description',
    )

    ordering = ('-timestamp',)