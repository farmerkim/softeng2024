from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # index 페이지
    path('post/<int:pk>/', views.single_post_page, name='single_post_page'),  # 개별 포스트 페이지
    path('blog/', views.blog_page, name='blog_page'),  # blog_page 추가
]
