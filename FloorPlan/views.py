from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import ProjectManager, TeamMember, Project, Category, Task

def index(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()


    return render(request, "core/index.html", {'projects': projects, 'tasks': tasks})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    projects = Project.objects.all()
    projectmanager = ProjectManager.objects.filter(project=project)  #May have to add project as a field to users?  Possibly unique constraints.
    user = TeamMember.objects.filter(project=project)  #May have to add this as well.  Many to many. 
    return render(request, 'FloorPlan/project.html'), {'project': project, 'projects': projects, 'pk': pk, 'projectmanager': projectmanager, 'user': user}

def new_project(request):
    if request.method == "POST":
        form =  ProjectForm(request.POST) #Need to build a form here.
        if form.is_valid():
            project = form.save()
            return redirect('index')
    else:
        form = ProjectForm()

    return render(request, 'FloorPlan/new_project.html', {'form': form,})
    
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            form.save()
            return redirect('index')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'FloorPlan/edit_project.html', {'form': form})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('index')


def new_task(request, category, ppk):  #This can't be right... 
    project = get_object_or_404(Project, pk=pk)
    task = Task(project=project)
    if request.method == "POST":
        form = TaskForm(request.POST)  #This will need a form.
        if form.is_valid():
            task = form.save()
            return redirect('project', pk=project.pk) #This is going to need a pk. 
        else:
            form = TaskForm(instance=task)
        return render(request, 'FloorPlan/project.html', {'form': form, 'task': task, 'project': project})  #This is going to need a pk I think.

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('project', pk=project.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'FloorPlan/edit_task.html', {'form': form, 'log': log, 'pk': pk})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task-detail', pk=task.project.pk)
    

