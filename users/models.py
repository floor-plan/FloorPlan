from django.contrib.auth.models import AbstractUser
from django.db import models

  
class Member(AbstractUser):
    username = models.CharField(max_length=20, blank=False, unique=True)
    is_active = models.BooleanField(("active"), default=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    is_project_manager = models.BooleanField('project_manager status', default=False)
    is_member = models.BooleanField('member status', default=False)
    email = models.EmailField(max_length=254, unique=True)
    UserRole = models.TextChoices('UserRole', 'SUPPLIER SUB-CONTRACTOR HOMEOWNER')
    role = models.CharField(blank=False, choices=UserRole.choices, max_length=30, default='misc')
    UserCategory = models.TextChoices('UserCategory', 'PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
    category = models.CharField(blank=False, choices=UserCategory.choices, max_length=30, default='misc')
   
	
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []
    
    def __string__(self):
        return f'{self.first_name} {self.last_name}'

    





