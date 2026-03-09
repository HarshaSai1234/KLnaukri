from django.shortcuts import render, redirect
import pytz
import datetime
from .forms import *

# Create your views here.
def adminapphomepage(request):
    return render(request,'adminapp/projecthomepage.html')
def printer(request):
    user_input=""
    if request.method == "POST":
        user_input = request.POST['klu']
    a1={'klu' : user_input}
    return render(request,'adminapp/printer.html',a1)
def timetable(request):
    return render(request,'adminapp/timetable.html')
def timezone1(request):
    if request.method=='POST':
        klu = request.POST.get('klu')
        timezone1 = pytz.timezone(klu)
        print("Current Time is : ",datetime.datetime.now(timezone1))
    return render(request,'adminapp/timezone1.html')
def signup(request):
    form=UserForm()
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(adminapphomepage)
        else:
            form=UserForm()
    return render(request,'adminapp/signup.html',{'form':form})