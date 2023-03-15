from django.shortcuts import render
import requests

# Create your views here.
def ok(request):
    return render(request,'ok.html')


def home(request):
    response=requests.get('https://www.boredapi.com/api/activity').json()
    print(response)
    return render(request,'home.html',{'response':response}) 