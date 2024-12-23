from django.shortcuts import render

# 실시간 온실 관리, 영농 일지, 수확량 계산기 등의 기본 뷰들
def index(request):
    return render(request, 'single_pages/index.html')

def crop_yield_meter_view(request):
    return render(request, 'single_pages/crop_yield_meter.html')

def sensor_view(request):
    return render(request, 'single_pages/sensor_view.html')

def greenhouse_reservation(request):
    return render(request, 'single_pages/greenhouse_reservation.html')

def customer_center(request):
    return render(request, 'single_pages/customer_center.html')