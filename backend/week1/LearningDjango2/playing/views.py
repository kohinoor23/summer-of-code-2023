from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the playing index.")

def hi1(request, username):
    return HttpResponse("Hello "+username)

def hi(request, username):
    return render(request, 'hi.html', {'name': username})