from django.contrib import admin

from .models import *

admin.site.register(Attendance)
admin.site.register(Program)
admin.site.register(Report)
admin.site.register(Activities)
admin.site.register(FundRequest)
admin.site.register(FundRequestApproval)
admin.site.register(FundRequestDecline)
admin.site.register(UpcomingEvent)