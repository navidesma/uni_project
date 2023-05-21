from django.contrib.auth.models import User
from django.db.models import CharField
from django.db import models


class ProfilePicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = CharField(max_length=1024)
