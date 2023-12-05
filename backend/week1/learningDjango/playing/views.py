from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# views are functions that take some request and create views- literally what the user sees

def index(request):
    return HttpResponse("Hello, world.")

def bye(request):
    return HttpResponse("Goodbye, world.")

def hi(request, username):
    return render(request, "hi.html", {'name': username})

# better way is to use templates