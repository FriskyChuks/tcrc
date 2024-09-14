from django.db import models
from django.contrib.auth.models import User

from profiles.models import *

PROGRAM_TYPE = (
    ('church', 'Church'),
    ('group', 'Group'),
)


class Program(models.Model):
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPE)
    title = models.CharField(max_length=225)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    time = models.TimeField()
    venue = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} | {self.start_date}-{self.time}"

class Attendance(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    unit_dept = models.ForeignKey(
        UnitsAndDepartments, on_delete=models.CASCADE, null=True, blank=True)
    attendance = models.IntegerField()
    comment = models.CharField(max_length=225, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.program} || {self.attendance}"


class Report(models.Model):
    purse = models.DecimalField(
        decimal_places=2, default='00.00', max_digits=20)
    fund = models.DecimalField(
        decimal_places=2, default='00.00', max_digits=20)
    chalenges = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField()

    def __str__(self):
        return f"{self.date_created} {self.created_by}"


class Activities(models.Model):
    title = models.CharField(max_length=100)
    days = models.CharField(max_length=15)
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class FundRequest(models.Model):
    total_amount = models.DecimalField(
        default=0.00, max_digits=65, decimal_places=2)
    request_details = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    request_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.total_amount)


class FundRequestApproval(models.Model):
    request = models.ForeignKey(FundRequest, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_approved = models.DateTimeField()

    def __str__(self):
        return str(self.approved_by)

class FundRequestDecline(models.Model):
    request = models.ForeignKey(FundRequest, on_delete=models.CASCADE)
    declined_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False,blank=False)
    date_declined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.declined_by)