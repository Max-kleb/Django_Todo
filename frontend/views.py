from django.shortcuts import render, redirect
from authentication.utils import verify_user

def home(request):
    user = verify_user(request)
    if not user: return redirect("/login")
    
    return render(request, 'index.html')


def login(request):
    user = verify_user(request)
    if user: return redirect("/")    

    return render(request, "login.html")


def signup(request):
    user = verify_user(request)
    if user: return redirect("/")
    return render(request, "signup.html")


def logout(request):
    user = verify_user(request)
    if not user:
        return redirect("/signup")

    user_datas = {
        "name": user.name,
        "email" : user.email
    }
    
    return render(request, "logout.html", user_datas)