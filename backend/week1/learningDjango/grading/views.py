from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Grade
# Create your views here.
def index(request):
    if request.user.is_authenticated: #use auth cookies
        studentid = request.user.id
        grade = get_object_or_404(Grade, student_id = studentid)
        coursename = grade.grade
        score = grade.marks
        return HttpResponse("Your grade in " + coursename + " is " + str(score))
    else:
        return HttpResponse("You are not logged in.")