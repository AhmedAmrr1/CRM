from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home(request):
    # check if the user is logging in

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        # Authentication
        user = authenticate (request , username = username , password = password)

        if user is not None: # user is valid
            login (request , user)
            messages.success(request , "Congartulations you have login succefully !")
            return redirect ("home")
        else:
            messages.error(request , "invalid ... Please Enter username & password again")


    return render (request , "home.html" , {})


def login_user (request):
    pass


def logout_user (request):

    logout (request)
    messages.success (request , "You Have Been Logged out...")
    return redirect ("home")



def register_user (request):
        if request.method == 'POST':
             form = SignUpForm(request.POST)  # here we are passing the data in the request
             if form.is_valid():
                  form.save()
                  # Auth And login
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password1']
                  user = authenticate(username = username , password = password)
                  login(request , user)
                  messages.success(request , "Welcome , You Have Succefully Registerd")
                  return redirect("home")
        else:
             form = SignUpForm()
             return render (request , "register.html" , {'form':form})
        return render (request , "register.html" , {'form':form})
