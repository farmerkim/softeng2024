from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

# Index 페이지 - 최근 포스트 목록을 보여줍니다.
def index(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신 게시글을 가져오기 위해 정렬
    return render(request, 'blog/index.html', {'posts': posts})

def single_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/single_post.html', {'post': post})

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog(request):
    return render(request, 'blog/blog.html')