from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 객체가 없을 때 404 에러를 발생시킵니다.
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )

def blog_page(request):  # blog_page 함수 추가
    posts = Post.objects.all().order_by('-pk')  # 예시로 전체 포스트를 불러옴

    return render(
        request,
        'blog/blog_page.html',  # blog_page 템플릿을 사용
        {
            'posts': posts,
        }
    )
