#EDIT FILE

from django.urls import path
from . import views # . means 'current directory'

urlpatterns = [
    path("", views.index, name="index"), #default route -> /testApp/
    path("bob", views.bob, name="bob"), #/testApp/bob
    path("<str:name>", views.greet, name="greet") #custom route allowing any string -> #/testApp/NAME
]