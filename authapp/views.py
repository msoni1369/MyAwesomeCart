from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import logout, authenticate, login
#from django.contrib.auth.models.AnonymousUser
# Create your views here.
def index(request):
    print(request.user)
    
    if request.user.is_anonymous:
        return redirect("login")
    return render(request, "Authapp-index.html")
def loginUser(request):
    if request.method=="POST":  
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            print("mayank")
            return redirect("/shop")
        else:
            # No backend authenticated the credentials
            return render(request, "Authapp-login.html")
    return render(request, "Authapp-Login.html")
def logoutUser(request):
    logout(request)
    return redirect("logout")