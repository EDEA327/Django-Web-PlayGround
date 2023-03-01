from django.db import models
from django.contrib.auth.models import User
from  django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles',null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True,max_length=200)

@receiver(post_save,sender = User)
def ensure_profile_exists(sender,instance,**kwargs):
    #* Nos aseguramos de que solo se ejecute la primera vez...
    if kwargs.get('created',False):
        Profile.objects.get_or_create(user = instance)
        print("Se acaba de crear un usuario y su perfil enlazado...")
