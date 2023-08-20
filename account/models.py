import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    AGE_CHOICES = [
        ("all", "All"),
        ("kids", "Kids"),
    ]
    age_limit = models.CharField(
        choices=AGE_CHOICES,
        max_length=10,
    )

    @property
    def is_kid(self):
        return self.age_limit == "kids"
