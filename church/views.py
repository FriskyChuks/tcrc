from datetime import date
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
import random

from .models import *
from files.models import ImageGallery, CarouselImage
from profiles.models import CouncilMember


def home(request):
    council_members = CouncilMember.objects.all()
    members = MembershipRegister.objects.all()
    carousel_images = CarouselImage.objects.all()
    image = carousel_images[random.randint(0, len(carousel_images)-1)]
    media_staff = request.user.groups.filter(name='Media')
    gallery = ImageGallery.objects.all()
    gallery = random.sample([item for item in gallery], 4)
    unit_depts = UnitsAndDepartments.objects.all()
    activities = Activities.objects.all()
    upcoming_events = UpcomingEvent.objects.filter(start_date__gt=date.today())

    context = {"unit_depts": unit_depts, "media_staff": media_staff,
               "activities": activities, "gallery": gallery,"image": image,
               "council_members": council_members, "members": members,
               "upcoming_events":upcoming_events,
               }
    return render(request, 'church/index.html', context)


def about_us(request):
#     council_members = CouncilMember.objects.all()
#     members = MembershipRegister.objects.all()
#     context = {"council_members": council_members, "members": members}
    return render(request, 'church/about_us.html', {})


def unit_dept(request):
    unit_depts = UnitsAndDepartments.objects.all()
    context = {"unit_depts": unit_depts}
    return render(request, 'church/unit_dept.html', context)


def submit_report(request):
    pass
    return render(request, 'church/contact.html', {})


def contact(request):
    pass
    return render(request, 'church/contact.html', {})


def attendance_view(request):
    msg = ""
    unit_dept = MembershipRegister.objects.get(
        user_id=request.user.id).unit_dept
    attendance_list = Attendance.objects.filter(unit_dept__id=unit_dept.id)
    programs = Program.objects.filter(program_type='group')
    council_member = CouncilMember.objects.filter(user_id=request.user.id)
    if council_member or unit_dept.title == 'Ushering':
        programs = Program.objects.all()
        attendance_list = Attendance.objects.filter(unit_dept__isnull=True)
        unit_dept.id = ''
    if request.method == 'POST':
        program = request.POST.get('program')
        date = request.POST.get('date')
        time = request.POST.get('time')
        attendance = request.POST.get('attendance')
        comment = request.POST.get('comment')
        instance = Attendance.objects.create(program_id=program, date=date, time=time,
                                             attendance=attendance, unit_dept_id=unit_dept.id, comment=comment, created_by_id=request.user.id)
        instance.save()
        msg = 'Attndance saved sucessfully'

    context = {'programs': programs, "msg": msg, "unit_dept": unit_dept,
               'attendance_list': attendance_list}
    return render(request, 'church/attendance.html', context)


def request_fund(request):
    president = CouncilMember.objects.filter(
        user_id=request.user.id, office__title='President')
    request_list = FundRequest.objects.filter(
        created_by_id=request.user.id).order_by('-id')
    if president:
        request_list = FundRequest.objects.filter(
            approved=False, declined=False).order_by('-id')
    if request.method == 'POST':
        total_amount = request.POST.get('total_amount')
        request_details = request.POST.get('request_details')

        obj = FundRequest.objects.create(total_amount=total_amount, request_details=request_details,
                                         created_by_id=request.user.id)
        obj.save()
        return redirect('request_fund')
    contex = {'request_list': request_list, 'president': president}
    return render(request, 'church/request_fund.html', contex)


def approve_fund_request(request, id):
    FundRequest.objects.filter(id=id).update(approved=True)
    return redirect('request_fund')


def decline_fund_request(request, id):
    get_request = FundRequest.objects.get(id=id)
    FundRequest.objects.filter(id=id).update(declined=True)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        FundRequestDecline.objects.create(
            request_id=id, comment=comment, declined_by_id=request.user.id
        )
        return redirect('request_fund')
    context = {'request': get_request}
    return render(request, 'church/decline_request.html', context)


def declined_request_detail(request, req_id):
    declined_request = FundRequestDecline.objects.get(request_id=req_id)
    print(declined_request)
    context = {"declined_request": declined_request}
    return render(request, 'church/declined_request_detail.html', context)
