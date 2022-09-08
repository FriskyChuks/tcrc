from django.shortcuts import render

def home(request):
    pass
    return render(request, 'church/index.html',{})

def about_us(request):
    pass
    return render(request, 'church/single.html',{})

def unit_dept(request):
    pass
    return render(request, 'church/unit_dept.html',{})

def submit_report(request):
    pass
    return render(request, 'church/contact.html',{})

def contact(request):
    pass
    return render(request, 'church/contact.html',{})
