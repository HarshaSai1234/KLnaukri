from django.shortcuts import render

# Create your views here.
def adminapphomepage(request):
    return render(request,'adminapp/projecthomepage.html')
def printer(request):
    if request.method == "POST":
        user_input = request.POST['klu']
    a1={'klu' : user_input}
    return render(request,'adminapp/printer.html',a1)