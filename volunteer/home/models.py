from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user        = models.ForeignKey(User, on_delete='')
    title       = models.CharField(max_length=250)
    description = models.CharField(blank=True, max_length=5000)
    website     = models.URLField(blank=True)
    address     = models.CharField(blank=True, max_length=500)
    date        = models.DateTimeField(auto_now_add=True)
    post_id     = models.AutoField(primary_key=True)

class Friend(models.Model):
    users           = models.ManyToManyField(User)
    current_user    = models.ForeignKey(User, related_name='owner', on_delete='', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
