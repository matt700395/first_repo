from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)#제목이 꼭 있도록 null=False
    #3개의 사진을 받도록 이미지 3개를 설정
    image = models.ImageField(upload_to='article/', null=False)
    image2 = models.ImageField(upload_to='article/', null=True)
    image3 = models.ImageField(upload_to='article/', null=True)

    content = models.TextField(null=True)#내용도 꼭 있도록 null=False

    created_at = models.DateField(auto_now_add=True, null=True)
