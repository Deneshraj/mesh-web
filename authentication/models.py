import uuid

from datetime import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.email} {self.password} {self.date_created}"