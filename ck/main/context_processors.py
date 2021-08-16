from django.conf import settings


def user_data(request):
    if request.user.is_authenticated:

        # notification_count
        notification_count = 99
        if notification_count > 9:
            notification_count = "9+"
        else:
            # to string coz it will be compared in str in header.html
            notification_count = str(notification_count)

        data = {
            'project_name': settings.PROJECT_NAME,
            'notification_count': notification_count,
        }

    # # if user not authenticated
    else:
        data = {
            'project_name': settings.PROJECT_NAME,
            'notification_count': "0",
        }
    return data
