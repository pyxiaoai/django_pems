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
from django.urls import path

import Login_registapp
from Login_registapp import views
app_name='emsapp'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    path('login_l/', views.login_l, name='login_l'),
    path('regist_r/', views.regist_r, name='regist_r'),
    path('checkName/', views.checkName, name='checkName'),
    path('getcapthca/', views.getcapthca, name='getcapthca'),
    path('checkcaptcha/', views.checkcaptcha, name='checkcaptcha'),

]
