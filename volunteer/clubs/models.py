from django.db import models
from django.contrib.auth.models import User

class CheerItems(models.Model):
    user = models.ForeignKey(User, on_delete='')
    items = models.CharField(max_length=10000)
    notes = models.CharField(max_length=500, blank=True)
    date_purchased = models.DateTimeField(auto_now=True)
