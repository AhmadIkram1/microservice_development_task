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
from django.views.decorators.cache import never_cache
#  Import the User class (model)
from django.contrib.auth.models import User
# Import the RegisterForm from forms.py
from .forms import *
from .models import *
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ScheduleSerializer
# Create your views here.

@api_view(['GET'])
def ScheduleListAPIView(request):
    schedule = Schedule.objects.all()
    serializer = ScheduleSerializer(schedule, many=True)
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


#Room Crud
@login_required
def room_create_view(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    return render(request, 'room_form.html', {'form': form})

@login_required
def room_read_view(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required
def room_update_view(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    return render(request, 'room_form.html', {'form': form})

@login_required
def room_delete_view(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'room_confirm_delete.html', {'room': room})


#Schedule Crud
@login_required
def schedule_create_view(request):
    api_url = 'http://127.0.0.1:8001/api/getcourses/'
    courses_choices = [('','Select a Course')]  
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            courses_data = response.json()
            courses_choices += [(course['name'], course['name']) for course in courses_data]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")  

    
    form = ScheduleForm()
    form.fields['course'].choices = courses_choices

    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        form.fields['course'].choices = courses_choices  
        form.save()
        return redirect('schedule_list')

    return render(request, 'schedule_form.html', {'form': form})


    # Pass the choices to the form dynamically
    form = ScheduleForm()
    form.fields['course'].widget.choices = courses_choices

    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    
    return render(request, 'schedule_form.html', {'form': form})

@login_required
def schedule_read_view(request):
    schedules = Schedule.objects.all()
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
    api_url = 'http://127.0.0.1:8001/api/getenrollments/'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            # Step 1: Delete all existing enrollments
            Enrollment.objects.all().delete()

            # Step 2: Fetch new enrollment data from the API
            enrollments_data = response.json()        
            for enrollment_data in enrollments_data:
                Enrollment.objects.create(
                    student=enrollment_data['student'],  # Assuming 'student_id' exists in the API response
                    course=enrollment_data['course'],    # Assuming 'course_id' exists in the API response
                    enrollment_date=enrollment_data['enrollment_date']
                )
              
            # Fetch all enrollments after the update
            enrollments = Enrollment.objects.all()
            print(enrollments)
        else:
            enrollments = []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        enrollments = []

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