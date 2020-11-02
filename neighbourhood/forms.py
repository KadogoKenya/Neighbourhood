from django import forms
from django.contrib.auth.models import User
from .models import Neighbourhood,Business, Post
from users.models import Profile
from 


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields=['name','location','occupants_count','pub_date','description']
        


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','email','description','neighbourhood']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['post','date','user','neighbourhood']