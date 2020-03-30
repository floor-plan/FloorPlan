from django.contrib.auth.models import AbstractUser
from django.db import models


    
class Member(AbstractUser):
    is_project_manager = models.BooleanField('project_manager status', default=False)
    is_member = models.BooleanField('member status', default=False)


# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model

    





