'''
Created on 2017. 8. 30.
a
@author: kil kyung wan
'''

from .models import CompanyImage
from .models import Company
from rest_framework import serializers

 
class PhotoSeializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="company-detail")
    companyImage_image = serializers.ImageField(
            max_length = None, use_url=True
        ) 
    class Meta:
        model=CompanyImage
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """
    id =serializers.IntegerField(read_only=True)    
    company_category =  serializers.ManyRelatedField(required=False)
    company_name = serializers.CharField(required=False)
    company_content=serializers.CharField(required=False)
    """
  
    
    class Meta:
        model=Company
        fields='__all__'
    """
    def create(self,validated_data):
        return Company.objects.create(**validated_data)
        
    def update(self,instance,validated_data):
        instance.category=validated_data.get('category',instance.category)
        instance.name=validated_data.get('name',instance.name)
        instance.content=validated_data.get('content',instance.content)
        instance.save()
        return instance
    """