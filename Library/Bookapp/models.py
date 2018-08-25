from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class userdetail(models.Model):
    user = models.OneToOneField(User)
   
    Address = models.CharField(max_length=100, default='')
    Email_ID =models.EmailField(max_length=50, default='')
    City = models.CharField(max_length=25, default='')
    State =models.CharField(max_length=25, default='')
    Country =models.CharField(max_length=25, default='')
    Pin_code =models.IntegerField(default='')
    Contact_Number =models.IntegerField(default='')

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_detail = userdetail.objects.create(user=kwargs['instances'])

    post_save.connect(create_profile, sender=user)
    