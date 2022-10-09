from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from profiles.models import MembershipRegister

def signup_view(request,membership_id):
    msg=""
    member = MembershipRegister.objects.get(id=membership_id)
    get_email = member.email
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            msg="Passwords do not match"
        else:
            user=User.objects.create(username=username,user_id=membership_id,password=password1)
            user.save()
            if not get_email:
                MembershipRegister.objects.filter(id=membership_id).update(email=email)
            msg="Successfully signed up!"

    context = {"msg":msg, "get_email":get_email}
    return render(request, "accounts/signup.html", context)
