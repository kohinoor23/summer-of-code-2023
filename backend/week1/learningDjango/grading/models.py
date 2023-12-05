from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Grade(models.Model):
    grade = models.CharField(max_length=10) #first name
    marks = models.IntegerField() #last name
    student = models.ForeignKey(User, on_delete=models.CASCADE) #if a user gets deleted, his grades are too (just a link to the user's id/existence)
    
