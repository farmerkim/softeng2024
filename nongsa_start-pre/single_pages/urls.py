from django.urls import include, path
from . import views

app_name = "single_pages"

urlpatterns = [
    path('', views.index, name='index_page'),
]
