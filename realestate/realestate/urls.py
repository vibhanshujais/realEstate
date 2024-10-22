"""
URL configuration for realestate project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from realestate.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login', login),
    path('register', register),
    path('dashboard',dashboard),
    path('logout', logout),
    path('flat', flat),
    path('farmhouse', fh),
    path('plot', plot),
    path('userdashboard',userdashboard),
    path('query', querymodel),
    path('f1',f1),
    path('f2',f2),
    path('f3',f3),
    path('f4',f4),
    path('f5',f5),
    path('f6',f6),
    path('book',fbook),
]
