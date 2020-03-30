
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from FloorPlan import views
from FloorPlan.views import SignUpView, ProjectManagerSignUpView, MemberSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('registration.backends.simple.urls')),
    # path('signup/', views.sign_up, name='sign_up'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/project_manager/', ProjectManagerSignUpView.as_view(), name='project_manager_signup'),
    path('accounts/signup/member/', MemberSignUpView.as_view(), name='member_signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.dashboard, name = 'dashboard'),
    path('project/<int:pk>', views.project, name='project'),
    path('new-project/', views.new_project, name='new_project'),
    path('edit-project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),
    path('project/<int:pk>/new-task/', views.new_task, name='new_task'),
    path('project/edit-task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
    path('project/<int:pk>/new-team-member/', views.new_team_member, name='new_team_member'),
    path('edit-team-member/<int:pk>/', views.edit_team_member, name='edit_team_member'),
    path('delete-team-member/<int:pk>/', views.delete_team_member, name='delete_team_member'),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

#Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
