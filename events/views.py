from django.shortcuts import render

def index(reqeust):
    
    return render(request, 'events/index.html')