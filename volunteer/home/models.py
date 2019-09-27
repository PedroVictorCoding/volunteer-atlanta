from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete='')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=5000)
    website = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
