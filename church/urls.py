from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about_us/', about_us, name='about_us'),
    path('unit_dept/', unit_dept, name='unit_dept'),
    path('submit_report/', submit_report, name='submit_report'),
    path('attendance/', attendance_view, name='attendance'),
    path('request_fund/', request_fund, name='request_fund'),
    path('approve_fund_request/<id>/', approve_fund_request,
         name='approve_fund_request'),
    path('decline_fund_request/<id>/', decline_fund_request,
         name='decline_fund_request'),
     path('declined_request_detail/<req_id>/', declined_request_detail, name='declined_request_detail'),

]
