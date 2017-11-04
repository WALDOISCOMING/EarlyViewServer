'''
Created on 2017. 10. 30.
실 값.
@author: kil kyung wan
'''

from Category.models import Category
from django.contrib.auth.models import  Group,User
from .models import NormalUser
from rest_framework import viewsets, status
from User.serializers import UserSerializer,NormalSerializer,CategorySerializer
from rest_framework.decorators import detail_route, permission_classes 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
 
 

 
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @detail_route(methods=['get'],permission_classes=[IsAuthenticatedOrReadOnly],url_path='emailfilter')    
    def emailcheck(self,request,pk=None):
       
        api_result = User.objects.filter(email=pk).order_by('-id')
        serializer_class = UserSerializer(api_result)
        return Response(serializer_class.data)
    




class NormalUserViewSet(viewsets.ModelViewSet):
    
    queryset = NormalUser.objects.order_by('-id')
    serializer_class = NormalSerializer
    
    
    
    

class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.order_by('-id')
    serializer_class = CategorySerializer