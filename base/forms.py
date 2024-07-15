from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "border border-gray-400 p-2 w-full rounded-lg focus:outline-none focus:border-blue-400"}))
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "border border-gray-400 p-2 w-full rounded-lg focus:outline-none focus:border-blue-400"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "border border-gray-400 p-2 w-full rounded-lg focus:outline-none focus:border-blue-400",
                                                        'rows': 10}))
    class Meta:
        model = Blog
        fields = ['title', 'author', 'body']

