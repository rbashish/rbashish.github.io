"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

#Add URL maps to redirect the base URL to our application
""" from django.views.generic import RedirectView
from django.urls import path 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(url='home/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) """




from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    #path('', views.index),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path("", include("singlepage.urls")),
] 
