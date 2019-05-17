from django.db import models


# TODO: Create models for logs once a incidence is modified, etc.
# Create your models here.
class Clocks(models.Model):
    """
    Model to save each biometric clock's ip

    ip (str): IPv4 format
    """
    ip = models.CharField(max_length=16)


class EmployeeAccount(models.Model):
    """
    Model to save the employee's account information, and includes a security measure to recover password

    username (str): Employee's username
    password (str): Employee's password
    passwordSalt (str):
    passwordHashAlgorithm (str): Stores the algorithm's name for reference
    passwordReminderToken (str):
    passwordReminderExpiration (str):
    """
    username = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=254)
    password = models.CharField(max_length=200)
    passwordSalt = models.CharField(blank=True, null=True, max_length=50)
    passwordHashAlgorithm = models.CharField(blank=True, null=True, max_length=50)
    passwordReminderToken = models.CharField(blank=True, null=True, max_length=100)
    passwordReminderExpiration = models.DateTimeField(blank=True, null=True)


class Employee(models.Model):
    """
    Model with Employee's general information

    name (str): Employee's name
    lastname (str): Employee's lastname
    """
    employeeAccountID = models.ForeignKey(EmployeeAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)


class AttendanceRecord(models.Model):
    """
    Model that holds the attendance records for all the employees

    employeeID (int): Reference to the employee
    register (DateTime): Complete timestamp of the record
    """
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    register = models.DateTimeField()


class Payroll(models.Model):
    """
    Model that links the payroll with the employee and the time period it covers

    employeeID (int): Reference to the employee
    hoursDeducted (int): The hours that were deducted from the payroll
    startDate (Date): Payroll's starting date
    endDate (Date): Payroll's ending date
    """
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hoursDeducted = models.PositiveSmallIntegerField()
    startDate = models.DateField()
    endDate = models.DateTimeField()


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
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    incidenceTypeID = models.ForeignKey(IncidenceType, on_delete=models.CASCADE)
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

    workTypeID (int): Stablishes if the work was a lecture or office job
    startDate (Date): Indicates the starting date for the lecture or office job
    endDate (Date): Marks the ending date for the lecture; if it's a office job it should be blank or a future date
    completed (bool): Indicates if the lecture was completed; semester ended so we don't query these anymore
    """
    workTypeID = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateTimeField(blank=True, null=True)
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
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workID = models.ForeignKey(Work, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    weekday = models.PositiveSmallIntegerField()


