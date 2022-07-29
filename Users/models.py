from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    credits = models.SmallIntegerField()

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class Instructor(models.Model):  # Here we are creating a class inheriting from Model in models
    # In models, we have a class called Model and this class defines the characteristics of a model
    # Instructor will have all the characteristics of a model
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    Icode = models.CharField(max_length=11)
    mobile = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course)

    # 2083 is the standard max length of urls
    class Meta:
        ordering = ['Icode']

    def __str__(self):
        return self.Icode


class Student(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    entrynumber = models.CharField(max_length=11)
    mobile = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course)

    class Meta:
        ordering = ['entrynumber']

    def __str__(self):
        return self.entrynumber


class Admin(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    Adcode = models.CharField(max_length=11)
    mobile = models.CharField(max_length=10)

    class Meta:
        ordering = ['Adcode']

    def __str__(self):
        return self.Adcode
