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
    post_caption = models.TextField()
    neighbourhood = models.ForeignKey('Neighbourhood')
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
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
    neighbourhood = models.ForeignKey('Neighbourhood',null=True,blank=True)
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
        businesses = cls.objects.all()
        return businesses

    @classmethod
    def search_by_neighbourhood(cls,search_term):
        businesses = cls.objects.filter(neighbourhood__neighbourhood_name__icontains=search_term)
        return businesses
    
class Profile(models.Model):
    neighbourhood = models.ForeignKey('Neighbourhood',null=True,blank=True)
    profile_pic = models.ImageField(upload_to='occupants/',default='')
    occupant_id = models.IntegerField(unique = True,null=True,blank=True)
    location = models.CharField(max_length=30,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
