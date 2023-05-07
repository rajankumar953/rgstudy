from django.urls import path, include
from django import views
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Admin Login"
admin.site.site_title = "R G Publication"
admin.site.index_title = "Admin Portal"


urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
]
