from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('logIn/',views.logIn,name='logIn'),
    path('signout/',views.signout,name='signout'),
]
