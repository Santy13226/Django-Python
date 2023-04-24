from django.http import HttpResponse, JsonResponse    
from .models import Project, Tasks
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask
from .forms import CreateNewProject

# Create your views here.
def index(request):
    title='Welcome to DJANGO Course!!'
    return render(request, 'index.html',{
        'title': title
    })

def about(request):
    username ='Santy'
    return render(request, "about.html",{
        'user':username
    })

def hello(request, username):
    return HttpResponse("<H1>Hola %s</H1>"%username)
    print(username)

def projects(request):
    #projects= list(Project.objects.values())
    projects =Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def tasks(request):
    #task=get_object_or_404(Tasks, id=id)
    tasks =Tasks.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    })

def create_task(request):
    if request.method =='GET':
        #show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Tasks.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method =='GET':
        return render(request, 'projects/create_project.html',{
        'form': CreateNewProject
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    project=get_object_or_404(Project, id=id)
    tasks=Tasks.objects.filter(project_id=id)
    return render(request,'projects/detail.html',{
        'project':project,
        'tasks': tasks
    })
