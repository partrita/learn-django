from django.urls import path
from . import views


app_name = 'lotto'

urlpatterns = [
    path('', views.index, name ='index'),
    path('new/', views.post, name='new_lotto'),
    path('<int:pk>/', views.detail, name='detail'),
]
