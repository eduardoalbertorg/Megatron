from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.models import Employee
from main.models import AttendanceRecord
from main.models import Incidence
from main.models import IncidenceType


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'


class IncidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidence
        fields = '__all__'


class IncidenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidenceType
        fields = '__all__'
