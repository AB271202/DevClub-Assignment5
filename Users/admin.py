from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display=('code','description', 'credits')


admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)