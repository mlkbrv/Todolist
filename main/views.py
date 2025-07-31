from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task

from django.db.models import Q


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = Task.objects.filter(completed=False, title__icontains=search_query)
        completed_tasks = Task.objects.filter(completed=True, title__icontains=search_query)
    else:
        tasks = Task.objects.filter(completed=False)
        completed_tasks = Task.objects.filter(completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'search_query': search_query,
        'task_number': tasks.count()
    }
    return render(request, 'main/index.html', context)

def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()

    return redirect('index')

@require_POST
def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('index')


def edit(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(instance=task)
    return redirect('index')

def complete(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.completed = True
        task.save()
    return redirect('index')

def undo(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.completed = False
        task.save()
    return redirect('index')