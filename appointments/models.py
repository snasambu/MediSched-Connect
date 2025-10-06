from django.db import models
from users.models import CustomUser

class Appointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments_as_patient')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments_as_doctor')
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=(
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ), default='Scheduled')

    def __str__(self):
        return f"{self.patient.username} with {self.doctor.username} on {self.date}"
