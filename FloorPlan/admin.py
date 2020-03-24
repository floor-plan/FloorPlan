from django.contrib import admin
from .models import ProjectManager, TeamMember, Project, Role, Category, Task

admin.site.register(ProjectManager)
admin.site.register(TeamMember)
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Task)

# Register your models here.
