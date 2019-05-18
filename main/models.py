from django.db import models


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
    full_name = models.CharField(unique=True, max_length=200)


class AttendanceRecord(models.Model):
    """
    Model that holds the attendance records for all the employees

    employeeID (int): Reference to the employee
    register (DateTime): Complete timestamp of the record
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    register = models.DateTimeField()


class Payroll(models.Model):
    """
    Model that links the payroll with the employee and the time period it covers

    employeeID (int): Reference to the employee
    hoursDeducted (int): The hours that were deducted from the payroll
    startDate (Date): Payroll's starting date
    endDate (Date): Payroll's ending date
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hours_deducted = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateTimeField()


class IncidenceType(models.Model):
    """
    NOTE: This is a reference table/model, it doesn't create more rows than the HR's rules for incidences
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
    Model that holds track/records of all the incidences that were made by the employee. Then when a new payroll is
    generated, it'll make a query and stablish the employee's discounted hours

    employeeID (int): Reference to the employee
    incidenceTypeID (int): Reference to the type of incidence
    date (Date): Marks the day that the incidence was made
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    incidence_type = models.ForeignKey(IncidenceType, on_delete=models.CASCADE)
    date = models.DateField()


class WorkType(models.Model):
    """
    Model to determine if it was a lecture or office work

    name (str): Lecture's name. E.g.: Principios electricos
    description (str): A brief description
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)


class Work(models.Model):
    """
    Model to track the period of time of lectures, and once a semester finishes it's archived with completed flag

    work_type (int): (ID)Stablishes if the work was a lecture or office job
    start_date (Date): Indicates the starting date for the lecture or office job
    end_date (Date): Marks the ending date for the lecture; if it's a office job it should be blank or a future date
    completed (bool): Indicates if the lecture was completed; semester ended so we don't query these anymore
    """
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField()


class WorkSchedule(models.Model):
    """
    Model to get the time period when classes were instructed

    employeeID (int): Reference to the employee
    workTypeID (int): Stablishes if the work was a lecture or office job
    weekday (int): Saves a positive integer value to link between a weekday:
                    Monday = 0
                    Tuesday = 1
                    Wednesday = 2
                    Thursday = 3
                    Friday = 4
                    Saturday = 5
    startTime (DateTime): Lecture's starting hour
    endTime (DateTime): Lecture's ending hour
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    weekday = models.PositiveSmallIntegerField()


