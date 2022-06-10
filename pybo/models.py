from django.db import models

# Create your models here.

from django.db import models

class Question(models.Model):
    """
    질문 모델 작성
    """
    subject = models.CharField(max_length=200) # 질문의 제목
    content = models.TextField() # 질문의 내용
    create_date = models.DateTimeField() # 질문을 작성한 일시
