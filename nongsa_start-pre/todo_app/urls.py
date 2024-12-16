from django.urls import path
from . import views

app_name = 'todo'  # 네임스페이스 설정

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('<int:list_id>/', views.ItemListView.as_view(), name='list'),
    path('add/', views.ListCreate.as_view(), name='list-add'),  # list-add URL
    path('<int:list_id>/item/add/', views.ItemCreate.as_view(), name='item-add'),
    path('<int:list_id>/item/<int:pk>/', views.ItemUpdate.as_view(), name='item-update'),
    path('<int:pk>/delete/', views.ListDelete.as_view(), name='list-delete'),
    path('<int:list_id>/item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
]
