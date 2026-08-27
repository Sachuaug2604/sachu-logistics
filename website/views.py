from django.shortcuts import render, get_object_or_404
from .models import Shipment


def home(request):
    return render(request, 'website/home.html')


def track_shipment(request):
    shipment = None
    tracking_number = request.GET.get('tracking_number')

    if tracking_number:
        shipment = get_object_or_404(
            Shipment,
            tracking_number=tracking_number.strip()
        )

    status_steps = [
        ('ORDER_RECEIVED', 'Order Received'),
        ('PICKED_UP', 'Picked Up'),
        ('IN_TRANSIT', 'In Transit'),
        ('AT_HUB', 'Arrived at Hub'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
    ]

    current_step = -1

    if shipment:
        for index, (code, name) in enumerate(status_steps):
            if code == shipment.status:
                current_step = index
                break

    return render(
        request,
        'website/track.html',
        {
            'shipment': shipment,
            'tracking_number': tracking_number,
            'status_steps': status_steps,
            'current_step': current_step,
        }
    )