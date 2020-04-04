from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Member
from .models import Project, Category, Task, ProjectCategory
from django.db import transaction


class ProjectManagerSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Member
		fields = ('first_name', 'last_name', 'username', 'email')

	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_member = True
		if commit:
			user.save()
		return user

class MemberSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Member
		fields = ('first_name', 'last_name', 'username', 'email', 'role', 'category')

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
    fields = ['project', 'task', 'category', 'assignee', 'due_date']

def __init__(self, *args, **kwargs):
	super().__init__(*args, **kwargs)
	self.fields['category'].queryset = ProjectCategories.objects.all()
    

class CategoryForm(forms.ModelForm):
  class Meta:
    model = ProjectCategory
    fields = ['category']




class AddTeamMemberForm(forms.ModelForm):
	queryset=Member.objects.all(),  #WE SHOULD LOOK AT THIS LATER!
	widget = forms.CheckboxSelectMultiple
	
	class Meta:
		model = Project
		fields = ['project_team']



class CompleteTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['is_complete', 'project']
