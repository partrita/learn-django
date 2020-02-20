from django.urls import path
from . import views

app_name = "tools"

urlpatterns = [
    path('', views.tools_list, name ='tools_list'),
    path('vib1/', views.vib1, name='vib1'),
    path('tool1/', views.tool1, name='tool1'),
    path('tool2/', views.tool2, name='tool2'),
    path('tool3/', views.tool3, name='tool3'),
]
