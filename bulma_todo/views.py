from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all()
            messages.success(request,("Task has been added!"))
            return render(request, 'bulma_todo/home.html', {'todos': todos})
    else:
        todos = Todo.objects.all()
        return render(request, 'bulma_todo/home.html', {'todos': todos})

def delete(reqeust, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(reqeust, 'Task has been deleted!')
    return redirect('bulma_todo:index')

def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('bulma_todo:index')
  
def mark_incomplete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('bulma_todo:index')

def edit(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id = todo_id)
        form = TodoForm(request.POST or None, instance=todo)
        
        if form.is_valid():
            form.save()
            messages.success(request,('Task has been edited!'))
            return redirect('bulma_todo:index')
    else:
        todo = Todo.objects.get(id=todo_id)
        return render(request, 'bulma_todo/edit.html', {'todo': todo})
