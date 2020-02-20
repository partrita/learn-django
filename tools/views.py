from django.shortcuts import render
from .models import Vib1InputForm, Tool1Form, Tool2Form, Tool3Form
from .compute import compute

def tools_list(request):
    tools_list = [
        {'name':'Square calculator', 'url': 'tool1', 'description':'square calculation'},
        {'name':'Sum', 'url': 'tool2', 'description':'Sum of parameter'},
        {'name':'tool3', 'url': 'tool3', 'description':'tool3_descript'},
        ]
    return render(request, 'tools/tools_list.html', {'tools': tools_list})

def tool1(request):
    result = None
    if request.method == 'POST':
        form = Tool1Form(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = float(form2.x)*float(form2.y)
    else:
        form = Tool1Form()
    return render(request, 'tools/tool1.html', {'form':form, 'result': result})

def tool2(request):
    result = None
    if request.method == 'POST':
        form = Tool2Form(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = float(form2.x)+float(form2.y)+float(form2.z)
    else:
        form = Tool2Form()
    return render(request, 'tools/tool2.html', {'form':form, 'result': result})

def tool3():
    result = None
    if request.method == 'POST':
        form = Tool3Form(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = float(form2.x)+float(form2.y)+float(form2.z)
    else:
        form = Tool3Form()
    return render(request, 'tools/tool2.html', {'form':form, 'result': result})

def vib1(request):
    result = None
    if request.method == 'POST':
        form = Vib1InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.A, form2.b, form2.w, form2.T)
    else:
        form = Vib1InputForm()
    return render(request, 'tools/vib1.html',
            {'form': form,
             'result': result,
             })