from django.shortcuts import render, HttpResponse
import random
import datetime

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    return render(request, 'index.html')
    
def dinner(request):
    box = ['치킨', '치킨', '편도', '롯데리아']
    dinner = random.choice(box)
    # render 필수인자
    # 1) request, 2) template 파일 (html)
    # 3) dictionary : 템플릿에서 쓸 변수 값을 정의
    return render(request, 'dinner.html', {'dinner': dinner, 'box': box})
    # template은 기본적으로 문법이 jinja2랑 같은데, 장고에서는 DTL을 쓴다.
    # Django Template Language

def you(request, name):
    return render(request, 'you.html', {'name': name})

def cube(request, num):
    return render(request, 'cube.html', {'cnum' : num**3, 'num' : num})
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    msg = request.GET.get('message')
    return render(request, 'pong.html', {'msg': msg})

def user_new(request):
    return render(request, 'user_new.html')
    
def user_read(request):
    id = request.POST.get('id')
    password = request.POST.get('password')
    return render(request, 'user_read.html',{'id' : id, 'password' : password})

def template_example(request):
    my_dict = {'name': 'kim', 'nickname': 'edutak', 'age': 100}
    my_list = ['짜장면', '짬뽕', '탕수육', '양장피']
    my_sentence = 'Life is short, you need python!'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.datetime.now()
    empty_list = []
    return render(request, 'template_example.html', {'my_list' : my_list, 'my_dict' : my_dict, 'my_sentence': my_sentence, 'messages': messages,'empty_list': empty_list, 'datetimenow': datetimenow })

def static_example(request):
    return render(request, 'static_example.html')