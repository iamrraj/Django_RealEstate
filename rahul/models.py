from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from django.utils import timezone
import datetime
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField( max_length = 100, null = True )
    last_name = models.CharField( max_length = 100, null = True )
    picture = models.ImageField( null = True, blank = True, default = 'no-img.png' )
    email = models.EmailField( max_length = 100, null = True )
    phone = models.CharField( max_length = 100, null = True )
    country = models.CharField( max_length = 100, null = True )
    city = models.CharField( max_length = 100, null = True )


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

    def get_website(self):
        if self.website[0:4] != 'http':
            return 'http://' + self.website
        else:
            return self.website

    def __str__(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return 'Student'



class Categoty(models.Model):
    Id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=200)

    def __str__( self ):
        return self.name

    def __unicode__(self):
        return self.Id

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now



class Product(models.Model):
    categoty = models.ForeignKey(Categoty, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    image = models.ImageField(blank = True, null = True)
    file = models.FileField(blank = True, null = True)
    description = HTMLField()
    specification = HTMLField()
    seller = models.CharField(max_length = 100)
    pub_date = models.DateTimeField( 'Date published' )
    available = models.BooleanField(default=True)

    def __str__( self ):
        return self.name

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now

class Slide(models.Model):
    Id = models.AutoField(primary_key=True)
    image = models.ImageField(blank = True, null = True)
    image1 = models.ImageField(blank = True, null = True)
    image2 = models.ImageField(blank = True, null = True)
    image3 = models.ImageField(blank = True, null = True)

    def __str__( self ):
        return self.image
    
    def __unicode__(self):
        return self.Id

