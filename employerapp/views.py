from django.shortcuts import *
from .models import *


# Create your views here.
def employerhomepage(request):
    return render(request,'employerapp/employerhomepage.html')
def crudfunction(request):
    employees = Employerdetails.objects.all()
    return render(request,'employerapp/crudfunction.html', {'employees':employees})
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

        add=Employerdetails(
            empid=empid,
            empname=empname,
            emplocation=emploc,
            empphone=empphone,
            empemail=empemail
        )
        add.save()
        return redirect('crudfunction')

    return render(request,'employerapp/crudfunction.html')
def read_employee(request):
    employees = Employerdetails.objects.all()
    selected_emp=None
    if request.method=="POST":
        read_empid=request.POST.get('read_empid')
        selected_emp=Employerdetails.objects.filter(empid=read_empid).first()
    context={
        'employees':employees,
        'selected_emp':selected_emp
    }
    return render(request,'employerapp/crudfunction.html',context)

def update_employee(request):
    employees=Employerdetails.objects.all()
    selected_emp=None
    message= None
    if request.method=="POST":
        empid=request.POST.get('empid')
        selected_emp=Employerdetails.objects.filter(empid=empid).first()
        if "fetch" in request.POST:
            pass
        elif "update" in request.POST:
            selected_emp.empname=request.POST.get('empname')
            selected_emp.emplocation=request.POST.get('emplocation')
            selected_emp.empphone=request.POST.get('empphone')
            selected_emp.empemail=request.POST.get('empemail')
            selected_emp.save()
            message = "Employee updated successfully"
    return render(request,'employerapp/crudfunction.html',{
        'employees':employees,
        "update_emp": selected_emp,
        "update_msg": message
    })

def delete_employee(request):
    employees = Employerdetails.objects.all()
    message = None

    if request.method == "POST":
        empid = request.POST.get("empid")
        emp = Employerdetails.objects.filter(empid=empid).first()

        if emp:
            emp.delete()
            message = f"Employee {empid} deleted successfully"
        else:
            message = "Employee not found"

    return render(request, "employerapp/crudfunction.html", {
        "employees": employees,
        "delete_msg": message
    })