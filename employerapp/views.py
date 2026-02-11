from django.shortcuts import render

# Create your views here.
def employerhomepage(request):
    return render(request,'employerapp/employerhomepage.html')
def crudfunction(request):
    return render(request,'employerapp/crudfunction.html')
