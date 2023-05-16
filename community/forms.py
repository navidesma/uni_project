from django import forms
from tinymce.widgets import TinyMCE


class CommunityForm(forms.Form):
    name = forms.CharField(max_length=512)
    short_description = forms.CharField(max_length=128)
    description = forms.CharField(
        widget=TinyMCE(
            attrs={'cols': 15, 'rows': 4}
        )
    )
