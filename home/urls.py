from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('searchLocation',views.searchLocation,name='searchLocation'),
    path('about/',views.about,name='about'),
]
