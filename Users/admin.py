from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('entrynumber', 'name')


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('Icode', 'name')


class AdminAdmin(admin.ModelAdmin):
    list_display = ('Adcode', 'name')


# REGISTER MODELS
admin.site.register(Student, StudentAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
