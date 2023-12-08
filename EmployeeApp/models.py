from django.db import models

# Create your models here.
class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

    def __str__(self):
        return self.DepartmentName
    
class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField()
    Department = models.ForeignKey(Department, related_name="employee", on_delete=models.CASCADE)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
