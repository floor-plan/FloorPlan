from phone_field import PhoneField
from django.db import models



class ProjectManager(models.Model):
	first_name = models.CharField(max_length=20, blank=False)
	last_name = models.CharField(max_length=20, blank=False)
	company = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=100, blank=False)
	phone = PhoneField(max_length=9, blank=False)

	def __str__(self):
		return f'Name:{self.first_name} {self.last_name} Company:{self.company} Phone Number:{self.phone}'


