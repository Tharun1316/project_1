from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')
def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        upass = request.POST.get('password')
        ucpass = request.POST.get('confirm-password')
        my_user = User.objects.create_user(uname,uemail,upass)
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        user = authenticate(request,username=uname,password=upass)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username and password mismatch")
    return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login')