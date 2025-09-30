from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Patient-specific fields
    date_of_birth = models.DateField(null=True, blank=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)

    # Doctor-specific fields
    specialization = models.CharField(max_length=255, blank=True, null=True)
    availability = models.TextField(blank=True, null=True)  # optional JSON/slots

    def __str__(self):
        return f"{self.username} ({self.role})"
