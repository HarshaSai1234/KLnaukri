from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
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
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect(adminapphomepage)
        else:
            print(form.errors)
    return render(request,'adminapp/signup.html',{'form':form})
def login_view(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = useraccount.objects.get(email=email)
            if check_password(password, user.password):
                print(password)
                request.session['user_id'] = user.email
                request.session['username'] = user.fname + " " + user.lname
                return redirect('adminapphomepage')
            else:
                error = "Invalid Password"
        except useraccount.DoesNotExist:
            error = "User does not exist"
        return render(request,'adminapp/login.html',{'error':error})
    return render(request,'adminapp/login.html')
def logout_view(request):
    request.session.flush()
    return redirect('adminapphomepage')
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
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            send_mail(
                subject="Feedback Submitted Successfully",
                message=(
                    f"Dear {feedback.student_name},\n\n"
                    "Thank you for submitting feedback "
                    "for your course at KL University.\n\n"
                    "Your response has been recorded successfully. - This is just a sample from PFSD Class on 23.3.26"
                ),
                from_email='amdeepakv@gmail.com',
                recipient_list=[feedback.student_email],
                fail_silently=False
            )
            return render(request,"adminapp/success.html")
    else:
        form = FeedbackForm()
    return render(request,"adminapp/feedback_form.html",{"form": form})