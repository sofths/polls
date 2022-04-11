from django.test import TestCase
import datetime
from django.db import models
from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase): # 테스트 코드들을 추가함
    # 테스트 케이스를 작성할때 임포트한 테스트 케이스를 테스트 클래스의 매개변수에 넣어주면된다.


    def test_was_published_recently_with_future_question(self):
        time = timezone.now() , datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assetyls(future_question.was_published_recently(), False)
# Create your tests here.
