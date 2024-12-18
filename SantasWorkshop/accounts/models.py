import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.core.validators import MaxValueValidator
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

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Ensure username only contains letters, numbers, and underscores
        if not re.match(r'^\w+$', username):
            raise forms.ValidationError("Username can only contain letters, numbers, and underscores.")

        # Additional rule (optional): Minimum length for username
        if len(username) < 5:
            raise forms.ValidationError("Username must be at least 5 characters long.")

        return username

    def clean(self):
        # Access the 'username' directly from the model instance, not from cleaned_data
        if not re.match(r'^\w+$', self.username):
            raise forms.ValidationError("Username can only contain letters, numbers, and underscores.")

        if len(self.username) < 5:
            raise forms.ValidationError("Username must be at least 5 characters long.")

        return super().clean()



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
        validators=[
            MaxValueValidator(100),
        ],
        blank=True,
        null=True,
        default=None,
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

    @property
    def presents_count(self):
        """Returns the number of presents created by this user"""
        return self.user.presents.count()

    def __str__(self):
        return f"{self.user.username}'s profile"