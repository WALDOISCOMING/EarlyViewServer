'''
Created on 2017. 8. 26.
a
@author: kil kyung wan
'''
from django.contrib.auth.models import Group,User
from rest_framework import serializers
from User.models import NormalUser
from Category.models import Category

 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields=('id','category_name')
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    #profile = ProfileSerializer()
    category =  serializers.CharField(
         write_only=True,
    )
    
    birthday = serializers.DateField(      
        write_only=True)
 
    password = serializers.CharField(
        write_only=True,
    )
    class Meta:
        model = User
        
        fields = ('username','email', 'password','birthday','category')
 #       write_only_fields=('user_password',)
        
    
    
    def create(self, validated_data):
        user = User.objects.filter(email=validated_data['email'])
        if user:
            raise serializers.ValidationError("email '"+validated_data['email']+"' already exists" )
        else:
            normaluser = NormalUser(username=validated_data['username'],email=validated_data['email'],birthday=validated_data['birthday'],category=validated_data['category'])
            normaluser.save()
            print(validated_data['birthday'])
            
            return User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])




class NormalSerializer(serializers.ModelSerializer):
    """
    id =serializers.IntegerField(read_only=True)    
    company_category =  serializers.ManyRelatedField(required=False)
    company_name = serializers.CharField(required=False)
    company_content=serializers.CharField(required=False)
    """
  
    
    class Meta:
        model=NormalUser
        fields='__all__'