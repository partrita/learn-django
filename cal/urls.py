from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calender'),
    path('new', views.event, name='event_new'),
    path('edit', views.event, name='event_edit'),
]