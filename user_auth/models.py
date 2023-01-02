from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        # if not password:
        #     raise ValueError(_("The password must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("role", 1)

        if extra_fields.get("role") != 1:
            raise ValueError("Superuser must have role of Global Admin")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """table which employee details are added"""

    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    GENDER_CHOICE = (
        ("Female", "Female"),
        ("Male", "Male"),
        ("Other", "Other"),
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICE,
        null=True,
        blank=True,
    )
    TYPE_CHOICE = (
        ("Primary", "Primary"),
        ("Secondary", "Secondary"),
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICE,
        null=True,
        blank=True,
    )
    ROLE_CHOICES = (
        (1, "Admin"),
        (2, "User"),
    )
    role = models.PositiveIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, default=2
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_date = models.DateTimeField(_("date joined"), default=timezone.now)
    updated_date = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()
