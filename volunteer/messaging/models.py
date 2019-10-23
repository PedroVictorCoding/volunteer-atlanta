from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author      = models.ForeignKey(User, on_delete='')
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    room        = models.TextField()

    def __str__(self):
        return self.author.username
