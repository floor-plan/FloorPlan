
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from FloorPlan import views
from FloorPlan.views import ProjectManagerSignUpView, MemberSignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view, name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/signup_as_pm/', ProjectManagerSignUpView.as_view(), name='project_manager_signup'),
    path('accounts/signup_as_member/', MemberSignUpView.as_view(), name='member_signup'),
    path('', views.dashboard, name = 'dashboard'),
    path('project/<int:pk>', views.project, name='project'),
    path('new-project/', views.new_project, name='new_project'),
    path('edit-project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),
    path('project/<int:pk>/new-task/', views.new_task, name='new_task'),
    path('project/edit-task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
    path('project/<int:pk>/add-team-member/', views.add_team_member, name='add_team_member'),
    path('delete-team-member/<int:pk>/', views.delete_team_member, name='delete_team_member'),
    path('complete_task/<int:pk>/', views.complete_task, name='complete_task'),
    path('project/<int:pk>/new-category/', views.new_category, name='new_category'),
    path('project/edit-category/<int:pk>/', views.edit_category, name='edit_category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete_category'),
    path('project/edit-category-customcategory/<int:pk>/', views.edit_category_customcategory, name='edit_category_customcategory'),
    path('delete-category-customcategory/<int:pk>/', views.delete_category_customcategory, name='delete_category_customcategory'),
    path('project/<int:pk>/new-task-customcategory/', views.new_task_customcategory, name='new_task_customcategory'),
    path('project/edit-task-customcategory/<int:pk>/', views.edit_task_customcategory, name='edit_task_customcategory'),
    
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

