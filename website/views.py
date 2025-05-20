from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import SignUpForm , AddRecordForm , UpdateForm
from .models import Record
# from django.contrib.auth.middleware import AuthenticationMiddleware

# Create your views here.

def home(request):
    # check if the user is logging in
    records = Record.objects.all() 
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        # Authentication
        user = authenticate (request , username = username , password = password)

        if user is not None: # user is valid
            login (request , user)
            messages.success(request, f"Login successful. Welcome back, {request.user.username}!") # "f" string formatting injects the name directly into the message.
            return redirect ("home")
        else:
            messages.error(request, "Invalid credentials. Please enter your username and password correctly.")
            return redirect ("home")
    else:
        return render (request , "home.html" , {'records':records})

         


def logout_user (request):

    logout (request)
    messages.success(request, "You have been logged out successfully.")
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
                  messages.success(request, "Registration completed successfully. Welcome!")
                  return redirect("home")
        else:
             form = SignUpForm()
             return render (request , "register.html" , {'form':form})
        return render (request , "register.html" , {'form':form})


def customer_record (request , pk):
     
     if request.user.is_authenticated:
          customer_record = Record.objects.get(id = pk)
          return render (request , "record.html" , {'customer_record':customer_record})
     
     else:
          messages.error(request, "You must be logged in to view this record.")
          return redirect ("home")



def delete_customer (request , pk):
     delete_record = Record.objects.get(id = pk)
     delete_record.delete()
     messages.success(request, "Customer deleted successfully.")
     return redirect ("home")



def add_customer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record added successfully.")
                return redirect("home")
        else:
            form = AddRecordForm()
        return render(request, "add_record.html", {'form': form})
    else:
        messages.error(request, "You must be logged in to add a customer.")
        return redirect("home")
    

def update_customer(request, pk):
    record = get_object_or_404(Record, id=pk)
    
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UpdateForm(request.POST, instance=record)
            if form.is_valid():
                form.save()
                messages.success(request, "Customer record updated successfully.")
                return redirect("home")
        else:
            form = UpdateForm(instance=record)

        return render(request, "update_record.html", {'form': form})

    else:
        messages.error(request, "You must be logged in to update records.")
        return redirect("home")


