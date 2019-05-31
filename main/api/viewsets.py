from main.models import Employee, Incidence, AttendanceRecord
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from main.api.serializers import EmployeeSerializer, AttendanceRecordSerializer, IncidenceSerializer


# groups a set of views to:
# list, create, retrieve, update, partial_update, destroy


class AttendanceRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attendance records to be viewed or edited
    """
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecord


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited
    """
    queryset = Employee.objects.all()
    serializer_class = Employee


class IncidenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows incidences to be viewed or edited
    """
    queryset = Incidence.objects.all()
    serializer_class = Incidence