from django.contrib.auth import REDIRECT_FIELD_NAME


def project_manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a project manager,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = project_manager_only(
        lambda u: u.is_active and u.is_project_manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator