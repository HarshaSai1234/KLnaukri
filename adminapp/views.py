from django.shortcuts import render, redirect
import pytz
import datetime
from .forms import *
import requests
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
def weather(request):
    weather_data = {}
    error_message = ""
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "8ec3d097351776f106143537273d2b8f"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if "main" in response:
            weather_data = {
                "city": city,
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"],
                "humidity": response["main"]["humidity"]
            }
        else:
            error_message = "Wrong Input / No City Found"
    return render(request, "adminapp/weather.html", {
        "weather": weather_data,
        "error": error_message
    })
    return render(request,'adminapp/weather.html')