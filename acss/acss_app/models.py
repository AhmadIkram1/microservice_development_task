from django.db import models

# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    
    def __str__(self):
        return (
            f"Room ID: {self.id},\n"
            f"Room Name: {self.room_name},\n"
            f"Capacity: {self.capacity}"
    )

class Schedule(models.Model):
    course = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=20)
    
    
    def __str__(self):
        return (
            f"Course: {self.course},\n"
            f"Room: {self.room.room_name},\n"
            f"Day of Week: {self.day_of_week},\n"
            f"Start Time: {self.start_time},\n"
            f"End Time: {self.end_time}"
    )

class Enrollment(models.Model):
    student = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    enrollment_date = models.DateField()
    
    def __str__(self):
        return (
            f"Student ID: {self.student},\n"
            f"Course: {self.course},\n"
            f"Enrollment Date: {self.enrollment_date}"
    )
