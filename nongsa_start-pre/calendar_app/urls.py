from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('', views.index, name='index_page'),
    path('save_event/', views.save_event, name='save_event'),
]
