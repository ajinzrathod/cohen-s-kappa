from django.conf import settings


def isAdmin(request):
    # if user.groups.filter(name__in=['Admin', 'group2']).exists()
    # OR
    if request.user.groups.filter(name='Admin').exists():
        return True
    if request.user.is_superuser:
        return True
    return False


def user_data(request):
    if request.user.is_authenticated:

        # Checking if admin
        # Source: https://stackoverflow.com/a/20110261/11605100
        admin_or_higher = isAdmin(request)

        data = {
            'project_name': settings.PROJECT_NAME,
            'admin_or_higher': admin_or_higher,
        }

    # # if user not authenticated
    else:
        data = {
            'project_name': settings.PROJECT_NAME,
        }
    return data
