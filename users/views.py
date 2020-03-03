# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.http import HttpResponse
# from .forms import UserForm, LoginForm
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.template import RequestContext

# def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(**form.cleaned_data)
#             login(request, new_user)
#             return redirect('index')
#     else:
#         form = UserForm()
#         return render(request, 'users/adduser.html', {'form': form})

# def signin(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             return HttpResponse('로그인 실패. 다시 시도 해보세요.')
#     else:
#         form = LoginForm()
#         return render(request, 'users/login.html', {'form': form})

# from youtube tutorials

from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')