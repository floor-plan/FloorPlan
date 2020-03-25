from django import forms
from .models import ProjectManager, TeamMember, Project, Role, Category, Task


class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'address', 'lot_number', 'owner', 'team_members']


  class TaskForm(forms.ModelForm):
    class Meta:
      model = Task
      fields = ['task', 'category', 'role', 'assignee']



  class NewTeamMemberForm(forms.ModelForm):
    class Meta:
      model = TeamMember
      fields = ['title', 'name', 'company', 'join_project']

