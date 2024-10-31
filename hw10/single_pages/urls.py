from django.urls import path
from . import views

app_name = "single_pages"

urlpatterns = [
    path('about_me/', views.about_crop, name='about_crop_page'),
    path('', views.index, name='index_page'),
    path('blog/', views.blog, name='blog_page'),
    path('crop_yield_meter/', views.crop_yield_meter, name='crop_yield_meter_page'),
]
