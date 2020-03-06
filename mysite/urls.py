"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page':'/'}),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('tools/', include('tools.urls')),
    path('lotto/', include('mylotto.urls')),
    # path('users/', include('users.urls')),
    path('polls/', include('polls.urls')),
    path('cal/', include('cal.urls')),
    path('boards/', include('boards.urls')),
    # path('schedule/', include('schedule.urls')),
    path('crud/', include('crud.urls')),
    path('news/', include('news.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('wordcount/', include('wordcount.urls')),
    path('csv/', include('csv_app.urls')),
    path('', include('blog.urls')),
]
