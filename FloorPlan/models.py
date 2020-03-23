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
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    join_project = models.BooleanField(default=True)

    def __str__(self):
        return self.role


class Project(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=400, blank=False)
	lot_number = models.CharField(max_length=100, blank=True)
	owner = models.ForeignKey(
		ProjectManager, on_delete=models.CASCADE, related_name='projects')

	def __str__(self):
		return f'Address and/or Lot number:{self.address}, {self.lot_number}'







