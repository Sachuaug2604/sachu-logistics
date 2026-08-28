from django.db import models


class Shipment(models.Model):

    STATUS_CHOICES = [
        ('ORDER_RECEIVED', 'Order Received'),
        ('PICKED_UP', 'Picked Up'),
        ('IN_TRANSIT', 'In Transit'),
        ('AT_HUB', 'Arrived at Hub'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
    ]

    tracking_number = models.CharField(
        max_length=20,
        unique=True
    )

    sender_name = models.CharField(max_length=100)

    receiver_name = models.CharField(max_length=100)

    origin = models.CharField(max_length=100)

    destination = models.CharField(max_length=100)

    current_location = models.CharField(max_length=100)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='ORDER_RECEIVED'
    )

    package_description = models.CharField(
        max_length=200,
        blank=True
    )

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    estimated_delivery = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.tracking_number


class TrackingUpdate(models.Model):

    shipment = models.ForeignKey(
        Shipment,
        on_delete=models.CASCADE,
        related_name='tracking_updates'
    )

    status = models.CharField(
        max_length=30,
        choices=Shipment.STATUS_CHOICES
    )

    location = models.CharField(
        max_length=100
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    timestamp = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.shipment.tracking_number} - {self.get_status_display()}"