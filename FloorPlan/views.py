from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.db.models.functions import Cast
from django.db.models import IntegerField, CharField
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .import forms
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from .forms import ProjectForm, TaskForm, AddTeamMemberForm, ProjectManagerSignUpForm, MemberSignUpForm, NewCategoryForm, CompleteTaskForm, CustomCategoryTaskForm
from users.models import Member
from .models import Project, Category, Task, ProjectCategory
from django.views.decorators.csrf import csrf_exempt
from .decorators import project_manager_required


#=====================================SIGNUP VIEWS==========================================================================

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


#=======================================DASHBOARD AND PROJECTS ==========================================================================
@login_required
def dashboard(request):
    projects = request.user.project_set.all()
    user = request.user
    tasks = Task.objects.filter(assignee=user)
    
    return render(request, "core/dashboard.html", {'projects': projects, 'tasks': tasks})

@login_required
def project(request, pk):
    project = Project.objects.get(pk=pk)
    tasks = Task.objects.filter(project=project)
    categories = Category.objects.all()
    projectcategories = ProjectCategory.objects.filter(project=project)
    users=Member.objects.all()  
    teammembers=Member.objects.filter(project=project) 

    return render(request, 'core/project.html', {'project': project, 'tasks': tasks, 'categories':categories, 'projectcategories': projectcategories, 'users':users, 'teammembers':teammembers, 'pk': pk})
    

@login_required
def new_project(request):
    user = request.user
    if request.method == "POST":
        form =  ProjectForm(request.POST)
        if form.is_valid():            
            project = form.save()
            project.project_team.add(user)
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



#=====================================TASKS==========================================================================
@login_required
@project_manager_required
def new_task(request, pk):  
    project = get_object_or_404(Project, pk=pk)
    form = TaskForm(request.POST)
    task = None
    if request.method == "POST":  
        if form.is_valid():
            task = form.save(commit=False)
            project.project_team.add(task.assignee)
            task.project = project
            task.save()
            return redirect('project', project.id)
    else:
            form = TaskForm(instance=task)
    return render(request, 'core/newtask.html', {'form': form, 'task': task, 'project': project, 'pk':pk})


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


#=====================================ASSIGNING TEAM MEMBERS TO PROJECTS==========================================================================

@login_required
@project_manager_required
def add_team_member(request, pk):  
    project = get_object_or_404(Project, pk=pk)
    form = AddTeamMemberForm(request.POST)
    members = Member.objects.all()
    if request.method == "POST":  
        if form.is_valid():
            project_team_data = form.cleaned_data.get("project_team")
            for member in project_team_data:
                project.project_team.add(member)
            return redirect('project', pk) 
    else:
            form = AddTeamMemberForm()
    return render(request, 'core/add_team_member.html', {'form': form, 'project': project, 'pk': pk})


@login_required
def delete_team_member(request, pk):
    team_member = get_object_or_404(Member, pk=pk)
    team_member.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#=====================================STANDARD CATEGORIES==========================================================================  

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



#===========================================CUSTOM CATEGORIES & TASKS===============================================================================
@login_required
@project_manager_required
def new_category(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = NewCategoryForm(request.POST, initial={'project': project.pk}) 
    category = None
    if request.method == "POST":  
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            category=form.save()
            return redirect('project', projectpk) 
    else:
            form = NewCategoryForm(instance=category)
    return render(request, 'core/new_category.html', {'form': form, 'category': category, 'project': project})


@login_required
def edit_category_customcategory(request, pk):
    category = get_object_or_404(ProjectCategory, pk=pk)
    if request.method == "POST":
        form = NewCategoryForm(request.POST, instance=category)
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            form.save()
            return redirect('project', projectpk)
    else:
        form = NewCategoryForm(instance=category)
    return render(request, 'core/edit_category_customcategory.html', {'form': form, 'pk':pk, 'category': category})
  

@login_required
def delete_category_customcategory(request, pk):
    category = get_object_or_404(ProjectCategory, pk=pk)
    category.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@project_manager_required
def new_task_customcategory(request, pk):  
    project = get_object_or_404(Project, pk=pk)
    form = CustomCategoryTaskForm(request.POST) 
    task = None
    if request.method == "POST":  
        if form.is_valid():
            task = form.save(commit=False)
            project.project_team.add(task.assignee)
            task.project = project
            task.save()
            return redirect('project', project.id)
    else:
            form = CustomCategoryTaskForm(instance=task)
    return render(request, 'core/new_task_customcategory.html', {'form': form, 'task': task, 'project': project})


@login_required
def edit_task_customcategory(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = CustomCategoryTaskForm(request.POST, instance=task)
        if form.is_valid():
            projectpk = form.cleaned_data['project'].pk
            form.save()
        return redirect('project', projectpk)
    else:
        form = CustomCategoryTaskForm(instance=task)
    return render(request, 'core/edit_task_customcategory.html', {'form': form, 'pk': pk, 'task': task})
    
    
    