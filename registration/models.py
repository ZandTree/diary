from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

def upload_avatar(instance,filename):
    """
    builds the media path for where it will store the avatar imgage
    """
    file_extention = filename.split('.')[1]
    start_file = filename.split('.')[0]
    time = timezone.now().strftime('%Y-%m-%d')
    if len(start_file) < 5:
        generic_file_name = start_file + time
    else:
        generic_file_name = start_file[:5] + time
    filename = generic_file_name + '.' + file_extention
    return os.path.join('avatars','user_{0}','{1}').format(instance.user.id,filename)

class Profile(models.Model):
    user = models.OneToOneField(User,primary_key = True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,default = "")
    last_name = models.CharField(max_length=60,default="")
    avatar = models.ImageField(default = 'default.jpg',upload_to=upload_avatar)
    age = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=70,default="")
    bio = models.CharField(max_length=300,default = "")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
    @property
    def full_name(self):
        if self.user.first_name and self.user.last_name:
            return "{0.first} {0.last_name}".format(self.user)
        return "{}".format(self.user.username)
        #return "{}".format(self.user.get_username())

    @property
    def get_avatar_url(self):
        if self.avatar:
            return '/media/{}'.format(self.avatar)
        return '/media/default.jpg'

@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwargs):
    """As New User created, create Profile"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    """As New User created, save Profile"""
    instance.profile.save()

# @receiver(post_save, sender=User)
# def create_profile_handler(sender, instance, **kwargs):
#     """As New User created, create and attach Profile"""
#     if kwargs.get('created'):
#         profile = Profile.objects.create(user=instance)
