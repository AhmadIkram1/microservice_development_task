from rest_framework import serializers
from .models import *

class ScheduleSerializer(serializers.ModelSerializer):
    room_name = serializers.CharField(source='room.room_name', read_only=True)
    class Meta:
        model = Schedule
        fields = ['id', 'course', 'room_name', 'start_time', 'end_time', 'day_of_week'] 