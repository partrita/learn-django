from django.shortcuts import render, redirect
from .models import GuessNumbers
from .forms import PostForm

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'mylotto/default.html', {'lottos':lottos})

def post(request):
    if request.method == "POST":
         # create a form instance and populate it with data from the request:
        form = PostForm(request.POST) #PostForm으로 부터 받은 데이터를 처리하기 위한 인스턴스 생성
        if form.is_valid(): #폼 검증 메소드
            lotto = form.save(commit = False) #lotto 오브젝트를 form으로 부터 가져오지만, 실제로 DB반영은 하지 않는다.
            lotto.generate()
            return redirect('index') #url의 name을 경로대신 입력한다.
    else:
        form = PostForm() #forms.py의 PostForm 클래스의 인스턴스
        return render(request, 'mylotto/form.html', {'form' : form})  # 템플릿 파일 경로 지정, 데이터 전달

def detail(request, pk): # perameter 'lottokey'를 함께 전달
    #primary key가 lottokey 파라미터와 일치하는 오브젝트를 가져온다.
    #primary key는 클래스의 오브젝트 생성시 자동으로 생성, .py 를 통해 가져올 수 있다.
    lotto = GuessNumbers.objects.get(pk = pk)
    return render(request, 'mylotto/detail.html', {'lotto' : lotto})
