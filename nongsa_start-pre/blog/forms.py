from django import forms
from .models import Post, Category, Tag

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        label='카테고리'
    )
    
    tags_str = forms.CharField(
        label='태그',
        required=False,
        help_text='쉼표(,)로 구분하여 입력해주세요',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '예: 파이썬, 장고, 웹개발'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags_str']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력하세요'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력하세요'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # 수정의 경우
            # 기존 태그들을 쉼표로 구분된 문자열로 변환
            tags_list = list(self.instance.tags.values_list('name', flat=True))
            self.initial['tags_str'] = ', '.join(tags_list)

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
            
            # 태그 처리
            tag_list = []
            tags_str = self.cleaned_data.get('tags_str', '').strip()
            if tags_str:
                tag_names = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(
                        name=tag_name,
                        defaults={'slug': tag_name.lower().replace(' ', '-')}
                    )
                    tag_list.append(tag)
            
            instance.tags.set(tag_list)
            
        return instance

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '카테고리 이름을 입력하세요'
            })
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '태그 이름을 입력하세요'
            })
        }