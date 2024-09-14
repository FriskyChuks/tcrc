from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import os


from .models import *


def membership_registration_view(request):
    msg = 'Kindly fill the form to register'
    unit_depts = UnitsAndDepartments.objects.all()
    if request.method == 'POST':
        if MembershipRegister.objects.filter(user_id=request.user.id).exists():
            msg = 'You are already registered!, See Admin to confirm'
            return redirect('membership')
        else:
            photo = request.FILES.get('photo')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            othernames = request.POST.get('othernames')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            unit_dept = request.POST.get('unit_dept')

            username = firstname.lower()
            if email:
                username = email
            if User.objects.filter(username=username).exists():
                msg = 'You are already registered!, See Admin to confirm'
                # put a new page here for error check
                return redirect('membership')
            user = User.objects.create(username=username, password='pass', email=email,
                                       first_name=firstname, last_name=lastname, is_active=False)
            user.set_password('pass')
            user.save()

            MembershipRegister.objects.create(
                photo=photo, user_id=user.id, othernames=othernames,
                phone=phone, address=address, unit_dept_id=unit_dept)
            msg = 'Registration successful!'
            return redirect('member_profile', user_id=user.id)

    return render(request, 'profiles/membership.html', {'msg': msg, 'unit_depts': unit_depts})


def member_profile_view(request, user_id):
    member = MembershipRegister.objects.get(user_id=user_id)
    context = {"member": member}
    return render(request, 'profiles/member_profile.html', context)


def update_member_profile_view(request, id):
    member = MembershipRegister.objects.get(id=id)
    unit_depts = UnitsAndDepartments.objects.all()

    if request.method == 'POST':
        User.objects.filter(id=member.user.id).update(
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            email = request.POST.get('email')
        )
        photo = request.FILES.get('photo')
        MembershipRegister.objects.filter(id=id).update(
            othernames = request.POST.get('othernames'),
            phone = request.POST.get('phone'),
            address = request.POST.get('address'),
            unit_dept_id = request.POST.get('unit_dept')
        )
        if photo:
            member.photo = photo
            member.save()
        return redirect('member_profile',member.user.id)
        
    context = {"member": member, "unit_depts": unit_depts}
    return render(request, 'profiles/update_profile.html', context)


def login_view(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        qs = User.objects.filter(username=username)
        if len(qs) < 1:
            msg = 'This user does not EXIST!'
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            msg = 'Wrong Password'
        else:
            if user:
                if not user.is_active:
                    msg = 'Inactive user, please contact the admin!'
                else:
                    login(request, user)
                    return redirect('home')

    return render(request, 'profiles/login.html', {"msg": msg})


def activate_user_view(request, id):
    msg = ''
    member = MembershipRegister.objects.get(user_id=id)
    council_member = CouncilMember.objects.filter(user_id=id)
    if council_member or member.unit_dept:
        User.objects.filter(id=id).update(is_active=True)
        msg = 'Activated successfully'
    elif not council_member:
        msg = 'Since the member is not a Council member, he/she must be assigned to a Unit/Dept'
        # return redirect('search')
    context = {'msg': msg}
    return render(request, "profiles/search_results.html", context)


def deactivate_user_view(request, id):
    msg = ''
    User.objects.filter(id=id).update(is_active=False)
    msg = 'De-activated successfully'
    context = {'msg': msg}
    return render(request, "profiles/search.html", context)


def update_user_view(request, id):
    member = MembershipRegister.objects.get(user_id=id)
    unit_depts = UnitsAndDepartments.objects.all()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        othernames = request.POST.get('othernames')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        unit_dept = request.POST.get('unit_dept')
        MembershipRegister.objects.filter(user_id=id).update(
            user_id=id, othernames=othernames, phone=phone, address=address,
            unit_dept_id=unit_dept)
        User.objects.filter(id=id).update(
            email=email, first_name=firstname, last_name=lastname)
        return redirect(reverse('search') + f'?q={firstname}')

    context = {"member": member, "unit_depts": unit_depts}
    return render(request, "profiles/update_user.html", context)


def search_user(request):
    council_members = None
    members = MembershipRegister.objects.all()
    for member in members:
        council_members = CouncilMember.objects.filter(user_id=member.user.id)
    try:
        query = request.GET.get('q')
    except:
        query = None
    lookups = (Q(email__iexact=query) | Q(first_name__icontains=query) |
               Q(last_name__icontains=query) | Q(username__iexact=query))
    if query:
        results = User.objects.filter(lookups).distinct()
        context = {'query': query, "results": results,
                   "members": members, "council_members": council_members}
        template = 'profiles/search_results.html'
    else:
        a = "Please enter a search parameter!"
        template = 'profiles/search_results.html'
        context = {'query1': a}
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('home')
