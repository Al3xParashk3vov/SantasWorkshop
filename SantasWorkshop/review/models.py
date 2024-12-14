from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()
# Create your models here.
class KidStatus(models.Model):
    STATUS_CHOICES = [
        ('GOOD', 'Good Kid'),
        ('NAUGHTY', 'Naughty Kid'),
    ]

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='kid_statuses'
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='GOOD')

    def __str__(self):
        return f"{self.user.username} is a {self.get_status_display()}"
