
from django.urls import path, include
from . import views

urlpatterns = [
            path("", views.index, name="home"),
            path("login",views.loginUser,name="login"),
            path("logout",views.logoutUser,name="logoff"),
            ]

