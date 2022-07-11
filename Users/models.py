from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Instructor(models.Model):  # Here we are creating a class inheriting from Model in models
    # In models, we have a class called Model and this class defines the characteristics of a model
    # Instructor will have all the characteristics of a model
    COURSECODES = ()
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=6, choices=COURSECODES)
    # 2083 is the standard max length of urls


class Student(models.Model):
    COURSECODES = ()
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=6, choices=COURSECODES)


class Course(models.Model):
    code = models.CharField(max_length=6)
    description = models.TextField()
    credits = models.SmallIntegerField()


class Admin(models.Model):
    pass
