from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=6)
    description = models.TextField()
    credits = models.SmallIntegerField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class Instructor(models.Model):  # Here we are creating a class inheriting from Model in models
    # In models, we have a class called Model and this class defines the characteristics of a model
    # Instructor will have all the characteristics of a model
    name = models.CharField(max_length=255)
    Icode = models.CharField(max_length=11)
    mobile = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course)
    # 2083 is the standard max length of urls


class Student(models.Model):
    name = models.CharField(max_length=255)
    entrynumber = models.CharField(max_length=11)
    mobile=models.CharField(max_length=10)
    courses = models.ManyToManyField(Course)


class Admin(models.Model):
    pass
