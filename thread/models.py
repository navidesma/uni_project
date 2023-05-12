from django.db.models import Model, IntegerField, ForeignKey, CharField, TextField, SET_NULL, DateTimeField
from django.contrib.auth.models import User


# class Thread(Model):
#     creator_id = ForeignKey(User, on_delete=SET_NULL, null=True)
#     title = CharField(max_length=256)
#     content = TextField()
#     likes = IntegerField()
#
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)

