from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.CalendarView.as_view(), name='index'),
    # path('event/new/', views.create_event, name='event_new'),
    # path('', views.index, name ='index'),
]
