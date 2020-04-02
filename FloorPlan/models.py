# from django.contrib.auth.models import AbstractUser
from users.models import Member
from django.db import models
from model_utils import Choices
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import datetime
from phone_field import PhoneField


class Category(models.Model):
	ProjectCategory = models.TextChoices('ProjectCategory', 'PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
	category = models.CharField(choices=ProjectCategory.choices, max_length=30, default='HOMEOWNER')
	
	def __str__(self):
		return f'{self.category}'

	class Meta:
		verbose_name = ('category')
		verbose_name_plural = ('categories')


class Project(models.Model):
	name = models.CharField(max_length=100, blank=True) 
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=400, blank=False)
	lot_number = models.CharField(max_length=100, blank=True) 
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return f'Address and/or Lot number:{self.address}, {self.lot_number}'

		class Meta:
			unique_together = ('name', 'categories',)

class Task(models.Model):
	task = models.TextField(max_length=300)
	category = models.ForeignKey(
		Category, on_delete=models.CASCADE, related_name='tasks')
	assignee = models.ForeignKey(
		Member, on_delete=models.CASCADE, related_name='tasks', default='')
	project = models.ForeignKey(
		Project, on_delete=models.CASCADE, related_name="tasks")
	is_complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.task} => {self.project}, {self.assignee}'
