from django.shortcuts import render

# Create your views here.
def employerhomepage(request):
    return render(request,'employerapp/employerhomepage.html')
