"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from FloorPlan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # doesn't this one need to be 'views.projects, name=projects'
    path('', views.dashboard, name = 'dashboard'),
    path('project/<int:pk>', views.project, name='project'),
    path('new-project', views.new_project, name='new_project'),
    path('edit-project/<int:pk>', views.edit_project, name='edit_project'),
    path('delete-project/<int:pk>', views.delete_project, name='delete-project'),
    path('project/new-task/<int:pk>', views.new_task, name='new_task'),
    path('edit-task/<int:pk>', views.edit_task, name='edit_task'),
    path('delete-task/<int:pk>', views.delete_task, name='delete_task'),
    path('new-team-member/<int:pk>', views.new_team_member, name='new_team_memeber'),
    path('edit-team-member/<int:pk>', views.edit_team_member, name='edit_team_member'),
    path('delete-team-member/<int:pk>', views.delete_team_member, name='delete_team_member'),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
