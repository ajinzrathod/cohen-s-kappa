"""ck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy

import debug_toolbar

admin.site.site_header = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),

    # accounts is social login
    path('accounts/', include('allauth.urls')),

    # main pages
    path('', include('main.urls')),

    # Tweets
    path('tweets/', include('tweet.urls')),

    # Compare
    path('compare/', include('compare.urls')),

    # APIs
    path('api/', include('api.urls')),

    path('__debug__/', include(debug_toolbar.urls)),

    # Contact
    path('contact/', include('contact.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403 = 'main.views.error_403'
handler500 = 'main.views.error_500'
handler404 = 'main.views.error_404'
