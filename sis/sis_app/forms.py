from django import forms
from django.contrib.auth.models import User
from .models import *

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
#     email = forms.CharField(widget=forms.EmailInput, label="Email")

#     class Meta:
#         model = User
#         fields  = ['username', 'password', 'password_confirm','email']
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')
    
#         # Check if the passwords match
#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError("Passwords do not match!")
#         return cleaned_data
        
#sis logic

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        lables = {
            'name': 'Student Name',
            'email': 'Email',
            'date_of_birth': 'Date Of Birth',
            'program_enrolled': 'Program Enrolled'
        }
        
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder':'E.g Ali', 'class':'form-control' }),
            'email': forms.EmailInput(
                attrs={'placeholder':'E.g ali@gmail.com', 'class':'form-control' }),
            'date_of_birth': forms.DateInput(
                attrs={'placeholder': '2001-01-01', 'class': 'form-control', 'type': 'date'}),
            'program_enrolled': forms.TextInput(
                attrs={'placeholder':'BA', 'class':'form-control' }),
        }
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'name': 'Course Name',
            'instructor': 'Instructor',
            'credits': 'Credits',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'E.g Data Science', 'class': 'form-control'}),
            'instructor': forms.TextInput(
                attrs={'placeholder': 'E.g John Doe', 'class': 'form-control'}),
            'credits': forms.NumberInput(
                attrs={'placeholder': 'E.g 3', 'class': 'form-control'}),
        }
        
        
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
        labels = {
            'student': 'Student',
            'course': 'Course',
            'enrollment_date': 'Enrollment Date',
        }
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
class ScheduleForm(forms.ModelForm):
    # Define the choices for the days of the week
    DAYS_OF_WEEK = [
        ('', 'Select a day'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    # Override the day_of_week field to use a dropdown
    day_of_week = forms.ChoiceField(choices=DAYS_OF_WEEK, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Schedule
        fields = '__all__'
        labels = {
            'course': 'Course',
            'room': 'Room',
            'start_time': 'Start Time',
            'end_time': 'End Time',
            'day_of_week': 'Day of Week',
        }
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. Room 101'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }