from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=250)
    description = models.CharField(blank=True, max_length=5000)
    website     = models.URLField(blank=True)
    address     = models.CharField(blank=True, max_length=500)
    date        = models.DateTimeField(auto_now_add=True)
    post_id     = models.AutoField(primary_key=True)

class VolunteeringLog(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    agency_name         = models.CharField(max_length=250)
    activity            = models.CharField(max_length=1000)
    hours               = models.CharField(max_length=250)
    date_activity       = models.CharField(max_length=250)
    supervisor_contact  = models.CharField(max_length=1000)
    signature           = models.CharField(max_length=50000)

class VolunteeringQuestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question1 = models.CharField(max_length=1000)
    question2 = models.CharField(max_length=1000)
    question3 = models.CharField(max_length=1000)
    question4 = models.CharField(max_length=1000)
