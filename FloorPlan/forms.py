from django import forms
from .models import Project, Category, Task, Profile
from users.models import User



class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'address', 'lot_number', 'category']


class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['project', 'task', 'category', 'assignee']



class NewTeamMemberForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['username', 'project', 'role', 'category', 'is_project_manager']

