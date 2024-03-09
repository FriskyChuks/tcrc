from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User


class UnitsAndDepartments(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='group_images', blank=True, null=True)

    def __str__(self):
        return self.title


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)


class MembershipRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    othernames = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    unit_dept = models.ForeignKey(
        UnitsAndDepartments, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.user.first_name)


class CouncilOffice(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CouncilMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.ForeignKey(CouncilOffice, on_delete=models.CASCADE)
    date_created = models.DateField()

    def __str__(self):
        return f"{self.office} || {self.user}"
