from django.contrib import admin
from .models import User, Project, Category, Task, Profile

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Profile)


# Register your models here.
