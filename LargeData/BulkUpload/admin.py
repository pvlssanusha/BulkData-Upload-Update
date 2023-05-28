from django.contrib import admin

# Register your models here.
from .models import EmployeeFields,File
class Employeeadmin(admin.ModelAdmin):
    list_display=('employee_id','first_name','last_name','email','gender','Number','Address')
admin.site.register(File)
admin.site.register(EmployeeFields,Employeeadmin)
