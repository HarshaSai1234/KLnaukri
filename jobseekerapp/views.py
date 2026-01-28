from django.shortcuts import render

# Create your views here.
def jobseekerhomepage(request):
    return render(request,'jobseekerapp/jobseekerhomepage.html')
