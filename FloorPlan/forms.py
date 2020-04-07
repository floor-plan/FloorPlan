from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Member
from .models import Project, Category, Task, ProjectCategory, ProjectCategoryTask
from django.db import transaction
import datetime


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

class DateInput(forms.DateInput):
	input_type = 'date'

	# def clean_date(self):
	# 	date = self.cleaned_data['date']
    #     if date < datetime.date.today():
	# 		raise forms.ValidationError("The date cannot be in the past!")
    # 	return date
	

class TaskForm(forms.ModelForm): 
	class Meta:
		model = Task
		widgets = {'due_date' : DateInput}
		fields = ['task', 'category', 'assignee', 'due_date']

	def clean_date(self):
		date = self.cleaned_data['due_date']
		if date < datetime.date.today():
			raise forms.ValidationError("The date cannot be in the past!")
		return date



class CustomCategoryTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		widgets = {'due_date' : DateInput}
		fields = ['task', 'custom_category', 'assignee', 'due_date']
    

class NewCategoryForm(forms.ModelForm):
	class Meta:
		model = ProjectCategory
		fields = ['category', 'project']




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
