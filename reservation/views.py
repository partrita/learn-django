from django.shortcuts import render
from django.http import HttpResponse
from djreservation.views import ProductReservationView
from .models import MyObject

def index(request):
    return HttpResponse('hello reservation world!')
# Create your views here.

def home(request):
    list_object = MyObject.objects.all()
    return render(request, 'reservation/index.html', context={
        'list_object': list_object
    })

class MyObjectReservation(ProductReservationView):
    base_model = MyObject     # required
    amount_field = 'quantity'  # required
    extra_display_field = ['measurement_unit']  # not required
