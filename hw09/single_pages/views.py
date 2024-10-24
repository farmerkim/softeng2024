from django.shortcuts import render
import pandas as pd

def get_blog_posts():
    df = pd.read_csv("blog_posts.csv")
    return df.to_dict(orient="records")

def index(request):
    return render(request, 'single_pages/index.html')

def blog(request):
    posts = get_blog_posts()
    return render(request, 'single_pages/blog.html', {'posts': posts})

def crop_yield_meter(request):
    return render(request, 'single_pages/crop_yield_meter.html')

def about_crop(request):
    return render(request, 'single_pages/about_crop.html')
