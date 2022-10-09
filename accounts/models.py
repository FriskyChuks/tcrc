from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, Group
)

from profiles.models import MembershipRegister

class UserManager(BaseUserManager):
    def create_user(self, username, user=None,password=None, is_staff=False, is_admin=False, is_active=True):
        if not user:
            raise ValueError("User must be a registered member!")
        if not username:
            raise ValueError("User must have a username!")
        if not password:
            raise ValueError("Users must have password!")

        user_obj = self.model(
            user_id = user,
            username = username,
            password = password
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj


    def create_staff(self, username, user=None, password=None):
        user = self.create_user(
            username,
            user_id=user,
            password=password,
            is_staff=True
        )
        return user


    def create_superuser(self, username, user=None, password=None):
        user = self.create_user(
            username,
            user_id=user,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user



class User(AbstractBaseUser):
    # image           = models.ImageField(null=True, blank=True, upload_to="users/")
    user            = models.OneToOneField(MembershipRegister, on_delete=models.CASCADE)
    username		= models.CharField(max_length=225, unique=True)
    active 			= models.BooleanField(default=True)
    staff 			= models.BooleanField(default=False)
    admin			= models.BooleanField(default=False)
    group 			= models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    timestamp 		= models.DateTimeField(auto_now_add=True, auto_now=False)

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ["user"]

    objects = UserManager()

    def __str__(self):
        return self.username

    # def get_full_name(self):
    #     return str(self.user) + " " + str(self.last_name)
    
    def get_short_name(self):
        return self.user

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
