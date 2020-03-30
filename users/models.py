from django.contrib.auth.models import AbstractUser
from django.db import models


    
class Member(AbstractUser):
    is_project_manager = models.BooleanField('project_manager status', default=False)
    is_member = models.BooleanField('member status', default=False)
    email = models.EmailField(max_length=254, unique=True)
    UserRole = models.TextChoices('UserRole', 'PROJECT-MANAGER SUPPLIER SUB-CONTRACTOR HOMEOWNER')
    role = models.CharField(blank=False, choices=UserRole.choices, max_length=30, default='misc')
    UserCategory = models.TextChoices('UserCategory', 'PROJECT-MANAGER PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
    category = models.CharField(blank=False, choices=UserCategory.choices, max_length=30, default='misc')
	


# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model

    





