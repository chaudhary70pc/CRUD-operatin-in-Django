from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_code = models.IntegerField()
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    mobail = models.IntegerField()
    email =models.EmailField(max_length=30)
    
     
    
    