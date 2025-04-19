from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    
    return render(request, 'todo/index.html',{'tasks':tasks, 'form':form})


def toggle_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed  # Toggle the completed status
    task.save()
    return redirect('/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
