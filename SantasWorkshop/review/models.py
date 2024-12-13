from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()
# Create your models here.
class KidStatus(models.Model):
    STATUS_CHOICES = [
        ('GOOD', 'Good Kid'),
        ('NAUGHTY', 'Naughty Kid'),
    ]

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='kid_status'
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='GOOD')
    notes = models.TextField(blank=True, null=True, help_text="Notes on why this user is naughty or good.")
    updated_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='status_updates'
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} is a {self.get_status_display()}"
