from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .import forms
from .models import ProjectManager, TeamMember, Project, Category, Task
from django.contrib.auth.models import User
from .forms import ProjectForm, TaskForm, NewTeamMemberForm

def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()

    return render(request, "core/dashboard.html", {'projects': projects, 'tasks': tasks})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    # tasks = Task.objects.filter(project=project)
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

    return render(request, 'core/new_project.html', {'form': form,})
    
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
    # task = Task(project=project)
    form = TaskForm(request.POST) 
    if request.method == "POST":  
        if form.is_valid():
            task = form.save()
            return redirect('project', pk=project.pk) 
        else:
            form = TaskForm(instance=task)
    return render(request, 'core/newtask.html', {'form': form,'project':project})  

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
    # user= User.objects.get(username=request.user.username)
    team_member = TeamMember(project.pk)
    form = NewTeamMemberForm(request.POST) 
    if request.method == "POST":
        try:
            add_tm = User.objects.get(username=request.POST['teammember'])
        except ObjectDoesNotExist:
            form = NewTeamMemberForm()
            return render(request, 'core/new_team_member.html', {'form': form, 'type': 'new_team_member', 'message': "That team member not found"})
        if TeamMember.objects.filter(team_member=add_tm, project=project):
            form = NewTeamMemberForm()
            return render(request, 'core/new_team_member.html', {'form': form, 'type': 'new_team_member','message': "You've already added that user as a team member"})
        else:
            new_team_member = TeamMember(project=project, new_team_member=add_tm)
            new_team_member.save()
            return redirect('project', pk=project.pk)
    else:
        form = NewTeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'core/new_team_member.html', {'form': form, 'pk':pk})
    # else:
    #     form = NewTeamMemberForm()
    return render(request, 'core/new_team_member.html', {'form': form})

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
    

