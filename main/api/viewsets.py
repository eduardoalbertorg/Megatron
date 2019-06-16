from main.models import Employee, Incidence, AttendanceRecord
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from main.api.serializers import EmployeeSerializer
from main.api.serializers import AttendanceRecordSerializer
from main.api.serializers import IncidenceSerializer


# groups a set of views to:
# list, create, retrieve, update, partial_update, destroy


class AttendanceRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attendance records to be viewed or edited
    """
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        This view should return a list of all the attendance records
        for the currently authenticated user.
        """
        user = self.request.user
        return AttendanceRecord.objects.filter(employee=user.employee)


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class IncidenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows incidences to be viewed or edited
    """
    queryset = Incidence.objects.all()
    serializer_class = IncidenceSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """
        This view should return a list of all the incidences
        for the currently authenticated user.
        """
        user = self.request.user
        return Incidence.objects.filter(employee=user.employee)
