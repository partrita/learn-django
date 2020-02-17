from django.shortcuts import render
from .models import Vib1InputForm
from .compute import compute

def tools_list(request):
    tools_list = [
        {'name':'tool1', 'url': 'tool1', 'description':'tool1_descript'},
        {'name':'tool2', 'url': 'tool2', 'description':'tool2_descript'},{'name':'tool3', 'url': 'tool3', 'description':'tool3_descript'},
        ]
    return render(request, 'tools/tools_list.html', {'tools': tools_list})

def tool1():
    pass

def tool2():
    pass

def tool3():
    pass

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