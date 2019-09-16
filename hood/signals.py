
#signal fired after an obj is saved in this cas when a user is created
from django.db.models.signals import post_save
#user to sender the signal
from django.contrib.auth.models import User
#reciever of the signal
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    
   if created:
       Profile.objects.create(user=instance)
       
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
   '''
   save profile once a user is saved
   '''
   instance.profile.save()

