from django import forms
from .import models



class ProjectForm(forms.ModelForm):
  class Meta:
    model = models.Project
    fields = ['name', 'address', 'lot_number', 'owner', 'team_members']


  class TaskForm(forms.ModelForm):
    class Meta:
      model = models.Task
      fields = ['task', 'category', 'role', 'assignee']



  class NewTeamMemberForm(forms.ModelForm):
    class Meta:
      model = models.TeamMember
      fields = ['title', 'name', 'company', 'join_project']

