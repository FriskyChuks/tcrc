from django.db import models

GENDER = (
		('male', 'Male'),
		('female', 'Female'),
	)

class MembershipRegister(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    othernames = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname


# class Executive(models.Model):
