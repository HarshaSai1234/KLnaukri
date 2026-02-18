from django.shortcuts import *
from .models import *


# Create your views here.
def employerhomepage(request):
    return render(request,'employerapp/employerhomepage.html')
def crudfunction(request):
    return render(request,'employerapp/crudfunction.html')
def crud_insert(request):
    if request.method=="POST":
        empid=request.POST['empid']
        empname=request.POST['empname']
        emploc=request.POST['emploc']
        empphone=request.POST['empphone']
        empemail=request.POST['empemail']
        print(empid)
        print(empname)
        print(emploc)
        print(empphone)
        print(empemail)
        redirect(crudfunction)

        add=Employerdetails(
            empid=empid,
            empname=empname,
            emplocation=emploc,
            empphone=empphone,
            empemail=empemail
        )
        add.save()
    return render(request,'employerapp/crudfunction.html')