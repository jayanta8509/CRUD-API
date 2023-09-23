from rest_framework import serializers
from .models import *


class studentSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = student
      fields = '__all__'


   def validate(self , data):
       
       if data ['roll'] <100:
          raise serializers.ValidationError({'error' : "Roll Number less then 100"})
       if data ['name']:
          for n in data['name']:
             if n.isdigit():
                raise serializers.ValidationError({'error' : "name can not numrric"})
       return data
