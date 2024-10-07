from django import forms
from .models import *
import requests

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        labels = {
            'room_name': 'Room Name',
            'capacity': 'Capacity',
        }
        widgets = {
            'room_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. Conference Room'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'E.g. 50'}),
        }
        
class ScheduleForm(forms.ModelForm):
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
            'room': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'day_of_week': forms.Select(choices=[
                ('', 'Select a day'),
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
                ('Saturday', 'Saturday'),
                ('Sunday', 'Sunday')
            ], attrs={'class': 'form-control'}),
        }
    course = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
        labels = {
            'student_id': 'Student ID',
            'course': 'Course',
            'enrollment_date': 'Enrollment Date',
        }
        widgets = {
            'student_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'E.g. 101'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. Mathematics'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }