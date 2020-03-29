from phone_field import PhoneField
from django.db import models
from model_utils import Choices
# from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser
from users.models import User


class Category(models.Model):
	ProjectCategory = models.TextChoices('ProjectCategory', 'PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
	category = models.CharField(choices=ProjectCategory.choices, max_length=30, default='HOMEOWNER')
	
	def __str__(self):
		return self.category
	
	# class Meta:
	# 	constraints = [models.UniqueConstraint(
	# 	fields=['category', 'project'], name='unique_team'),
	# 	]
		
class Project(models.Model):
	name = models.CharField(max_length=100, blank=True) 
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=400, blank=False)
	lot_number = models.CharField(max_length=100, blank=True) 
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', default='')

	def __str__(self):
		return f'Address and/or Lot number:{self.address}, {self.lot_number}'
    

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

class Profile(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles', default='')
	email = models.EmailField(max_length=254, unique=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="profiles")
	UserRole = models.TextChoices('UserRole', 'PROJECT-MANAGER SUPPLIER SUB-CONTRACTOR HOMEOWNER')
	role = models.CharField(blank=False, choices=UserRole.choices, max_length=30, default='misc')
	UserCategory = models.TextChoices('UserCategory', 'PROJECT-MANAGER PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
	category = models.CharField(blank=False, choices=UserCategory.choices, max_length=30, default='misc')
	is_project_manager = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.username}'
		




		







