from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Models):
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
        
    
    
    
