import uuid

from django.db import models
from user.models import User

class AuthToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    auth_token = models.UUIDField(unique=True, default=uuid.uuid4)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.auth_token}"

    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'auth_token': str(self.auth_token),
            'date_created': str(self.date_created),
        }

class VerifyToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User requested Authentication")
    verify_token = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f"{self.verify_token}"
