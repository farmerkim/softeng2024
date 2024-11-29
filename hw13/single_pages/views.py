from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings

def get_blog_posts():
    file_path = os.path.join(settings.BASE_DIR, 'data', 'blog_posts.csv')  # 경로 설정

    # 파일 존재 여부 확인
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")  # 파일이 없을 경우 경고 메시지
        return []  # 빈 리스트 반환 등 예외 처리

    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")

def index(request):
    return render(request, 'single_pages/index.html')

def blog(request):
    posts = get_blog_posts()
    return render(request, 'single_pages/single_post.html', {'posts': posts})  # posts를 컨텍스트에 추가

def crop_yield_meter(request):
    return render(request, 'single_pages/crop_yield_meter.html')

def about_crop(request):
    return render(request, 'single_pages/about_crop.html')