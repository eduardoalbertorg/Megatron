from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.models import Employee, AttendanceRecord, Incidence


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('full_name', 'code')


class AttendanceRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ('employee', 'attendance_record')


class IncidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incidence
        fields = ('employee', 'incidence_type', 'date')
