from dataclasses import fields
from pyexpat import model
from django import forms
from App_Post.models import Post
class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['image','caption']