from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author = models.ForeignKey(User, on_delete='')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_50_messages(self):
        return Message.objects.order_by('-timestamp').all()[:50]
