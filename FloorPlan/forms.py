from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Project, Category, Task, Profile
from django.db import transaction

class ProjectManagerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_project_manager = True
        user.save()
        project_manager = ProjectManager.objects.create(user=user)
        project_manager.projects.add(*self.cleaned_data.get('projects'))
        return user

class MemberSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_member = True
        if commit:
            user.save()
        return user


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['address', 'lot_number', 'name']


class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['project', 'task', 'category', 'assignee']
    # need to add assignee back



class NewTeamMemberForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['email', 'project', 'role', 'category', 'is_project_manager']
    # removed 'profile' replaced with email

