from rest_framework import serializers
from .models import Students, Teachers, Course

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
        
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
