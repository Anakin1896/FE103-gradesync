from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    employee_id = models.CharField(unique=True, max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20)

    department = models.ForeignKey('core.Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
