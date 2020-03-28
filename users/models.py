from django.db import models
from django.contrib.auth.models import AbstractUser



# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    UserRole = models.TextChoices('UserRole', 'PROJECT-MANAGER SUPPLIER SUB-CONTRACTOR HOMEOWNER')
    role = models.CharField(blank=False, choices=UserRole.choices, max_length=30, default='misc')
    UserCategory = models.TextChoices('UserCategory', 'PROJECT-MANAGER PLUMBING ELECTRICAL MASONRY FRAMING ROOFING HOMEOWNER')
    category = models.CharField(blank=False, choices=UserCategory.choices, max_length=30, default='misc')
    is_project_manager = models.BooleanField(default=False)
                
    def __str__(self):
        return f'{self.username}'
        # , {self.UserRole}, {self.UserCategory}



