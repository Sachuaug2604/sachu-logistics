from django.shortcuts import render
from .models import Shipment


def home(request):
    return render(request, 'website/home.html')


def track_shipment(request):
    shipment = None
    tracking_number = request.GET.get('tracking_number')

    if tracking_number:
        shipment = Shipment.objects.filter(
            tracking_number__iexact=tracking_number.strip()
        ).first()

    status_steps = [
        ('ORDER_RECEIVED', 'Order Received'),
        ('PICKED_UP', 'Picked Up'),
        ('IN_TRANSIT', 'In Transit'),
        ('AT_HUB', 'Arrived at Hub'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
    ]

    current_step = -1
    tracking_updates = []

    if shipment:
        # Get the latest tracking update
        tracking_updates = shipment.tracking_updates.all().order_by('-timestamp')

        # Use the latest tracking update as the current status
        if tracking_updates.exists():
            latest_update = tracking_updates.first()
            current_status = latest_update.status
        else:
            current_status = shipment.status

        # Find the current step in the timeline
        for index, (code, name) in enumerate(status_steps):
            if code == current_status:
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
            'tracking_updates': tracking_updates,
        }
    )