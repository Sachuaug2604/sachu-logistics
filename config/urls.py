from django.contrib import admin
from django.urls import path
from website.views import home, track_shipment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('track/', track_shipment, name='track_shipment'),
]