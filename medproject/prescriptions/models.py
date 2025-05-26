import uuid
from django.db import models
from django.urls import reverse

class Prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_name = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    issued_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('prescription_detail', kwargs={'pk': self.pk})
