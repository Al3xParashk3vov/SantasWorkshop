from django.db import models

# Create your models here.
class Present(models.Model):
    PRESENT_MAX_LENGTH = 40

    name = models.CharField(
        max_length=PRESENT_MAX_LENGTH,
        blank=False,
    )

    description = models.TextField(
        max_length=100,
        blank=False,
    )

    image = models.URLField(
        blank=False,
        help_text='Help Santa find this present!',
    )

    user = models.ForeignKey(
        to='accounts.Profile',
        on_delete=models.CASCADE,
        related_name='presents',
    )