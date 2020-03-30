from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .import forms
# from django.core.exceptions import DoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView
from .forms import ProjectForm, TaskForm, NewTeamMemberForm, ProjectManagerSignUpForm, MemberSignUpForm
from users.models import Member
from .models import Project, Category, Task




class SignUpView(TemplateView):
    template_name = 'signup.html'

    def home(request):
        if request.user.is_authenticated:
            if request.user.is_project_manager:
                return redirect('projects')
        else:
            return redirect('dashboard')
        return render(request, 'core/dashboard.html')

class ProjectManagerSignUpView(CreateView):
    model = Member
    form_class = ProjectManagerSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'project_manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('project_manager:projects')

class MemberSignUpView(CreateView):
    model = Member
    form_class = MemberSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'member'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('member:projects')

@login_required
def dashboard(request):
    projects = Project.objects.all()
    users = Member.objects.all()
    user = Member.objects.get(username=request.user.username)
    # ***Lines 30, 39, and 40 may need some attention***
    tasks = Task.objects.all()
    # assignee = Task.objects.filter(assignee=user)
    return render(request, "core/dashboard.html", {'projects': projects, 'tasks': tasks, 'user':user})

@login_required
def project(request, pk):
    project = Project.objects.get(pk=pk)
    tasks = Task.objects.filter(project=project)
    users=Member.objects.all()  
    teammembers = Profile.objects.filter(project=project)
    return render(request, 'core/project.html', {'project': project, 'tasks': tasks, 'teammembers':teammembers, 'users':users, 'pk': pk})
    

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


@login_required
def edit_project(request, pk):         
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
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
  

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def new_team_member(request, pk):
    project = get_object_or_404(Project, pk=pk)
    user = request.user.username
    team_member = Member(project.pk)
    if request.method == "POST":
        form = NewTeamMemberForm(request.POST) 
        if form.is_valid():
            new_team_member = form.save(commit=False)
            try:
                team_member = user

            except Member.DoesNotExist:
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
    team_member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = NewTeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            form.save()
            return redirect('project', projectpk)
    else:
        form = NewTeamMemberForm(instance=team_member)
    return render(request, 'core/edit_team_member.html', {'form': form, 'pk': pk, 'team_member': team_member})


@login_required
def delete_team_member(request, pk):
    team_member = get_object_or_404(Member, pk=pk)
    team_member.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    