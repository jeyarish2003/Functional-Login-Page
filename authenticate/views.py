from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request,"authenticate\index.html")
    
def signup(request):
    if request.method == "POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "Success")
        return redirect('login')
    return render(request,"authenticate\signup.html")
def logi(request):
    if request.method == "POST":
        username=request.POST["username"]
        pass1=request.POST["pass1"]
        user=authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname=user.first_name
            # return HttpResponse(fname)
            return render(request, "authenticate/index.html", {'fname': fname })
        else:
            messages.error(request, "Bad Credentials")
            return redirect('signup ')
    return render(request,"authenticate\login.html")
def logou(request):
    logout(request)
    return HttpResponse("Go out")