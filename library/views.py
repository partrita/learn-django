from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

def index(request):
    shelf = Book.objects.all()
    return render(request, 'library/index.html', {'shelf':shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('library:index')
        else:
            return HttpResponse('your form is wrong')
    else:
        return render(request, 'library/upload.html',{'upload':upload})

def update(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('library:index')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('library:index')
    return render(request, 'library/upload.html', {'upload':book_form})

def delete(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('library:index')
    book_sel.delete()
    return redirect('library:index')
