from django.shortcuts import render
from .models import EmployeeFields,File
import pandas as pd
# Create your views here.
def database(filepath):
    df=pd.read_csv(filepath,delimiter=",")
    print(df)
    list_df=[list(row) for row in df.values]
    print(list_df)
    for i in list_df:
        instance,created=EmployeeFields.objects.get_or_create(employee_id=i[0])
        if not created:
            instance.employee_id=i[0]
            instance.first_name=i[1]
            instance.last_name=i[2]
            instance.email=i[3]
            instance.gender=i[4]
            instance.Number=i[5]
            instance.Address=i[6]
            instance.save()
       
def htmltest(request):
    return render(request,'index.html')
def uploadfile(request):
    if request.method=='POST':
        files=request.FILES['file']
        obj=File.objects.create(file=files)
        database(obj.file)
    return render(request,'index.html')
                            
        