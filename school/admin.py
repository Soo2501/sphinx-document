from django.contrib import admin
from .models import Teachers, Students, Course
# Register your models here.

admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Course)