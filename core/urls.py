"""core URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('jet_api/', include('jet_django.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('api/user/', include('account.urls')),
    # path('api/',include('account.urls')),
    path('api/garden/',include('garden.urls')),
    path('api/employee/',include('employee_information.urls')),
    path('api/complaint/',include('complaint_management.urls')),
    path('api/feeds/',include('feeds.urls')),
    path('api/forum/',include('forum.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
