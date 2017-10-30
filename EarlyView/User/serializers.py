'''
Created on 2017. 8. 26.
a
@author: kil kyung wan
'''
from django.contrib.auth.models import User, Group
from rest_framework import serializers
 
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups','password')
        
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
