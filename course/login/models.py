from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class accountmanager(BaseUserManager):
    def create_user(self, username, password , NAME=""):
        if not username:
            raise ValueError("username required")

        user = self.model(
            username = username,
            NAME=NAME,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class account(AbstractBaseUser):

    NAME = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = accountmanager()

    def __str__(self):
        return self.username

    def has_perm(self , perm , obj = None):
        return self.is_admin

    def has_module_perms(self , app_label ):
        return True
