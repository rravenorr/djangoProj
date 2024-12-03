from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('shiftchange/', views.shiftC, name='shiftchange'),
    path('notifications/', views.notifications, name='notifications'),
]
