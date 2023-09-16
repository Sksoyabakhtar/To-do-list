from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed')

        if not completed:
            completed = False
        else:
            completed = True

        Task.objects.create(title=title, description=description, completed=completed)
        return redirect('task_list')
    return render(request, 'add_task.html')


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') 

        completed = completed == 'on'

        task.title = title
        task.description = description
        task.completed = completed
        task.save()
        return redirect('task_list')
    return render(request, 'update_task.html', {'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
