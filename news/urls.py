from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.news_list, name ='index'),
    path('scrape/', views.scrape, name='scrape'),
    # path('<int:pk>/', views.detail, name='detail'),
]
