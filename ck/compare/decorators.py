from functools import wraps
from django.core.exceptions import PermissionDenied


def admin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.groups.filter(name='Admin').exists():
            return function(request, *args, **kwargs)
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied()
    return wrap
