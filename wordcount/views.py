from django.shortcuts import render
from .forms import WordForm

# def home(request):
#     return render(request, 'wordcount/home.html')

# def result(request):
#     full = request.GET['fulltext']
#     words = full.split()
#     words_dic = {}
#     for i in words:
#         if i in words_dic:
#             words_dic[i]+=1
#         else:
#             words_dic[i]=1

#     return render(request, 'wordcount/result.html', {
#         'full':full,
#         'length':len(words),
#         'dic':words_dic.items(),
#     })

def word(request):
    result = None
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            full = form.cleaned_data['user_input']
            words = full.split()
            words_dic = {}
            for i in words:
                if i in words_dic:
                    words_dic[i]+=1
                else:
                    words_dic[i]=1
            result = {
                'full':full,
                'length':len(words),
                'dic':words_dic.items(),
            }
    form = WordForm()            
    return render(request, 'wordcount/home.html', {'form':form, 'result': result})

