from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'task':tasks, 'form':form}
    return render(request, "index.html", context=context)

def add(request, pk):
    tasks = task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, "index.html", context=context)

def delete(request, pk):
    tasks = task.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('index')
    context = {'task':tasks}
    return render(request, "delete.html", context=context)
