from phone_field import PhoneField
from django.db import models
from model_utils import Choices
# from django.contrib.auth.models import User
from users.models import User


class Project(models.Model):
	name = models.CharField(max_length=100, blank=True) 
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=400, blank=False)
	lot_number = models.CharField(max_length=100, blank=True)
	owner = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name='projects')
	team_members = models.ManyToManyField(User)

	def __str__(self):
		return f'Address and/or Lot number:{self.address}, {self.lot_number}'


class Category(models.Model):
	project = models.ForeignKey(
    	Project, on_delete=models.CASCADE, related_name='categories', default='')

	
	def __str__(self):
		return self.category
	
	# class Meta:
	# 	constraints = [models.UniqueConstraint(
	# 	fields=['category', 'project'], name='unique_team'),
	# 	]
		


class Task(models.Model):
	task = models.TextField(max_length=300)
	category = models.ForeignKey(
		Category, on_delete=models.CASCADE, related_name='tasks')
	assignee = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name='tasks', default='')
	project = models.ForeignKey(
		Project, on_delete=models.CASCADE, related_name="tasks")
	#completed as boolean?


	def __str__(self):
		return f'{self.task} => {self.project}, {self.assignee}'
		



		







