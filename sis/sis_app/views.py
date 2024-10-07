# To handle views and redirects
from django.shortcuts import render, redirect
# To Import auth functions form Django
from django.contrib.auth import authenticate, login, logout
# The login_required decorator to protect views
from django.contrib.auth.decorators import login_required
# For class-based views[CBV]
from django.contrib.auth.mixins import LoginRequiredMixin
# For class-based views[CBV]
from django.views import View
#  Import the User class (model)
from django.contrib.auth.models import User
# Import the RegisterForm from forms.py
from .forms import *
import requests
import json
import xml.etree.ElementTree as ET
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(['GET'])
def get_enrolled_students(request):
    enrollments = Enrollment.objects.all()
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_courses(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)

def register_view(request):
    if request.method == "POST":
        # Directly grab form data from POST request
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        
        # Perform validation (you can use a helper function if needed)
        errors = {}
        if password != password_confirm:
            errors['password'] = "Passwords do not match!"

        if User.objects.filter(username=username).exists():
            errors['username'] = "Username already taken!"

        if User.objects.filter(email=email).exists():
            errors['email'] = "Email already registered!"

        # If there are no errors, create the user
        if not errors:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)  # Automatically log the user in
            return redirect('home')
        else:
            # If there are errors, re-render the template with error messages
            return render(request, 'register.html', {'errors': errors})
    else:
        return render(request, 'register.html')


def login_view(request):
    error_message = None 
    if request.method == "POST":  
        username = request.POST.get("username")  
        password = request.POST.get("password")  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'  
            return redirect(next_url) 
        else:
            error_message = "Invalid credentials"  
    return render(request, 'login.html', {'error': error_message})

    
def logout_view(request):
    logout(request)
    return redirect('login')

# Home View
# Using the decorator 
@login_required
def home_view(request):
    return render(request, 'home.html')

#CRUD Student
@login_required
def student_create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'student_form.html', {'form':form})

@login_required
def student_read_view(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students':students})

@login_required
def student_update_view(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'student_form.html', {'form':form})

@login_required
def student_delete_view(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        #student.save()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student':student})

# Crud Course
@login_required
def course_create_view(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    return render(request, 'course_form.html', {'form': form})

@login_required
def course_read_view(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def course_update_view(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    return render(request, 'course_form.html', {'form': form})

@login_required
def course_delete_view(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})


#Enrollment Crud
@login_required
def enrollment_create_view(request):
    form = EnrollmentForm()
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    return render(request, 'enrollment_form.html', {'form': form})

@login_required
def enrollment_read_view(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})

@login_required
def enrollment_update_view(request, id):
    enrollment = Enrollment.objects.get(id=id)
    form = EnrollmentForm(instance=enrollment)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    return render(request, 'enrollment_form.html', {'form': form})

@login_required
def enrollment_delete_view(request, id):
    enrollment = Enrollment.objects.get(id=id)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')
    return render(request, 'enrollment_confirm_delete.html', {'enrollment': enrollment})


#Schedule Crud
@login_required
def schedule_create_view(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    return render(request, 'schedule_form.html', {'form': form})

@login_required
def schedule_read_view(request):
    api_url = 'http://127.0.0.1:8000/api/schedules/'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            # Parse the JSON response
            schedules_data = response.json()  # This will give you a list of schedule entries

            for schedule_data in schedules_data:
                print(schedule_data)
                # Update or create the schedule in the database
                Schedule.objects.update_or_create(
                    id=schedule_data['id'],  # Use the ID for updating
                    defaults={
                        'course': schedule_data['course'],
                        'start_time': schedule_data['start_time'],
                        'end_time': schedule_data['end_time'],
                        'day_of_week': schedule_data['day_of_week'],
                        'room': schedule_data['room_name'],  # Foreign key reference to Room
                    }
                )

            schedules = Schedule.objects.all()  # Fetch all schedules for rendering
        else:
            schedules = []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        schedules = []

    return render(request, 'schedule_list.html', {'schedules': schedules})


@login_required
def schedule_update_view(request, id):
    schedule = Schedule.objects.get(id=id)
    form = ScheduleForm(instance=schedule)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    return render(request, 'schedule_form.html', {'form': form})

@login_required
def schedule_delete_view(request, id):
    schedule = Schedule.objects.get(id=id)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'schedule_confirm_delete.html', {'schedule': schedule})

# Protected View 
# class ProtectedView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     # 'next' - to redirect URL
#     redirect_field_name = 'redirect_to'
    
#     def get(self, request):
#         return render(request, 'protected.html')