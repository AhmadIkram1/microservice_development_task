from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    program_enrolled = models.CharField(max_length=100)
    
    def __str__(self):
       return (
         f"ID: {self.id},\n"
         f"Name: {self.name},\n"
         f"Email: {self.email},\n"
         f"Date Of Birth: {self.date_of_birth},\n"
         f"Program Enrolled: {self.program_enrolled}"
    )

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()
    
    def __str__(self):
        return (
            f"ID: {self.id},\n"
            f"Name: {self.name},\n"
            f"Instructor: {self.instructor},\n"
            f"Credits: {self.credits}"
    )

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    
    def __str__(self):
        return (
            f"Student: {self.student.name},\n"
            f"Course: {self.course.name},\n"
            f"Enrollment Date: {self.enrollment_date}"
    )

class Schedule(models.Model):
    course = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=20)
    
    def __str__(self):
        return (
            f"Course: {self.course},\n"
            f"Room: {self.room},\n"
            f"Day of Week: {self.day_of_week},\n"
            f"Start Time: {self.start_time},\n"
            f"End Time: {self.end_time}"
    )

