from django import forms
from .models import Project, Category, Task



class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'address', 'lot_number', 'owner', 'team_members']


class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['project', 'task', 'category', 'assignee']



# class NewTeamMemberForm(forms.ModelForm):
  # class Meta:
  #   model = User
  #   fields = ['role', 'category', 'is_project_manager']

