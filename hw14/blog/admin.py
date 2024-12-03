from django.contrib import admin
from .models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # 관리자 화면에 표시할 필드
    list_filter = ('author', 'created_at', 'tags')  # 태그별 필터링 추가
    search_fields = ('title', 'content')  # 검색 기능 추가
    filter_horizontal = ('tags',)  # 태그 선택을 위한 좌/우 박스 위젯 추가
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')  # N+1 문제 방지

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # `slug` 필드를 자동 생성
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'post_count')  # 표시할 필드
    list_filter = ('created_at',)  # 생성일 기준 필터
    search_fields = ('name',)  # 이름으로 검색
    prepopulated_fields = {'slug': ('name',)}  # slug 자동 생성
    
    def post_count(self, obj):
        """해당 태그가 사용된 포스트 수를 반환"""
        return obj.posts.count()
    post_count.short_description = '포스트 수'  # 컬럼 헤더 이름 설정
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('posts')  # N+1 문제 방지