from django.db import models

class EmpData(models.Model):
    Fullname = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Location = models.CharField(max_length=100)
