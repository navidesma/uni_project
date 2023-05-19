from django import forms
from tinymce.widgets import TinyMCE


class ThreadForm(forms.Form):
    title = forms.CharField(max_length=512)
    community = forms.CharField(max_length=64)
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 15, 'rows': 4}
        )
    )


class CommentForm(forms.Form):
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 1, 'rows': 1}
        )
    )
    parent = forms.IntegerField(required=False)
