from django.urls import path
from . import views
#url 패턴에 걸리게 되면 해당 내용을 연결해준다.

app_name = 'polls'
urlpatterns = [
    #/polls/  클라이언트가 /polls 를 호출하게 되면 패턴대로 view에 index를 호출하게 되고 리턴값인 hello world 가 리턴되게 된다.
    path('',views.index, name='index'),
    #/polls/int/    question id 로 int 값을 전달해주면 detail 에 전달해주고 전달한 값을 view 에서 리턴에 출력되게 작성되었다.
    path('<int:question_id>/',views.detail,name='detail'),
    #/polls/int/result
    path('<int:question_id>/results',views.results,name='results'),
    ##/polls/int/vote
    path('int:question_id/vote', views.vote,name='vote')
] # question_id 는 view 에 있는 question_id 와 매치되어야한다.
  # view 에서는 Httpresponse 객체를 반환하거나. 혹은 404 값을 발생하게 된다.
  # 리턴되기 전에 데이터 베이스나 어떤 여러 작업을 할 수 있게된다.