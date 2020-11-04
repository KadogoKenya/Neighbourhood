from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
from cloudinary.models import CloudinaryField



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
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')


    def __str__(self):
        return f'{self.name} Neighbourhood'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, neighbour_id):
        return cls.objects.filter(id=neighbourhoods_id)

    @classmethod
    def get_all_neighbourhoods(cls):
        neighbourhoods = cls.objects.all()
        return neighbourhoods


    def get_absolute_url(self):        
        return reverse('index')
    

class Business(models.Model):
    name = models.CharField(max_length=255)
    # id=models.IntegerField()
    # user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    email=models.EmailField()
    image = CloudinaryField('images')
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)
    


    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def get_businesses(request, id):
        try:
            business = Business.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return business
    
    def _str_(self):
        return self.name
    
    class Meta:
        # ordering = ['-pub_date']
        verbose_name = 'My Business'
        verbose_name_plural = 'Business'

    


class Post(models.Model):
    post = models.TextField()
    image = CloudinaryField('images')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighbour')

    def __str__(self):
        return f'{self.post} Post'

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def find_post(cls, post_id):
        return cls.objects.filter(id=post_id)


# class User(models.Model):
#     name=models.CharField(max_length=25)
#     id=models.IntegerField()
#     emai=models.EmailField()
#     neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='neighbour')





