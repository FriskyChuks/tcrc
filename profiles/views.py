from django.shortcuts import render,redirect

from .models import *

def login_view(request):
    pass
    return render(request,'profiles/login.html',{})


def logout_view(request):
    pass
    return render(request,'profiles/logout.html',{})


def membership_registration_view(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        othernames = request.POST.get('othernames')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')

        MembershipRegister.objects.create(
            firstname=firstname,lastname=lastname,othernames=othernames,
            phone=phone,email=email,address=address
        )
        return redirect('membership')

    return render(request,'profiles/membership.html',{})
