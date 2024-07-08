from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        context={
            'tasks': tasks,
            'form': form,
        }
    return render(request, 'task_list.html',context )

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context={
        'task': task,
    }
    return render(request, 'task_detail.html',context )

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
        context={
        'task': task,
    }
    return render(request, 'task_confirm_delete.html', context)
