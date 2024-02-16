from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Todo
from django.views.decorators.http import require_http_methods

def todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')

    if title:
        todo = Todo.objects.create(title=title)

    return render(request, 'todo/partials/todo.html', {'todo': todo})

@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()

    return render(request, 'todo/partials/todo.html', {'todo': todo})

@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()
