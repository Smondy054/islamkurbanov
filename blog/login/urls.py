from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('add_user/', views.add_user, name='add_user'),
]