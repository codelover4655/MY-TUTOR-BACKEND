from rest_framework import serializers
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.models import User
from .models import *
User=get_user_model()



class macreateserializer(serializers.ModelSerializer):

    class Meta:
        model=mathtutor
        fields=('matutor','contact_no','address','aboutyou','img','doc','dis','distance')
    '''def save(self, **kwargs):
        data = self.validated_data
        user = self.context['request'].user
        title = data['title']
        todo = Todo.objects.create(creator=user, title=title)
        return todo'''
    def create(self, validated_data): 
         data = self.validated_data
         user=self.context['request'].user
         masstar = mathtutor.objects.create(matutor=user,contact_no=data['contact_no'], address=data['address'],aboutyou=data['aboutyou'],img=data['img'],doc=data['doc'])
         return masstar

        


   


