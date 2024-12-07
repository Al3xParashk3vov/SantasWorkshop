from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.db import models

from SantasWorkshop.accounts.managers import AppUserManager

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'username'  # USERNAME_FIELD means the first credential in our auth
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        default=None
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True,
    )

    presents = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username}'s profile"