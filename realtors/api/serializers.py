from rest_framework import serializers
from realtors.models import Realtor
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User




class DetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Realtor
    fields = ('pk','name','photo','description','phone','email',
              'is_mvp','hire_date')

class DetailsSerializer1(serializers.ModelSerializer):
  class Meta():
    model = Realtor
    fields = ('pk','name','photo','description','phone','email',
              'is_mvp')


class LDetailsSerializer(serializers.ModelSerializer):
  class Meta():
    model = Realtor
    fields = ('pk','name','photo','description','phone','email',
              'is_mvp','hire_date')

 