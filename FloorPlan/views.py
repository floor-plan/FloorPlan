from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .import forms
from .models import ProjectManager, TeamMember, Project, Category, Task
from users.models import User
from .forms import ProjectForm, TaskForm, NewTeamMemberForm
# from django.core.exceptions import DoesNotExist
from django.contrib import messages



def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()

    return render(request, "core/dashboard.html", {'projects': projects, 'tasks': tasks})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    # tasks = Task.objects.filter(project=project)
    projects = Project.objects.all()
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
    form = TaskForm(request.POST, instance=task)
    if request.method == "POST":
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = TaskForm(instance=task)


    return render(request, 'core/edit_task.html', {'form': form, 'pk':pk, 'task': task})



# def edit_habit(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)

#     if request.method == 'POST':
#         form = HabitForm(request.POST, instance=habit)
#         if form.is_valid():
#             form.save()

#             return redirect('home')
#     else:
#         form = HabitForm(instance=habit)

#     return render(request, 'core/edit_habit.html', {"form": form})    

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('dashboard')

def new_team_member(request, pk):
    project = get_object_or_404(Project, pk=pk)
    user = request.user
    team_member = TeamMember(project.pk)
    # form = NewTeamMemberForm(request.POST) 
    if request.method == "POST":
        form = NewTeamMemberForm(request.POST) 
        if form.is_valid():
            new_team_member = form.save(commit=False)
            try:
                team_member = TeamMember.objects.get(name=new_team_member.name, company=new_team_member.company)

            except TeamMember.DoesNotExist:
                new_team_member.project = project
                new_team_member.team_member = user
                form.save()
                return redirect('project', pk=project.pk)
            else:
                print('user exists')
                messages.warning(request, "This user already exists")
                form = NewTeamMemberForm()
                return render(request, 'core/new_team_member.html', {'form':form, 'project': project})
    else:
        form = NewTeamMemberForm()
        return render(request, 'core/new_team_member.html', {'form':form, 'project': project})


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
    

