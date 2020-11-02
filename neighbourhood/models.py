from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    

class Business(models.Model):
    name = models.CharField(max_length=255)
    # id=models.IntegerField()
    # user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    email=models.EmailField()
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)


class Post(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighbour')

# class User(models.Model):
#     name=models.CharField(max_length=25)
#     id=models.IntegerField()
#     emai=models.EmailField()
#     neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighbour')





