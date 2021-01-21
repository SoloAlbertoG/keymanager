from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [

    # Sección para usuarios
    path('',views.index),
    path('index',views.index),
    path('welcome', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add', views.add),
    path('admin/', admin.site.urls),
]
