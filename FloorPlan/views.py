from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .import forms
from .models import ProjectManager, TeamMember, Project, Category, Task

from FloorPlan.forms import ProjectForm

def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()

    return render(request, "core/dashboard.html", {'projects': projects, 'tasks': tasks})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    # projects = Project.objects.all()
    # projectmanager = ProjectManager.objects.filter(project=project.owner) 
    # team_member = TeamMember.objects.filter(project=project.team_members)
    return render(request, 'core/project.html', {'project': project, 'pk': pk})
    

def new_project(request):
    if request.method == "POST":
        form =  ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()

    return render(request, 'core/new_project.html', {'form': form})
    
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'core/edit_project.html', {'form': form})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('dashboard')

def new_task(request, pk):  
    project = get_object_or_404(Project, pk=pk)
    # category = get_object_or_404(Category, pk=pk)
    task = Task(project=project)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  
        if form.is_valid():
            task = form.save()
            return redirect('project', pk=project.pk) 
        else:
            form = TaskForm(instance=task)
    return render(request, 'core/project.html', {'form': form, 'project': project})  

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('project', pk=project.pk)
        else:
            form = TaskForm(instance=task)
    return render(request, 'core/edit_task.html', {'form': form, 'pk': pk})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task-detail', pk=task.project.pk)

def new_team_member(request, pk):
    project = get_object_or_404(Project, pk=pk)
    team_member = Team_Member(project=project)
    if request.method == "POST":
        form = NewTeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project', pk=project.pk)
        else:
            form = NewTeamMemberForm(instance=team_member)
    return render(request, 'core/project.html', {'form': form, 'project': project, 'pk': pk})

def edit_team_member(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    if request.method == "POST":
        form = NewTeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            team_member = form.save()
            return redirect('project', pk=project.pk)
        else:
            form = NewTeamMemberForm(instance=team_member)
    return render(request, 'core/edit_team_member.html', {'form': form, 'pk':pk})

def delete_team_member(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    team_member.delete()
    return redirect('project', pk=project.pk)
    

