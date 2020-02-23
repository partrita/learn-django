from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.board_topics, name='board_topics'),
    path('<int:pk>/new', views.new_topic, name='new_topic'),
    # path('new', views.event, name='event_new'),
    # path('edit', views.event, name='event_edit'),
]