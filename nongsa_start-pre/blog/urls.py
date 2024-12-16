from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('post/<int:id>/', views.single_post, name='single_post'),
    path('home/', views.home, name='home'),
    path('category/<str:slug>/', views.category_page),
    path('no-category/', views.no_category, name='no_category'),
    path('tag/', views.tag_page, name='tag_page'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)