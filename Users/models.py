from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Instructor(models.Model):#Here we are creating a class inheriting from Model in models
    #In models, we have a class called Model and this class defines the characteristics of a model
    #Instructor will have all the characteristics of a model
    name=models.CharField(max_length=255)
    #2083 is the standard max length of urls