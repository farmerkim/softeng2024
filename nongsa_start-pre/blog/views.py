from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag
from .forms import PostForm
from django.views.generic import ListView

# Index 페이지 - 최근 포스트 목록을 보여줍니다.
def index(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신 게시글 순 정렬
    categories = Category.objects.all()
    no_category_post_count = Post.objects.filter(category=None).count()

    return render(
        request,
        'blog/blog_home.html',
        {
            'posts': posts,
            'categories': categories,
            'no_category_post_count': no_category_post_count,
        }
    )
# 단일 포스트 보기 - ID 기반
def single_post(request, id):
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.all()
    no_category_post_count = Post.objects.filter(category=None).count()

    return render(
        request,
        'blog/single_post.html',
        {
            'post': post,
            'categories': categories,
            'no_category_post_count': no_category_post_count,
        }
    )
def simple_page(request, template_name):
    return render(request, template_name)

# 단순 페이지들
def home(request):
    return simple_page(request, 'blog/home.html')
# 클래스 기반 뷰 - 포스트 목록
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 포스트 생성 페이지
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# 포스트 상세 보기
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 카테고리와 관련된 데이터 포함
def category_page(request, slug):
    if slug == 'no_category':
        category = None
        post_list = Post.objects.filter(category=None)  # 미분류 포스트
    else:
        category = get_object_or_404(Category, slug=slug)
        post_list = Post.objects.filter(category=category)  # 선택된 카테고리의 포스트

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )
# 미분류 포스트 페이지
def no_category(request):
    post_list = Post.objects.filter(categories=None)  # 미분류 포스트
    return render(request, 'blog/no_category.html', {'post_list': post_list})

# 태그 목록 페이지
def tag_page(request):
    post_list = Post.objects.all()
    tags = Tag.objects.all()  # 전체 태그 가져오기
    
    return render(
        request,
        'blog/blog_home.html',
        {
            'post_list': post_list,
            'tags': tags,  # 태그 전체 목록 전달
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count()
        }
    )