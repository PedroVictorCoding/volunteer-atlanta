from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete="")

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile, sender=User)


class VolunteeringLog(models.Model):
    user                = models.ForeignKey(User, on_delete='')
    agency_name         = models.CharField(max_length=250)
    activity            = models.CharField(max_length=1000)
    hours               = models.CharField(max_length=250)
    date_activity       = models.CharField(max_length=250)
    supervisor_contact  = models.CharField(max_length=1000)
