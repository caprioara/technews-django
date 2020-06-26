from markdownx.fields import MarkdownxFormField
from django import forms

class NewsForm(forms.Form):
    body_txt = MarkdownxFormField()