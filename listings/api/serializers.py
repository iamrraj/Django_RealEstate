from rest_framework import serializers
from listings.models import Listing
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from realtors.models import Realtor



class DetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Listing
    fields = ('pk','realtor','title','address','city','state',
              'zipcode','description','price','bedrooms','photo_main',
              'sqft','bathrooms','garage','lot_size','list_date')


class RetailsSerializer1(serializers.ModelSerializer):
  class Meta():
    model = Realtor
    fields = ('pk','name','photo','description','phone','email',
              'is_mvp')




class DetailsSerializer1(serializers.ModelSerializer):
  class Meta():
    model = Listing
    fields = ('pk','realtor','title','address','city','state',
              'zipcode','description','price','bedrooms','photo_main',
              'sqft','bathrooms','garage','lot_size','photo_1','photo_2',
              'photo_3','photo_4','photo_5','photo_6','is_published')


class LDetailsSerializer(serializers.ModelSerializer):
  # comments = RetailsSerializer1()
  class Meta():
    model = Listing
    fields = ('pk','realtor','title','address','city','state',
              'zipcode','description','price','bedrooms','photo_main',
              'sqft','bathrooms','garage','lot_size','photo_1','photo_2',
              'photo_3','photo_4','photo_5','photo_6','is_published','list_date')

 