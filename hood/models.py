from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length = 50)
    neighbourhood_location = models.CharField(max_length = 50)
    occupants_count = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
      
    def __str__(self):
        return self.neighbourhood_name
    
    def create_neighbourhood(self):
        '''
        Method to create a neighbourhood
        '''
        self.create()
        
    def delete_neighbourhood(self):
        '''
        Method to delete a neighbourhood
        '''
        self.delete()
        
    @classmethod
    def get_neighbourhoods(cls):
        '''
        method thats gets all images posts from database
        '''
        Neighbourhoods = cls.objects.all()
        return Neighbourhoods
    
class Post(models.Model):
    name = models.CharField(max_length =50)
    post = models.ImageField(upload_to='posts/')
    profile = models.ForeignKey('Profile')
    post_caption = models.ForeignKey('Neighbourhood')
    date = models.CharField(max_lenght=20)
    business = models.ForeignKey('Business')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_post(cls):
        images = Post.object.all()
        return images
        
    @classmethod
    def get_post_by_id(cls, id):
        selected_post = Post.objects.filter_by(id=id)
        return selected_post

    @classmethod
    def get_post_by_neighbourhood_id(cls, neighbourhood_id):
        images = Post.objects.filter(id = neighbourhood_id).all()
        return images
    
class Business(models.Model):
    name = models.CharField(max_length = 30)
    b_email = models.CharField(max_length = 50)
    neighbourhood = models.ForeignKey('Neighbourhood')
    profile = models.ForeignKey('Profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'businesss/')

    def __str__(self):
        return self.name

    def create_business(self):
        self.create()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_businesses(cls):
        businesses = Business.objects.all ()
        return businesses

    @classmethod
    def search_by_neighbourhood(cls,search_term):
        businesses = cls.objects.filter(neighbourhood__neighbourhood_name__icontains=search_term)
        return businesses
    
class Profile(models.Model):
    name = models.CharField(max_length =30)
    neighbourhood = models.ForeignKey('Neighbourhood')
    email = models.CharField(max_length = 40)
    profile_pic = models.ImageField(upload_to='occupants/')
    occupants_id = models.IntegerField(unique = True)
    location = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
