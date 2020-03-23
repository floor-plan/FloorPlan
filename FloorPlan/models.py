from phone_field import PhoneField
from django.db import models
from users.models import User


# Create your models here.
class Contractor(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    join_project = models.BooleanField(default=True)

    def __str__(self):
        return self.role



class ProjectManager(models.Model):
	first_name = models.CharField(max_length=20, blank=False)
	last_name = models.CharField(max_length=20, blank=False)
	company = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=100, blank=False)
	phone = PhoneField(max_length=9, blank=False)

	def __str__(self):
		return f'Name:{self.first_name} {self.last_name} Company:{self.company} Phone Number:{self.phone}'



