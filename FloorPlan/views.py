from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .import forms
from .models import Project, Category, Task
from users.models import User
from .forms import ProjectForm, TaskForm
# from django.core.exceptions import DoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'sign_up.html', {'form': form})


@login_required
def dashboard(request):
    projects = Project.objects.all()
    user = User.objects.get(username=request.user.username)
    tasks = Task.objects.all()
    assignee = Task.objects.filter(assignee=user)
    return render(request, "core/dashboard.html", {'projects': projects, 'tasks': tasks, 'user':user})

@login_required
def project(request, pk):
    project = Project.objects.get(pk=pk)
    tasks = Task.objects.filter(project=project)
    users = User.objects.filer(project=project)
    return render(request, 'core/project.html', {'project': project, 'tasks': tasks, 'users':users,'pk': pk})
    

@login_required
def new_project(request):
    if request.method == "POST":
        form =  ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project', project.pk)
    else:
        form = ProjectForm()

    return render(request, 'core/new_project.html', {'form': form,})



# def edit_project(request, pk): 
#     if request.method == 'GET':
#         return render(request, 'core/edit_project.html', {'form':form})
#     else:
#         try:
#             form = ProjectForm(request.POST)
#             editproject = form.save(commit=False)
#             editproject.save()
#             return redirect('dashboard')
#         except ValueError:
#             return render(request, 'core/edit_project.html', {'form':form})

@login_required
def edit_project(request, pk):         
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            form.save()
            return redirect('project', pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'core/edit_project.html', {'form': form})
    

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('dashboard')


@login_required
def new_task(request, pk):  
    project = get_object_or_404(Project, pk=pk)
    form = TaskForm(request.POST) 
    task = None
    if request.method == "POST":  
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            task = form.save()
            return redirect('project', projectpk) 
    else:
            form = TaskForm(instance=task)
    return render(request, 'core/newtask.html', {'form': form,'task': task, 'project':project})  


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            form.save()
            return redirect('project', projectpk)
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

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
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


@login_required
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


@login_required
def delete_team_member(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    team_member.delete()
    return redirect('project', pk=project.pk)
    

