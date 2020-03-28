from phone_field import PhoneField
from django.db import models
from model_utils import Choices
# from django.contrib.auth.models import User
from users.models import User



class ProjectManager(models.Model):
	first_name = models.CharField(max_length=30, blank=False)
	last_name = models.CharField(max_length=30, blank=False)
	company = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=100, blank=False)
	phone = PhoneField(max_length=11, blank=False)

	def __str__(self):
		return f'Name:{self.first_name} {self.last_name} Company:{self.company} Phone Number:{self.phone}'

	
def get_project():
	return Project.objects.get(id=1)


class TeamMember(models.Model):
	title = models.CharField(max_length=100, blank=True)
	name = models.CharField(max_length=100)
	company = models.CharField(max_length=50, blank=True)
	join_project = models.BooleanField(default=True)
	team_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_members', default=1)

	def __str__(self):
		return f' Name:{self.name}, {self.title}, {self.company}'


class Project(models.Model):
	name = models.CharField(max_length=100, blank=True) 
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=400, blank=False)
	lot_number = models.CharField(max_length=100, blank=True)
	owner = models.ForeignKey(
		ProjectManager, on_delete=models.CASCADE, related_name='projects')
	team_members = models.ManyToManyField(TeamMember)

	def __str__(self):
		return f'Address and/or Lot number:{self.address}, {self.lot_number}'


class Role(models.Model):
	RoleType = models.TextChoices('RoleType', 'PROJECT-MANAGER SUPPLIER SUB-CONTRACTOR HOMEOWNER')
	role = models.CharField(blank=False, choices=RoleType.choices, max_length=30)
	member = models.ForeignKey(
		TeamMember, on_delete=models.CASCADE, related_name='roles')
	
	def __str__(self):
		return self.role

class Category(models.Model):
	CategoryType = models.TextChoices('CategoryType', 'PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
	category = models.CharField(blank=False, choices=CategoryType.choices, max_length=30, default='misc')
	member = models.ForeignKey(
		TeamMember, on_delete=models.CASCADE, related_name='categories')
	project = models.ForeignKey(
    Project, on_delete=models.CASCADE, related_name='categories', default='')

	
	def __str__(self):
		return self.category
	
	class Meta:
		constraints = [models.UniqueConstraint(
			fields=['category', 'project'], name='unique_team'),
	]
	

class Task(models.Model):
	task = models.TextField(max_length=300)
	category = models.ForeignKey(
		Category, on_delete=models.CASCADE, related_name='tasks')
	role = models.ForeignKey(
		Role, on_delete=models.CASCADE, related_name='tasks', default='')
	assignee = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name='tasks', default='')
	project = models.ForeignKey(
		Project, on_delete=models.CASCADE, related_name="tasks")


	def __str__(self):
		return f'{self.task} => {self.project}, {self.assignee}' 



		







