from django.db.models import Model, IntegerField, ForeignKey, CharField, SET_NULL, DateTimeField
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Community(Model):
    name = CharField(max_length=512)
    short_description = CharField(max_length=128)
    description = HTMLField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class CommunitySubscription(Model):
    community = ForeignKey(Community, on_delete=SET_NULL, null=True)
    user = ForeignKey(User, on_delete=SET_NULL, null=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
