from django.db import models
import os

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def filename(self):
        """첨부 파일의 이름을 반환"""
        return os.path.basename(self.file_upload.name)
    
    def file_extension(self):
        """첨부 파일의 확장자를 반환"""
        _, extension = os.path.splitext(self.file_upload.name)
        return extension.lower()

    def __str__(self):
        return f'[{self.pk}]{self.title}'
