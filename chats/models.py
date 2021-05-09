import uuid

from django.db import models
from user.models import User

# Create your models here.
class Chat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    message = models.CharField(max_length=1024)
    from_user = models.ForeignKey(User, null = False, related_name="from_name", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, null=False, related_name="to_user", on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user.username} sent ${self.message} to {self.to_user.username}"

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'from_user': self.from_user.to_dict(),
            'to_user': self.to_user.to_dict(),
        }

class RecentMessage(models.Model):
    pass