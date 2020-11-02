from django import forms
from django.contrib.auth.models import User
from .models import Neighbourhood,Business, Post
from users.models import Profile



class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields=['name','location','occupants_count','Admin','description']
        


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','email','image','description','neighbourhood','health','police']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['post','user','image','neighbourhood']