from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomManager(UserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Phone is required")
        
        user = self.model(
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(phone, password, **extra_fields)


class UserRole(models.TextChoices):
    ADMIN = ("admin", "Admin")
    MANAGER = ("manager", "Manager")
    CUSTOMER = ("customer", "Customer")
    

class User(AbstractUser):
    username = None
    phone = models.CharField(
        max_length=20,
        unique=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER,
    )

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
    objects = CustomManager()

    def __str__(self):
        return self.phone
