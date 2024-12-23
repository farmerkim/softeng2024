from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostCreate
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.single_post, name='single_post'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('create/', PostCreate.as_view(), name='create_post'),
    path('search/', views.search, name='search'),
    path('single_pages/', include('single_pages.urls')),
    path('tag/', views.tag_page, name='tag_page'),
    path('category/<str:slug>/', views.category_page, name='category_page'), 
    path('no-category/', views.no_category, name='no_category'),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='update_post'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
