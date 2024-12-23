# single_pages/models.py
from django.db import models

class GreenhouseData(models.Model):
    temperature = models.FloatField()  # 온도
    humidity = models.FloatField()  # 습도
    timestamp = models.DateTimeField(auto_now_add=True)  # 데이터 기록 시간

    def __str__(self):
        return f"{self.timestamp} - Temp: {self.temperature}°C, Humidity: {self.humidity}%"
