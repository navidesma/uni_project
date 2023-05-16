from django import forms
from django.urls import reverse
from tinymce.widgets import TinyMCE
from .models import Thread


class ThreadForm(forms.Form):
    title = forms.CharField(max_length=512)
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 15, 'rows': 4}
        )
    )
