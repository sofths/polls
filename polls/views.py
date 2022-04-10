from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question,Choice
from django.urls import reverse
from django.shortcuts import render # reder 는 코드 양을 줄일수 있다.
# 간단한 함수를 지원한다. http함수를 response 하지 않고 render 로 사용할 수 있다.
# Create your views here.
# 뷰에서는 request 를 받고 여러가지 정보를 받고 response 를해준다.
# #response 를 해주기전에 데이터를 추출하고,저장하고,다운로드 로직을 거칠수도 있고 기본 개념은 위와 같다.

# def index(request): # view 로 보여줌
#     return HttpResponse('hello, world')
# 데이터를 추출하여 클라이언트에게 보내주기
# 앞으로 어떻게 하면 수정영역이 줄어들까 고민해야함
# 템플릿에 polls 를 만들건데 apps 이름을 붙여 만들어야 한다.
# 왜냐하면 그냥 구분 없이 만들면 장고는 어떤 앱인지 모르게 되기 때문이다.
# def index(request): #DB 에 추출해서 보여줌
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] # 출력 내용은 출판 일자를 정렬하여 5개 까지만 출력하게 됨
#     output = ','.join([q.question_text for q in latest_question_list]) # 이 다섯개를 , 로 연결하게 된다.
#
#     return HttpResponse(output)
# def index(request): #
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] # 출력 내용은 출판 일자를 정렬하여 5개 까지만 출력하게 됨
#     template = loader.get_template('polls/index.html') # loader.get_template 를 사용하여 해당 경로의 html 을 불러옴
#     context = { # context 를 통해서 template 에 data 를 전달해준다. # 질문이 여러개 있다면 tamplate 를 통해 데이터를 가져오고
#         'latest_question_list': latest_question_list,  # 가져온 데이터를 여기에 넣어주고 템플릿에 보내지게 된다.
#     }
#
#     return HttpResponse(template.render(context,request)) # template 을 loader 에서 response 해주면 된다.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request,'polls/index.html',context) # render 함수 사용 함수 매개 변수를 보고싶으면 controll 누르고 클릭


# 에러 일으키기
# def detail(request, question_id):
#     try:
#         question= Question.objects.get('pk-question_id') # question id 번호를 가져옴
#     except Question.DoseNotExist: # 없는번호를 조회하면
#         raise Http404("Question dose not exist")   #404에 띄워줄 메시지를
#     return render(request,'polls/detail.html',{'question':question}) # 리턴한다.
#try, except 처리 없이 하는 방법도 있다.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #테이블, 기본키 컬럼 설정
    return render(request,'polls/detail.html',{'question':question}) # 리턴 request,html 경로,키:벨류 를 리턴

def results(request,question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_cohice = question.choice_set.get(pk=request.POST['choice'])
    except {KeyError, Choice.DoesNotExist}:
        return render(request, 'polls/detail.html', {'question': question,
                                                     'error_message':"You didn't select a choice",
                                                     })
    else:
        selected_cohice.votes += 1
        selected_cohice.save()

        return HttpResponseRedirect('polls:result', args=(question_id, id))

