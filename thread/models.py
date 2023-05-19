from django.db.models import Model, IntegerField, ForeignKey, CharField, SET_NULL, DateTimeField, CASCADE
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from community.models import Community


class Thread(Model):
    creator = ForeignKey(User, on_delete=SET_NULL, null=True)
    title = CharField(max_length=512)
    community = ForeignKey(Community, on_delete=SET_NULL, null=True)
    content = HTMLField()

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def comments(self):
        return Comment.objects.filter(thread=self)


class Comment(Model):
    commenter = ForeignKey(User, on_delete=CASCADE)
    thread = ForeignKey(Thread, on_delete=CASCADE)
    content = HTMLField()
    parent = ForeignKey('self', on_delete=CASCADE, null=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def children(self):
        if self.parent is None:
            return Comment.objects.filter(parent=self)

        return None
