from django.db import models

# Create your models here.
#creating a model which have a attribute to store files 
class File(models.Model):
    file=models.FileField(upload_to='files')
    
class EmployeeFields(models.Model):
    employee_id=models.CharField(max_length=50,primary_key=True)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    gender=models.CharField(max_length=10)
    Number=models.CharField(max_length=10)
    Address=models.CharField(max_length=50)
    