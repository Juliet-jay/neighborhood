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
        
        def__str__(self):
            return self.name
        
        @classmethod
        def get_post(cls):
            images = Post.object.all()
            return images
        
    @classmethod
    def get_post_by_id(cls, id):
    selected_post = Post.objects.filter_by(id=id)
    return selected_post

    
    
