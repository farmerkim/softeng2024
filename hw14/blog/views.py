from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from .models import Post, Category, Tag
from .forms import PostForm
from django.utils.text import slugify
from django.core.paginator import Paginator

def index(request):
    # post_list로 통일
    post_list = Post.objects.select_related('author', 'category').order_by('-created_at')
    print("Loaded posts:", post_list.count())

    # 페이지네이션 설정
    paginator = Paginator(post_list, 5)  # 한 페이지에 5개의 포스트 표시
    page_number = request.GET.get('page')  # 페이지 번호를 GET 파라미터에서 가져옴
    page_obj = paginator.get_page(page_number)

    # 템플릿 컨텍스트에 전달할 데이터
    return render(
        request,
        'blog/index.html',
        {
            'page_obj': page_obj,  # page_obj를 템플릿으로 전달
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'tags': Tag,
        }
    )

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

def post_delete(request, post_id):
    # 해당 포스트 가져오기
    post = get_object_or_404(Post, id=post_id)

    # 포스트 삭제
    post.delete()

    # 삭제 후 홈으로 리디렉션
    return redirect('blog:index')

def simple_page(request, template_name):
    return render(request, template_name)

def home(request):
    return simple_page(request, 'blog/home.html')

def tag_page(request):
    post_list = Post.objects.all()
    tags = Tag.objects.all()

    return render(
        request,
        'blog/index.html',
        {
            'post_list': post_list,
            'tags': tags,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count()
        }
    )

def category_page(request, slug):
    if slug == 'no_category':
        category = None
        post_list = Post.objects.filter(category=None)
    else:
        category = get_object_or_404(Category, slug=slug)
        post_list = Post.objects.filter(category=category)

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

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'  # 'posts' 대신 'post_list'로 통일
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:index')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        
        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip().replace(',', ';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)

        return response

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def no_category(request):
    post_list = Post.objects.filter(category=None)
    return render(request, 'blog/no_category.html', {'post_list': post_list})

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'category', 'tags']
    template_name = 'blog/post_update_form.html'
    success_url = reverse_lazy('blog:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.tags.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip().replace(',', ';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)

        return response

def search(request):
    query = request.GET.get('query', '')
    search_results = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search_results.html', {
        'search_results': search_results,
        'query': query
    })