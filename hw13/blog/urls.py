# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # 블로그 홈
    path('post/<int:id>/', views.single_post, name='single_post'),
    path('category/<str:slug>/', views.category_page),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('tag/', views.tag_page, name='tag_page'),
    path('no-category/', views.no_category, name='no_category'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)