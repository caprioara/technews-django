from markdownx.fields import MarkdownxFormField
from django import forms


class FormNews(forms.Form):
    body_txt = MarkdownxFormField()