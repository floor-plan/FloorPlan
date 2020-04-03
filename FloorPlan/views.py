from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .import forms
# from django.core.exceptions import DoesNotExist
from django.contrib import messages

from django.views.generic import CreateView, TemplateView
from .forms import ProjectForm, TaskForm, NewTeamMemberForm, ProjectManagerSignUpForm, MemberSignUpForm, CategoryForm, CompleteTaskForm
from users.models import Member
from .models import Project, Category, Task
from django.views.decorators.csrf import csrf_exempt
from .decorators import project_manager_required


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

    def home(request):
        if request.user.is_authenticated:
            if request.user.is_teacher:
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        return render(request, 'dashboard.html')


class ProjectManagerSignUpView(CreateView):
    model = Member
    form_class = ProjectManagerSignUpForm
    template_name = 'registration/signup_as_pm.html'

    def get_context_data(self, **kwargs):
        kwargs['group'] = 'project_manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.is_project_manager = True
        user.save()
        login(self.request, user)
        return redirect('dashboard')

class MemberSignUpView(CreateView):
    model = Member
    form_class = MemberSignUpForm
    template_name = 'registration/signup_as_member.html'

    def get_context_data(self, **kwargs):
        kwargs['group'] = 'member'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


@login_required
def dashboard(request):
    projects = Project.objects.all()
    user = request.user
    tasks = Task.objects.filter(assignee=user)
    
    return render(request, "core/dashboard.html", {'projects': projects, 'tasks': tasks})

@login_required
def project(request, pk):
    project = Project.objects.get(pk=pk)
    tasks = Task.objects.filter(project=project)
    categories = Category.objects.all()
    users=Member.objects.all()  
    return render(request, 'core/project.html', {'project': project, 'tasks': tasks, 'categories':categories, 'users':users, 'pk': pk})
    

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
@project_manager_required
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
            # next = request.POST.get('next', '/')
            form.save()
        return redirect('project', projectpk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'core/edit_task.html', {'form': form, 'pk':pk, 'task': task})



    # return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))
   
  
@login_required
@csrf_exempt
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_complete = True
        task.save()
    return JsonResponse({"status": "ok", "data": None})


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


@login_required
def new_category(request, pk):  
    project = get_object_or_404(Project, pk=pk)
    form = CategoryForm(request.POST) 
    category = None
    if request.method == "POST":  
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            form.save()
            return redirect('project', projectpk) 
    else:
            form = CategoryForm(instance=category)
    return render(request, 'core/new_category.html', {'form': form, 'category': category, 'project': project})
    

@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            form.save()
            return redirect('project', projectpk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'core/edit_category.html', {'form': form, 'pk':pk, 'category': category})
  

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    