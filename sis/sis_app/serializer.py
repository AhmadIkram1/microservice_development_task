from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.name', read_only=True)  # Fetch student name
    course = serializers.CharField(source='course.name', read_only=True)    # Fetch course name

    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'enrollment_date']  # Only include the desired fields

    
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'