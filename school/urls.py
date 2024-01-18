from django.urls import path
from .views import (
    StudentCreateView, 
    TeacherCreateView,
    CourseCreateView
)

urlpatterns = [
    path("student/", StudentCreateView.as_view(), name="student-list"),
    path("teacher/", TeacherCreateView.as_view(), name="teacher-list"),
    path("course/", CourseCreateView.as_view(), name="course-list"),
]
