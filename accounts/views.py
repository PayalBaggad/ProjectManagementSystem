""" This file contains the views for the account app . """

# Create your views here.

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm 

User = get_user_model()
# later on if i want to change user model then i don"t need to change in code
# only change setting

#  Function Based Views

# def register(request):
#     """This function renders the Registration Form"""
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "registration/register.html", {"form": form})


# Class Based Views

class RegisterView(View):
    """This class renders the Registration Form"""
    
    def get(self, request):
        """ This method handles the GET Request"""
        form = UserRegistrationForm()
        return render(request, "accounts/register.html", {"form": form}) # render is used to convert dynamic values into static values
    
    def post(self, request):
        """ This method handles the POST Request """
        form  = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "User Created successfully. Please ask admin to activate your account")
            return redirect("login")
        return render(request, "accounts/register.html", {"form": form} )

