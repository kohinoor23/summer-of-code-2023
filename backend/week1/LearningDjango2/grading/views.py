from django.shortcuts import render
from .models import Grade
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.user.is_authenticated: # use inbuilt authentication, uses authcookies
        studentid = request.user.id #every user is assigned a serial using cookies via auth middleware
        grade = Grade.objects.get(student_id = studentid)
        coursename = grade.course
        marks = grade.marks
        return HttpResponse(f"You have scored {marks} marks in {coursename}.")
    else: 
        return HttpResponse("You are not logged in.")
        #redirect to login page