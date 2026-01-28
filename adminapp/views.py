from django.shortcuts import render

# Create your views here.
def adminapphomepage(request):
    return render(request,'adminapp/projecthomepage.html')