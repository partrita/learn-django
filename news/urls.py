from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('scrape/', views.scrape, name='scrape'),
    path('', views.news_list, name ='home'),
    # path('<int:pk>/', views.detail, name='detail'),
]
