from django import forms
from .models import GuessNumbers
# 모델클래스 GuessNumbers로 부터 데이터를 입력 받을 폼을 작성한다.

class PostForm(forms.ModelForm): #forms의 ModelForm 클래스를 상속 받는다.

    class Meta:
        model = GuessNumbers #GuessNumbers와 연결
        fields = ('name', 'text', 'num_lotto', ) # 그 중에 입력 받을 것
