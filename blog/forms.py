from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post, Comment, Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
              "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="post"
              )
          }
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class': 'form-control content', 'rows': 2}),
        label='Comment')
    class Meta:
        model = Comment
        fields = ['content']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['bio', 'profile_pic']


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded', 'placeholder': 'Email'}), max_length=64)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'mt-1 block w-full p-2 border border-gray-300 rounded', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'fmt-1 block w-full p-2 border border-gray-300 rounded', 'form-label': 'confirm Password', 'placeholder': 'Password Again'}), label='password confirmation')
    class Meta:
        model = User
        fields = ['username', 'email', "password1", "password2"]


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

