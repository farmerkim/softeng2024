from django.shortcuts import render
from datetime import datetime

# 실시간 온실 관리, 영농 일지, 수확량 계산기 등의 기본 뷰들
def index(request):
    return render(request, 'single_pages/index.html')
