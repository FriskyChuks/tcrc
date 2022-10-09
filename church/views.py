from django.shortcuts import render

from . models import *

def home(request):
    unit_depts = UnitsAndDepartments.objects.all()
    context = {"unit_depts":unit_depts}
    return render(request, 'church/index.html',context)

def about_us(request):
    pass
    return render(request, 'church/single.html',{})

def unit_dept(request):
    unit_depts = UnitsAndDepartments.objects.all()
    context = {"unit_depts":unit_depts}
    return render(request, 'church/unit_dept.html',context)

def submit_report(request):
    pass
    return render(request, 'church/contact.html',{})

def contact(request):
    pass
    return render(request, 'church/contact.html',{})
