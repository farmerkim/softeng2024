# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostCreate

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # 블로그 홈
    path('post/<int:id>/', views.single_post, name='single_post'),
     path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('create/', PostCreate.as_view(), name='create_post'),
    path('search/', views.search, name='search'),
    path('home/', views.home, name='home'),
    path('tag/', views.tag_page, name='tag_page'),
    path('category/<str:slug>/', views.category_page),
    path('no-category/', views.no_category, name='no_category'),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view())
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)