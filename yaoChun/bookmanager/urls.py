from django.urls import path,include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register/',register,name='register'),
]