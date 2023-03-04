from django.db import models
from django.contrib.auth.models import User
from  django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
def custom_upload_to(instance,filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'users_profiles/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True,max_length=200)

    class Meta:
        ordering = ['user__username']

@receiver(post_save,sender = User)
def ensure_profile_exists(sender,instance,**kwargs):
    #* Nos aseguramos de que solo se ejecute la primera vez...
    if kwargs.get('created',False):
        Profile.objects.get_or_create(user = instance)
        #print("Se acaba de crear un usuario y su perfil enlazado...")
