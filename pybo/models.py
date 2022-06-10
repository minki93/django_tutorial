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

    def __str__(self):
        """
        조회 결과에 속성값으로 보여주기
        """
        return self.subject

class Answer(models.Model):
    """
    답변 모델 작성
    """
    question = models.ForeignKey(Question, on_delete = models.CASCADE) # 질문 -- 어떤 질문의 답변인지 알아야하므로, 질문 속성 필요
    content = models.TextField() # 답변 내용
    create_date = models.DateTimeField() # 답변 작성 일시
