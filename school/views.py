from rest_framework import generics
from .serializers import StudentSerializers, TeacherSerializers, CourseSerializers
from .models import Students, Teachers, Course

class StudentCreateView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers


class TeacherCreateView(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializers


class CourseCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


