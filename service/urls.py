from django.urls import path
from . import views

urlpatterns = [
    path('',views.services,name='service'),
    path('haveFlatForm/',views.haveFlatForm,name='haveFlatForm'),
    path('needFlatForm/',views.needFlatForm,name='needFlatForm'),
]
