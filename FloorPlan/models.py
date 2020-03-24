from phone_field import PhoneField
from django.db import models
from users.models import User



class ProjectManager(models.Model):
	first_name = models.CharField(max_length=30, blank=False)
	last_name = models.CharField(max_length=30, blank=False)
	company = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=100, blank=False)
	phone = PhoneField(max_length=9, blank=False)

	def __str__(self):
		return f'Name:{self.first_name} {self.last_name} Company:{self.company} Phone Number:{self.phone}'


class TeamMember(models.Model):
	title = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=100)
	company = models.CharField(max_length=50, blank=True)
	join_project = models.BooleanField(default=True)
	# May need to remove following 4 lines
	# category = models.ForeignKey(
	# 	Category, on_delete=models.CASCADE, related_name='team_members')
	# role = models.ForeignKey(
	# 	Role, on_delete=CASCADE, related_name='team_members')
	# task = models.ForeignKey(
	# 	Task, on_delete=models.CASCADE, related_name='team_members')

	def __str__(self):
		return f' Name:{self.name}, {self.title}, {self.company}'


class Project(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=400, blank=False)
	lot_number = models.CharField(max_length=100, blank=True)
	owner = models.ForeignKey(
		ProjectManager, on_delete=models.CASCADE, related_name='projects')

	def __str__(self):
		return f'Address and/or Lot number:{self.address.pk}, {self.lot_number.pk}'


class Role(models.Model):
	RoleType = models.TextChoices('RoleType', 'SUPPLIER SUB-CONTRACTOR HOMEOWNER')
	role = models.CharField(blank=False, choices=RoleType.choices, max_length=30)
	member = models.ForeignKey(
		TeamMember, on_delete=models.CASCADE, related_name='roles')
	
	def __str__(self):
		return self.role

class Category(models.Model):
	CategoryType = models.TextChoices('CategoryType', 'PLUMBING ELECTRICAL MASONRY FRAMING ROOFING')
	category = models.CharField(blank=False, choices=CategoryType.choices, max_length=30, default='')
	member = models.ForeignKey(
		TeamMember, on_delete=models.CASCADE, related_name='categories')
	
	def __str__(self):
		return self.category
	

class Task(models.Model):
	task = models.TextField(max_length=300)
	category = models.ForeignKey(
		Category, on_delete=models.CASCADE, related_name='tasks')
	role = models.ForeignKey(
		Role, on_delete=models.CASCADE, related_name='tasks', default='')
	assignee = models.ForeignKey(
		TeamMember, on_delete=models.CASCADE, related_name='tasks', default='')
	
	def __str__(self):
		return f'{self.task.pk} done by {self.assignee.pk} => {self.role.pk}'



		







