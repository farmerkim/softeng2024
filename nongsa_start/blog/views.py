from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from .models import Post, Category, Tag
from .forms import PostForm, CommentForm
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    # post_list로 통일
    post_list = Post.objects.select_related('author', 'category').order_by('-created_at')
    
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
            'tags': Tag.objects.all(),  # Tag 모델의 모든 객체를 전달
            'recent_posts': Post.objects.order_by('-created_at')[:5],  # 최근 게시물 5개
            'user': request.user  # user 정보 추가
        }
    )

def single_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # 로그인하지 않은 사용자가 댓글을 작성하려고 할 때
        if not request.user.is_authenticated:
            messages.error(request, "로그인 해주셔서 댓글 작성이 가능합니다.")
            return redirect('login')  # 로그인 페이지로 리디렉션

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # 해당 포스트에 댓글을 연결
            comment.author = request.user  # 댓글 작성자를 설정
            comment.save()
            return redirect('blog:single_post', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/single_post.html', {'post': post, 'form': form})

# 로그인하지 않은 사용자가 댓글을 달려고 할 때
def not_logged_in(request):
    messages.error(request, "로그인 해주세요.")
    return redirect('login')  # 로그인 페이지로 리디렉션


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # 작성자나 스태프만 삭제할 수 있도록
    if request.user == post.author or request.user.is_staff:
        post.delete()
        return redirect('blog:index')
    else:
        raise PermissionDenied

def simple_page(request, template_name):
    return render(request, template_name)

def home(request):
    return render(request, 'single_pages/index.html')

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
    context_object_name = 'post_list'
    ordering = ['-created_at']
    paginate_by = 5  # 한 페이지에 5개의 포스트 표시

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

        # tags 처리
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