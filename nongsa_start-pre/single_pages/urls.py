from django.urls import include, path
from . import views

app_name = "single_pages"

urlpatterns = [
    path('', views.index, name='index_page'),
    path('crop_yield_meter/', views.crop_yield_meter_view, name='crop_yield_meter'),
    path('sensors/', views.sensor_view, name='sensor_view'),
    path('greenhouse_reservation/', views.greenhouse_reservation, name='greenhouse_reservation'),
    path('customer_center/', views.customer_center, name='customer_center'),
]
