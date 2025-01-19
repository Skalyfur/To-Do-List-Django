from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'home.html')


def task_list(request):
    task = Task.objects.all()
    return render(request, 'task_list.html', {'task': task})    


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
       
        tasks = Task(title=title, description=description, date=date)
        tasks.save()  
        
        return render(request, 'create_task.html')
    
    return render(request, 'create_task.html')


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.date = request.POST.get('date')
        task.complete = request.POST.get('complete')
        task.complete = 'complete' in request.POST
         
        task.save()
        return redirect('task_list')  
        
    return render(request, 'update_task.html', {'task': task})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    
    return redirect('/task_list')