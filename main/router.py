from main.api.viewsets import EmployeeViewSet
from main.api.viewsets import AttendanceRecordViewSet
from main.api.viewsets import IncidenceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('attendance-records', AttendanceRecordViewSet)
router.register('incidences', IncidenceViewSet)
