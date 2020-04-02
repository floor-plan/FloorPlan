# from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .import forms
# from django.core.exceptions import DoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from .forms import ProjectForm, TaskForm, NewTeamMemberForm, ProjectManagerSignUpForm, MemberSignUpForm, CategoryForm, CompleteTaskForm
from users.models import Member
from .models import Project, Category, Task
from django.views.decorators.csrf import csrf_exempt

# class LoginView(TemplateView):
#     template_name = 'registration/signup.html'

#     def home(request):
#         if request.user.is_authenticated:
#             if request.user.is_project_manager:
#                 return redirect('dashboard')
#             else:
#                 return redirect('dashboard')
#         return render(request, 'dashboard.html')

# class LogoutView(TemplateView):
#     template_name = 'registration/login.html'

#     def home(request):
#         if not login_url:
#             login_url = settings.LOGIN_URL
#         login_url = resolve_url(login_url)
#         return render(request, "registration/login.html")


class ProjectManagerSignUpView(CreateView):
    model = Member
    form_class = ProjectManagerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'project_manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class MemberSignUpView(CreateView):
    model = Member
    form_class = MemberSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'member'
        return super().get_context_data(**kwargs)
 
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

def logout_then_login(request, login_url=None, current_app=None, extra_context=None):
    """
    Logs out the user if they are logged in. Then redirects to the log-in page.
    """
    if not login_url:
        login_url = settings.LOGIN_URL
    login_url = resolve_url(login_url)
    return logout(request, "registration/logout.html", current_app=current_app, extra_context=extra_context)

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
    categories = Category.objects.filter(project=project)
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
@csrf_exempt
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_complete = True
        task.save()
    return JsonResponse({"status": "ok", "data": None})

# post = request.POST.copy() # to make it mutable
# post['field'] = value
# # or set several values from dict
# post.update({'postvar': 'some_value', 'var': 'value'})
# # or set list
# post.setlist('list_var', ['some_value', 'other_value']))

# # and update original POST in the end
# request.POST = post

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
    
    