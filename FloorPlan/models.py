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
