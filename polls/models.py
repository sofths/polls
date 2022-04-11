import datetime

from django.db import models
from django.utils import timezone # 발행일 시간을 입력하기 위해 time zone 을씀

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # 출판 일자

    def __str__(self): #__str__ 메소드를 입력하면 해당 메소드가 컬럼의 데이터를 불러옴
        return self.question_text

    def was_published_recently(self): # 커스텀 메소드 입력가능
        now = timezone.now()
        return now - datetime.timedelta(days=1) <- self.pub_date # 현재로 부터 하루 차감한 어제의 시간을 반환하게 되고 어제 이후에 발행이 된 데이터가 리턴
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 위 Question 함수를 참조하겠다 라는의미 CASCADE 는 참조자가 삭제되면 삭제 된다는 뜻
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): #__str__ 메소드를 입력하면 해당 메소드가 컬럼의 데이터를 불러옴
        return self.question_text
# Create your models here.
