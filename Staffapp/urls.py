"""django_pems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import Login_registapp
from Staffapp import views

app_name = "Staffapp"

urlpatterns = [
    path('emplist/', views.emplist, name='emplist'),
    path('updateEmp/', views.updateEmp, name='updateEmp'),
    path('addEmp/', views.addEmp, name='addEmp'),
    path('emplist_e/', views.emplist, name='emplist_e'),
    path('u/', views.u, name='u'),
    # path('addEmp_a/', views.addEmp, name='addEmp_a'),
    path('a/', views.a, name='a'),
    path('delete/', views.delete, name='delete'),
    path('exit/', views.exit, name='exit'),
    # path('checkname/',views.checkname,name='checkname')

]
