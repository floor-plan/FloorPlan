from django.contrib import admin
from .models import Project, Category, Task, User


admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(User)

# Register your models here.
