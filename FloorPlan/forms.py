from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Member
from .models import Project, Category, Task
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
    

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['category']



class NewTeamMemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['role', 'category', 'is_project_manager']



class CompleteTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['is_complete', 'project']
