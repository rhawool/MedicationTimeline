from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [

    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name="logout_user"),

]
