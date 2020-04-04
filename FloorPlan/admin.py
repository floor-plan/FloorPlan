from django.contrib import admin
from .models import Project, Category, Task, ProjectCategory


admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(ProjectCategory)



# Register your models here.
