from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('shiftchange/', views.shiftC, name='shiftchange'),
    path('notifications/', views.notifications, name='notifications'),
]
