"""jroget URL Configuration

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
from django.urls import include, path
from django.shortcuts import redirect
from welcome.views import *
from university.views import *
from semester.views import *

def redirect_view(request):
    response = redirect('welcome/')
    return response

urlpatterns = [
    path('', redirect_view),
    path('admin/', admin.site.urls),
    path('welcome/', welcome_index),
    path('university/', university_index),
    path('university/semester/<int:semester_number>', semester_index),
]
