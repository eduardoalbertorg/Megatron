from django.db import models
from django.contrib.auth.models import User


# TODO: Create models for logs once a incidence is modified, etc.
# Create your models here.
class Clocks(models.Model):
    """
    Model to save each biometric clock's ip

    ip (str): IPv4 format
    """
    ip = models.CharField(max_length=16)


class Employee(models.Model):
    """
    Model with Employee's general information

    full_name (str): Employee's full name since the clock registers it this way
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(unique=True, max_length=200)
    code = models.CharField(unique=True, max_length=10)

    def __str__(self):
        return f'{self.full_name}'


class AttendanceRecord(models.Model):
    """
    Model that holds the attendance records for all the employees

    employeeID (int): Reference to the employee
    register (DateTime): Complete timestamp of the record
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_record = models.DateTimeField()


class Payroll(models.Model):
    """
    Model that links the payroll with the employee
    and the time period it covers

    startDate (Date): Payroll's starting date
    endDate (Date): Payroll's ending date
    """
    start_date = models.DateField(unique=True)
    end_date = models.DateField(unique=True)


class HoursDeducted(models.Model):
    """
    Model to link the hours deducted form each payroll to the employee

    employee (int): Reference to the employee class/table
    payroll (int): Reference to the payroll class/table
    hoursDeducted (int): The hours that were deducted from the payroll
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    hours_deducted = models.PositiveSmallIntegerField()


class IncidenceType(models.Model):
    """
    NOTE: This is a reference table/model, it doesn't create more
    rows than the HR's rules for incidences

    Model to determine the type of incidences:
    0-10 mins -> Small incident
    11-15 mins -> Medium incidence

    name (str): Incidence's name
    description (str): Small description of the incidence
    """
    name = models.CharField(unique=True, max_length=200)
    description = models.CharField(max_length=250)


class Incidence(models.Model):
    """
    Model that holds track/records of all the incidences that
    were made by the employee. Then when a new payroll is
    generated, it'll make a query and stablish the employee's discounted hours

    employeeID (int): Reference to the employee
    incidenceTypeID (int): Reference to the type of incidence
    date (Date): Marks the day that the incidence was made
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    incidence_type = models.ForeignKey(IncidenceType, on_delete=models.CASCADE)
    date = models.DateField()


class Schedule(models.Model):
    """
    Model to get the time period when classes were instructed

    employeeID (int): Reference to the employee
    work_type (int): (ID)Stablishes if the work was a lecture or office job
    work_schedule (int): (ID)Reference to the schedule it followed
    start_date (Date): Indicates the starting date for
    the lecture or office job
    end_date (Date): Marks the ending date for the lecture;
    if it's a office job it should be blank or a future date
    completed (bool): Indicates if the lecture was completed;
    semester ended so we don't query these anymore
    weekday (int): Saves a positive integer value to link between a weekday:
                    Monday = 0
                    Tuesday = 1
                    Wednesday = 2
                    Thursday = 3
                    Friday = 4
                    Saturday = 5
    startTime (Time): Office, Guard, or Lecture's starting hour
    endTime (Time): Office, Guard, or Lecture's ending hour
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    weekday = models.PositiveSmallIntegerField()
    completed = models.BooleanField()
