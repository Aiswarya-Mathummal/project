from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name=''),
    path('register',views.register,name='register'),
    path('details',views.details,name='details'),
]