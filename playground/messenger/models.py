from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
