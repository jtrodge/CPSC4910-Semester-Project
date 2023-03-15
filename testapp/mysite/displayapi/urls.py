from django.urls import path, include 
from . import views

urlpatterns = [
   path('vo',views.ok),
    path('',views.home,name = 'home'),
]