from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def HomePage(request):
    return render(request, 'HomePage.html')
def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user =User.objects.create_user(username,email,password)
        my_user.save()
        return redirect("login")
    else:
        return render(request, 'SignUp.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return redirect('HomePage')
    else:
        return render(request, 'login.html')
def LocationPage(request):
    return render(request, 'LocationPage.html')
def FoodPage(request):
    return render(request, 'FoodPage.html')
def logoutPage(request):
    logout(request)
    return redirect('login')
