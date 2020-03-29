from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import Choices
from django.utils import timezone
from phone_field import PhoneField



class User(AbstractUser):
    is_project_manager = models.BooleanField('project_manager status', default=False)
    is_member = models.BooleanField('member status', default=False)

class Category(models.Model):
	ProjectCategory = models.TextChoices('ProjectCategory', 'PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
	category = models.CharField(choices=ProjectCategory.choices, max_length=30, default='HOMEOWNER')
	def __str__(self):
		return f'{self.category}'

	class Meta:
		verbose_name = ('category')
		verbose_name_plural = ('categories')
		constraints = [models.UniqueConstraint(
		fields=['category', 'project'], name='unique_team'),
		]


class Project(models.Model):
	name = models.CharField(max_length=100, blank=True) 
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=400, blank=False)
	lot_number = models.CharField(max_length=100, blank=True) 
	# category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', default='')
	def __str__(self):
		return f'Address and/or Lot number:{self.address}, {self.lot_number}'



class Profile(models.Model):
	# profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles', default='')
	email = models.EmailField(max_length=254, unique=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="profile_members")
	UserRole = models.TextChoices('UserRole', 'PROJECT-MANAGER SUPPLIER SUB-CONTRACTOR HOMEOWNER')
	role = models.CharField(blank=False, choices=UserRole.choices, max_length=30, default='misc')
	UserCategory = models.TextChoices('UserCategory', 'PROJECT-MANAGER PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
	category = models.CharField(blank=False, choices=UserCategory.choices, max_length=30, default='misc')
	is_project_manager = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.email} => {self.project}'

class Task(models.Model):
	task = models.TextField(max_length=300)
	category = models.ForeignKey(
		Category, on_delete=models.CASCADE, related_name='tasks')
	assignee = models.ForeignKey(
		Profile, on_delete=models.CASCADE, related_name='tasks', default='')
	project = models.ForeignKey(
		Project, on_delete=models.CASCADE, related_name="tasks")
	#completed as boolean?
	def __str__(self):
		return f'{self.task} => {self.project}, {self.assignee}'
