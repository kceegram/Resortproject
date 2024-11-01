from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse

# decorator
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('User profile created successfully')
    else:
        print('Error occured, Profile not created')


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
           try:
               instance.Profile.save()
               print('Profile updated successfully')
           except Exception as e:
               print(f'Error occurred: {e}')
               instance.profile = None
    


    