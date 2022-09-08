from lib2to3.pgen2 import token
from tkinter import messagebox
from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User_profile
from django.core.mail import send_mail
from Ecomerce_project.settings import EMAIL_HOST_USER
from django.views.decorators.csrf import csrf_exempt
import random

# Home Page 
def home(request):
    return render(request,'Auth/base.html')

# Creating Register Page and Storing Data into DataBase
@csrf_exempt
@transaction.atomic
# @api_view(['POST'])    # Uncomment this to See in API view
def signup(request):
    if request.method == "POST":

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile'] 
        password = request.POST['password']
        password = make_password(password)

        users = User_profile.objects.create(username=username, email=email,first_name=first_name, last_name=last_name,mobile = mobile,password=password)
        generated_otp = random.randint(1000,9999)

 
        subject = 'OTP Verification is Pending'
        message = "Hello " + users.username +"," + " \n\n Welcome to Eshop  \n\n  " + f'Your One-Time Password { generated_otp}'
        recepient = users.email
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

        if generated_otp == int(input("Enter OTP")):
            users.save()
        else: 
            int(input("Enter Valid OTP"))
            
        return redirect('login')

    else:
        return render(request,'Auth/signup.html')

# Login Page 
@csrf_exempt
@transaction.atomic
# @api_view(['POST'])   # Uncomment this to See in API view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Sucessfully logged in")

            return redirect('home')
            
        else:
            return render (request,'Auth/login.html', {'error':'Username or password is incorrect!'})

    else:
        return render(request,'Auth/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

