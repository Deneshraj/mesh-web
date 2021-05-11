import uuid

from datetime import datetime
from django.db import models
from utils.config import default_profile_pic_url

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    profile_pic_url = models.TextField(max_length=255, default=None, null=True, blank=True)
    friends = models.ManyToManyField("self", blank=True, auto_created=False, editable=True)
    active = models.BooleanField(default=True)
    socket_id = models.CharField(default=None, null=True, unique=True, blank=True, max_length=30)

    def __str__(self):
        return f"{self.username}"

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'dateCreated': str(self.date_created),
            'verified': self.verified,
            'profilePicUrl': self.profile_pic_url
        }
