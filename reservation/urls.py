from django.urls import path
from djreservation import urls as djreservation_urls
from . import views

app_name = "reserv"

urlpatterns = [
    # path('', views.index, name ='index'),
    path('', views.home, name='home'),
    path('create/<int:pk>', views.MyObjectReservation.as_view()),
]

urlpatterns += djreservation_urls.urlpatterns