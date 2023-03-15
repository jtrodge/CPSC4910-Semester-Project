from django.shortcuts import render

#EDIT FILE BELOW
from django.http import HttpResponse

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world!")

#if you want to render an entire html file ->
def index(request):
    return render(request, "testApp/index.html")

def bob(request):
    return HttpResponse("Hello, bob!")

#def greet(request, name):
#    return HttpResponse(f"Hello, {name.capitalize()}!") #.capitalize() will capitalize the first character of a string

def greet(request, name):
    return render(request, "testApp/greet.html", {
        "name": name.capitalize() #variable sent to greet.html file
    })