from django.contrib import admin
from .models import Question

admin.site.register(Question) # Question 을 어드민 화면에 등록함
# Register your models here.
# 장고어드민은 어드민 사이트를 만드는 시간을 줄여주고 테스트를 원할하게 할수 있게 해준다.
